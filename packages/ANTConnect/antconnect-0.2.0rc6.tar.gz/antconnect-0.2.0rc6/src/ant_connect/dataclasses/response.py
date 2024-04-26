from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Response:
    request_id: str
    code: str
    message: str
    timestamp: datetime

    @classmethod
    def create_response_from_json(cls, response_dict: dict) -> Response:
        return cls(
            request_id=response_dict["requestId"],
            code=response_dict["code"], 
            message=response_dict["message"], 
            timestamp=response_dict["timestamp"]
        )

@dataclass
class TokenResponse:
    token_type: str
    expires_in: int
    access_token: str
    refresh_token: str

    @classmethod
    def from_json(cls, request_response: dict) -> TokenResponse:
        return TokenResponse(
            token_type=request_response["token_type"], 
            expires_in=request_response["expires_in"], 
            access_token=request_response["access_token"],
            refresh_token=request_response["refresh_token"]
        )