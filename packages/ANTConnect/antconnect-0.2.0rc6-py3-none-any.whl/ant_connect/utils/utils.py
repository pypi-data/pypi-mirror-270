"""
Module containing utils for the scripts and auto generation for ANT v2 package
"""
import re
from typing import Union, Tuple
from enum import Enum

from ant_connect.enums import DataType, Priority


def enum_check(data_type: Union[str, None], example: list[str]) -> Union[str, DataType, Priority, None]:
    """helper function to check if an argument or attribute could be an
    enum from the enums.py module.

    Args:
        data_type (Union[str, None]): data type of the attribute or argument.
        example (list[str]): examples list from the ANT data model, if 
        provided.

    Returns:
        Union[str, DataType, Priority, None]: If data type is no enum a 
        str is returned, else return is the corresponding enum. None will
        be returned if no data type is provided.
    """
    # check if data_type is enum
    if data_type is not None and type(example) == list and type(example[0]) == str:
        # check if example is enum, then sub_type is enum
        if example[0] in DataType._value2member_map_:
            data_type = "DataType"
        elif example[0] in Priority._value2member_map_:
            data_type = "Priority"

    return data_type


def type_conversion(json_data_type: str) -> str:
    """converts a JSON data type Python data type.

    Args:
        json_data_type (str): input a json data type string

    Returns:
        str: converted Python data type string
    """

    conversion_dict = {
        "string": "str",
        "boolean": "bool",
        "integer": "int",
        "array": "list",
        "object": "dict",
        "number": "float",
        None: None
    }

    return conversion_dict[json_data_type]


def tag_conversion(api_tag: str) -> str:
    """converts a paths tag to an object model name.
    Use this as a temp solution. Tags and schemas should match!

    Args:
        api_tag (str): input as an api data model tag

    Returns:
        str: converted tag name to model name
    """
    conversion_dict = {

    }

    if api_tag in conversion_dict:
        return conversion_dict[api_tag]
    return api_tag


def convert_defaults(default: str) -> Union[str, bool, list, dict]:
    """If the attribute or argument from the data model has a default 
    value, convert it a string.

    Strings will be added to the model of meethod definition, generating
    the models.py

    Args:
        default (str): attribute / argument defaults values

    Returns:
        Union[str, bool, list, dict]: type of the default value, if 
        there is any.
    """
    if default == 'false' or default == 'true':
        converted = default.capitalize()
    elif default is None:
        converted = default
    else:
        converted = "'" + default + "'"

    return converted


def camel_to_snake(name: str) -> str:
    """Helper function converting camel case to snake case variables 
    with regex.

    Args:
        name (str): camel case variable

    Returns:
        str: snake case variable
    """
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def check_parameter_name(parameter_name: str) -> str:
    """ Convert parameter names for the models in the data model to 
    more descriptive names: 'project' will become 'project_id'.

    Args:
        parameter_name (str): model parameter / argument

    Returns:
        str: converted parameter/ argument
    """
    if "[" in parameter_name:
        argument = parameter_name.lower().replace('[', '_').replace(']', '')
    else:
        argument = parameter_name.lower() + "_id"

    return argument


def method_name_conversion(operation_id: str, tag: str) -> str:
    """Converts the operationId from data model to agreed upon
    method name

    Args:
        operation_id (str): operation ID from json data model

    Returns:
        str: converted method name to be used in api package
    """
    # create method names without tags in name (also if plural)
    method_no_tag = ''
    plural_tag = tag + 's'
    if plural_tag in operation_id:
        method_no_tag = operation_id.replace(plural_tag, '').replace('get', 'all')
    elif tag in operation_id:
        method_no_tag = operation_id.replace(tag, '')
    else:
        method_no_tag = operation_id

    # strip from clutter and convert to snake case
    new_operation_id_snake = camel_to_snake(name=method_no_tag.replace('V2', '').replace('2', '')).replace('_from', '')

    # if name is 'store' convert to 'create' instead
    if new_operation_id_snake == 'store':
        new_operation_id_snake = 'create'

    # if name ends with '_to' remove it from the name. Is also clutter due tag name removal
    if new_operation_id_snake.split('_')[-1] == 'to':
        new_operation_id_snake = new_operation_id_snake.split('_')
        new_operation_id_snake.pop(-1)
        new_operation_id_snake = "_".join(new_operation_id_snake)

    return new_operation_id_snake


def get_nested_value_by_path(data: dict, path: str) -> Union[str, None]:
    """Get a nested value from a dictionary by a path string. 
    Example path: "#/components/schemas/BaseModel/properties/id"

    Args:
        data (dict): input data as a dictionary
        path (str): path to the value in the dictionary

    Returns:
        str: value from the dictionary
    """
    # split path into list
    type_reference_list = path.split('/')
    # get the data type from the data model by using the list with path recursively
    if type_reference_list[0] == "#":
        type_reference_list.pop(0)
    for i in range(len(type_reference_list)):
        data = data.get(type_reference_list[i], {})
    json_data_type = data.get("type", None)

    return json_data_type