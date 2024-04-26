from enum import Enum


class HttpMethodType(Enum):
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"
    POST = "POST"


class DataType(Enum):
    """possible column data types

    Args:
        * "text"
        * "text-field"
        * "integer"
        * "boolean"
        * "date"
        * "link"
        * "email"
        * "dropdown"
        * "document"
        * "float"
        * "sbscode"
        * "table"
    """
    TEXT = "text"
    TEXT_FIELD = "text-field"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    DATE = "date"
    LINK = "link"
    EMAIL = "email"
    DROPDOWN = "dropdown"
    DOCUMENT = "document"
    FLOAT = "float"
    SBSCODE = "sbscode"
    TABLE = "table"


class Priority(Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    URGENT = "urgent"