"""
Module with classes to parse and create Python object from the ant data model.
"""
from __future__ import annotations
from dataclasses import dataclass
from urlpath import URL
from pathlib import Path
from typing import Union
import re
import json
import requests

from ant_connect.utils import type_conversion, tag_conversion, method_name_conversion, enum_check
from ant_connect.utils import check_parameter_name, convert_defaults, get_nested_value_by_path

@dataclass
class AntDataModelLoader:
    """ant data model class helper to fetch ant data model and/or 
    write data model to json file.
    """
    json_data: dict
    schemas: dict
    paths: list[tuple]

    @classmethod
    def fetch_ant_data_model(cls, url: URL) -> AntDataModelLoader:
        """class method to fetch the ant data model and collect the
        paths and schemas.

        Args:
            url (URL): URL object to the host

        Raises:
            ValueError: error when connection to the host has failed
            ValueError: error when fetching the ant data model

        Returns:
            AntDataModelLoader: ant data model object with schema's and paths
        """
        try:
            response = requests.get(str(url))
            if response.status_code == 200:
                json_data = response.json()
            else:
                raise ValueError(f"Connection to host '{url}' failed.") 
        except requests.RequestException as e:
            raise ValueError(f"Error fetching ant data model: {e}")
        
        return cls(
            json_data=json_data,
            schemas=json_data["components"]["schemas"],
            paths=json_data["paths"]
            )

    @classmethod
    def from_json(cls, file_path: str) -> AntDataModelLoader:
        """ class method to load the ant data model from a json file. """
        with open(file_path, 'r') as f:
            json_data = json.load(f)

        # creates a list of tuples containing the paths and properties for each method
        paths_list = [(path, {http_method: properties}) for path, dict in json_data["paths"].items() for http_method, properties in dict.items()]

        return cls(
            json_data=json_data,
            schemas=json_data["components"]["schemas"],
            paths=json_data["paths"]
        )

    def write_to_json_file(self, file_name: str, file_path: Union[Path, str]) -> None:
        """class method to write the full ant data model to a json file 

        Args:
            file_name (str): name of the json file
        """
        extension = ".json"
        if extension not in file_name:
            file_name = "".join((file_name, extension))
        file_loc = file_path / file_name
        with open(file_loc, 'w') as file:
            json.dump(self.json_data, file, indent=4)


@dataclass
class AntPropertyDefinition:
    """ Dataclass to define a property in the models and methods. """
    name: str
    data_type: str
    required: bool
    sub_type: Union[str, None] = None
    default: Union[str, None] = None

    def to_python_definition(self) -> str:
        """Create a string from the property definition"""
        if not self.required:
            if self.sub_type is None:
                object_property = f"{self.name}: Union[{self.data_type}, None]"
            else:
                object_property = f"{self.name}: Union[{self.data_type}[{self.sub_type}], None]"
        elif self.sub_type is not None:
            object_property = f"{self.name}: {self.data_type}[{self.sub_type}]"
        else:
            object_property = f"{self.name}: {self.data_type}"

        if not self.required:
            object_property += f' = {self.default}'

        return object_property


@dataclass
class AntModelDefinition:
    """ Dataclass to define a model from the data model. """
    name: str
    properties: list[AntPropertyDefinition]

    @classmethod
    def from_json(cls, name: str, properties: dict, json_data: dict) -> AntModelDefinition:
        """ Create a model definition from the json data model. """
        ant_properties_list = []
        if properties.get("properties") is not None:
            for key, value in properties["properties"].items():
                sub_type = None
                if value.get("type") is not None:
                    data_type = type_conversion(json_data_type=value.get("type"))
                    sub_type = type_conversion(value.get("items", {}).get("type"))
                    example = value.get("example")
                    # check if data_type is enum
                    if isinstance(example, list):
                        data_type = enum_check(data_type=data_type, example=example)
                # if the data type is not specified in the properties, check the $ref
                elif isinstance(value.get("$ref"), str):
                    json_data_type = get_nested_value_by_path(data=json_data, path=value.get("$ref", " "))
                    data_type = type_conversion(json_data_type=json_data_type)
                else:
                    raise ValueError("No correct data type for argument found in data model")
                # check if property is required
                required = False
                default = None
                if key in properties.get("required", []):
                    required = True
                # TODO: when default values are added to data model, add these to object definition
                if not required:
                    pass
                ant_properties_list.append(AntPropertyDefinition(name=key, data_type=data_type, sub_type=sub_type, required=required, default=default))

        return cls(
            name=name,
            properties=ant_properties_list
        )

    def to_python_definition(self, model_base_class_name: str) -> str:
        """Create a python class definition as a string from the model definition"""

        # Define the different elements of a python class definition
        header_str = f"class {self.name}({model_base_class_name}):"
        docstring = f"\"\"\"Python dataclass for the {self.name} schema\"\"\""
        property_strings = [property.to_python_definition() for property in self.properties]

        # Add all the elements together and add the lines to one big string 
        # Add the class header lines and the class body lines
        body_lines = [docstring] + property_strings

        # Create strings for the header and body (add indentation for body)
        body_str = "\n".join(["\t" + line for line in body_lines])

        # Make one big string
        class_definition_string = "\n" + header_str + "\n" + body_str

        return class_definition_string


@dataclass
class AntMethodDefinition:
    """ Dataclass to define a method for a model from the data model. """
    http_method: str
    tag: str
    endpoint: str
    docstring: str
    method_name: str
    arguments: list[AntPropertyDefinition]
    request_body_type: str
    request_args_def: list[AntPropertyDefinition]
    response_type: str

    @staticmethod
    def get_response_type(method_properties: dict) -> str:
        """ Get the response type from the method properties. """
        # There are 5 response type objects, check response code
        if method_properties.get("responses", {}).get("200", None) is None:
            response_object = method_properties.get("responses", {}).get("201", None)
        else:
            response_object = method_properties.get("responses", {}).get("200", None)

        # Start filtering the response type to return te correct response object for the method
        # if response is 'Any' (usually a document) 
        response_type = None
        if response_object.get("content", None) is None:
            response_type = 'Any'
        else:
            schema_type = response_object.get("content", {}).get("application/json", {}).get("schema", {}).get("type", None)
            # if response is an object from the data model schemas 
            if schema_type is None:
                response_type = response_object.get("content", {}).get("application/json", {}).get("schema", {}).get("$ref", None).split('/')[-1]
            # if response is an object not specified in the schemas
            elif schema_type == "object":
                response_type = type_conversion(json_data_type=schema_type)
            elif schema_type == "array":
                items_type = response_object.get("content", {}).get("application/json", {}).get("schema", {}).get("items", None)
                # if response is an array of objects from the data model schemas
                if items_type.get("$ref", None) is not None:
                    model_name = items_type.get("$ref", None).split('/')[-1]
                    response_type = f"list[{model_name}]"
                # if response is an array of objects not from the data model schemas
                elif items_type.get("properties", None) is not None:
                    model_name = 'dict'
                    response_type = f"list[{model_name}]"
        if 'deletedMessage' in response_type:
            response_type = 'BaseModel.deletedMessage'

        if response_type == 'record':
            response_type = 'dict'

        if response_type is None:
            raise ValueError("No correct response type found, check data model")

        return response_type.replace('v2', 'V2')

    @classmethod
    def from_json(cls, path: str, properties: dict, json_data: dict) -> AntMethodDefinition:
        """ Create a method definition from the json data model. """
        # when exclude in "operationId" do not create method
        for key, value in properties.items():
            # CHECK if method needs to be ignored
            if 'exclude' in value["operationId"].lower():
                continue
            if 'import' in value["operationId"].lower():
                continue

            http_method = key
            tag = tag_conversion(value["tags"][0])
            docstring = value.get("description")
            operation_id = value.get("operationId")
            method_name = method_name_conversion(operation_id=operation_id, tag=tag)

            # CHECK if params are needed in url endpoint
            arguments_list: list[AntPropertyDefinition] = []
            for i, parameter in enumerate(value.get("parameters", {})):
                # parse argument and argument type for method definition line
                argument = check_parameter_name(parameter.get("name"))
                parameter_schema_type = type_conversion(parameter.get("schema", {}).get("type"))
                is_required = parameter.get("required")
                arguments_list.append(AntPropertyDefinition(name=argument, data_type=parameter_schema_type, required=is_required))

                # check if param in endpoint url, to replace name
                path_search = "{" + parameter.get("name").replace("[id]", "") + "}"
                if path_search in path:
                    path = path.replace(path_search, "{" + f"{argument}" + "}")

            # CHECK if request body is needed
            request_body_schema = value.get("requestBody", {}).get("content", {}).get("application/json", {}).get("schema", {})
            request_body_type = type_conversion(json_data_type=request_body_schema.get("type"))
            request_args_def: list[AntPropertyDefinition] = []
            if request_body_type is not None:
                # parse argument and argument type for request params and method definition line
                for argument, properties in request_body_schema.get("properties", {}).items():
                    name = argument.replace('-', '_')
                    if name == 'import':
                        name = "is_" + name
                    arg_type = properties.get("type", None)
                    # no type then check for $ref
                    if arg_type is None:
                        ref_type_string = properties.get("$ref", None)
                        if ref_type_string is not None:
                            arg_type = get_nested_value_by_path(data=json_data, path=ref_type_string)
                            ref_type_string_split = ref_type_string.split("/")
                            if ref_type_string_split[-1] == "id":
                                name = "".join((name, "_id"))
                    arg_type = type_conversion(json_data_type=arg_type)
                    sub_type = type_conversion(json_data_type=properties.get("items", {}).get("type"))
                    example = properties.get("example")
                    # check if data_type is enum
                    if isinstance(example, list):
                        arg_type = enum_check(data_type=arg_type, example=example)
                    # read defaults
                    default = convert_defaults(properties.get("default"))
                    is_required = False
                    if argument in request_body_schema.get("required", []):
                        is_required = True
                    request_args_def.append(AntPropertyDefinition(name=name, data_type=arg_type, required=is_required, default=default, sub_type=sub_type))
            # if name of arg in requestbody matches name params, change name also to <name>_id
            for i in request_args_def:
                for j in arguments_list:
                    if i.name in j.name:
                        i.name = j.name
            arguments_list += request_args_def # combine all args for method definition line

            # CHECK for args doubles 
            double_check = []
            for arg in arguments_list:
                if arg.name in double_check:
                    arguments_list.remove(arg)
                double_check.append(arg.name)

            # CHECK response
            response_type = AntMethodDefinition.get_response_type(method_properties=value)

            return cls(
                http_method=http_method,
                tag=tag, 
                endpoint=path,
                docstring=docstring, 
                method_name=method_name, 
                arguments=arguments_list, 
                request_body_type=request_body_type,
                request_args_def=request_args_def,
                response_type=response_type
            )

    def to_python_definition(self) -> str:
        """Create a python method definition as a string from the data model definition"""

        # define the method elements
        classmethod_str = "\t@classmethod"
        # sort args line
        arguments_unsorted  = [arg.to_python_definition() for arg in self.arguments]
        arguments_sorted = sorted(arguments_unsorted, key=lambda x: " = " in x) # sort all args with default value to the back
        arguments_str = ", ".join(arguments_sorted) 
        if arguments_str:
            arguments_str = ", ".join(("cls", arguments_str))
        else:
            arguments_str = "cls"

        if "dict" in self.response_type or "deletedMessage" in self.response_type:
            model_instance_str = "response.json()"
        elif "Any" in self.response_type:
            model_instance_str = "response"
        elif "list" in self.response_type:
            model_extract = re.findall(r'\[(.*?)\]', self.response_type)[0]
            model_instance_str = f"[{model_extract}._from_json(i) for i in response.json()]"
        else:
            model_instance_str = f"{self.response_type}._from_json(response.json())"

        method_definition_str = f"\tdef {self.method_name}({arguments_str}) -> {self.response_type}:"
        docstring = f"\t\t\"\"\"{self.docstring}\"\"\""
        if self.request_args_def:
            params_var_str_start = "\t\tparameters = {\n"
            params_var_str_mid = "".join(f"\t\t\t'{arg.name.replace('_id', '')}': {arg.name},\n" for arg in self.request_args_def)
            params_var_str_end = "\t\t\t}"
            params_var_str = "".join((params_var_str_start, params_var_str_mid, params_var_str_end, "\n\n"))
            if "Any" in self.response_type:
                response_str = f"\t\tresponse = {self.tag}._call_api(method_type=HttpMethodType.{self.http_method.upper()}, endpoint=endpoint, parameters=parameters)"
            else:
                response_str = f"\t\tresponse: requests.Response = {self.tag}._call_api(method_type=HttpMethodType.{self.http_method.upper()}, endpoint=endpoint, parameters=parameters)"
        else:
            params_var_str = ""
            if "Any" in self.response_type:
                response_str = f"\t\tresponse = {self.tag}._call_api(method_type=HttpMethodType.{self.http_method.upper()}, endpoint=endpoint)"
            else:
                response_str = f"\t\tresponse: requests.Response = {self.tag}._call_api(method_type=HttpMethodType.{self.http_method.upper()}, endpoint=endpoint)"

        # endpoint basic or endpoint complex
        endpoint_str = f'\t\tendpoint = f"{self.endpoint[1:]}"'

        # check response code
        response_code_ok = f"\t\tif response.ok:\n\t\t\treturn {model_instance_str}"
        response_code_not_ok = f"\t\telse:\n\t\t\traise ValueError(f'Could not load data from API, response code {{response.status_code}} with response {{response.text}}')"

        # method definition string
        method_definition_to_str = classmethod_str + "\n" + method_definition_str + "\n" + docstring + "\n" + params_var_str + endpoint_str + "\n" + response_str + "\n" + response_code_ok + "\n" + response_code_not_ok
        return method_definition_to_str