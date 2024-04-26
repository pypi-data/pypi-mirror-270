""" Model Base Class setup module"""
import requests
import json
from urlpath import URL
from pydantic import BaseModel
from enum import Enum
from abc import ABC
from time import sleep, perf_counter
from typing import Union, ClassVar
from typing_extensions import Self

from ant_connect.config import HostUrlConfig, RequestsConfig, ThrottleConfig
from ant_connect.enums import HttpMethodType

class ModelBaseClass(BaseModel, ABC):
	""" Model Base Class """
	_get_host: ClassVar[URL] = HostUrlConfig.host / HostUrlConfig.type / HostUrlConfig.version
	_access_token: ClassVar[str] = ""
	_headers: ClassVar[dict] = RequestsConfig.headers.copy()
	_throttle_counter: ClassVar[int] = 0
	_time: ClassVar[float] = 0.0
	_is_timing: ClassVar[bool] = False
	_auto_throttle: ClassVar[bool] = False

	@classmethod
	def _from_json(cls, json) -> Self:
		"""Get an instance of the model by id"""

		return cls(**json)

	@classmethod
	def _call_api(cls, method_type: HttpMethodType, endpoint: str, parameters: Union[dict, None] = None) -> requests.Response:
		"""Model base class for http requests with build-in throttle. 
		See the config for throttle constants.

		Args:
			method_type (HttpMethodType): http method type enum
			endpoint (str): url endpoint for http request
			parameters (Union[dict, None], optional): parameters as request content. Defaults to None.

		Raises:
			ValueError: error is thrown when auto_throttle is False and requests in time-frame has exceeded
			ValueError: error is thrown when invalid http method is given.

		Returns:
			requests.Response: response object from request
		"""
		# check requests count for throttle
		if ModelBaseClass._is_timing:
			if ModelBaseClass._throttle_counter < ThrottleConfig.amount:
				ModelBaseClass._throttle_counter += 1
			else:
				if ModelBaseClass._auto_throttle:
					while perf_counter() - ModelBaseClass._time <= ThrottleConfig.time_frame:
						sleep(0.001)
				else: 
					raise ValueError(f"Too many requests received {ThrottleConfig.time_frame} seconds. \
						Change your process or turn auto_throttle on with the ApiConnector class")

				ModelBaseClass._time = perf_counter()
				ModelBaseClass._throttle_counter = 1
		else:
			ModelBaseClass._time = perf_counter()
			ModelBaseClass._throttle_counter = 1
			ModelBaseClass._is_timing = True


		# set url and parameters for http request
		url = str(ModelBaseClass._get_host / endpoint)
		ModelBaseClass._headers["Authorization"] = RequestsConfig._placeholder_string.format(ModelBaseClass._access_token)

		if parameters is None:
			parameters ={}
		else:
			for key, value in parameters.items():
				if isinstance(value, Enum):
					parameters[key] = value.value

		request_data = json.dumps(parameters)

		match method_type:
			case HttpMethodType.GET:
				return requests.get(url=url, params=request_data, headers=ModelBaseClass._headers, verify=RequestsConfig.verify)
			case HttpMethodType.PUT:
				return requests.put(url=url, headers=ModelBaseClass._headers, data=request_data, verify=RequestsConfig.verify)
			case HttpMethodType.DELETE:
				return requests.delete(url=url, headers=ModelBaseClass._headers, data=request_data, verify=RequestsConfig.verify)
			case HttpMethodType.POST:
				return requests.post(url=url, headers=ModelBaseClass._headers, data=request_data, verify=RequestsConfig.verify)
			case _:
				raise ValueError("No correct HTTP method was provided")