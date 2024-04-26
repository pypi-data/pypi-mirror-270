###############################################################################
#
# (C) Copyright 2024 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################
import json
from typing import Any
from everysk.core.datetime import DateTime, Date

## Private functions
def _default(obj: Any) -> str: # pylint: disable=inconsistent-return-statements
    """
    Is used on JSONEncoder to convert objects to JSON format.

    Args:
        obj (Any): The object that needs to be changed into JSON format.

    Returns:
        str: The JSON representation of the object

    Usage:
        This function is typically used internally by JSONEncoder and should not be called directly.
    """
    if Date.is_date(obj) or DateTime.is_datetime(obj):
        return obj.isoformat()

    if obj == Undefined:
        return Undefined.default_parse_string


def _json_parser(obj: Any, convert_str_to_date: bool = False) -> Any:
    """
    Transforms all strings in their correct objects.

    This function recursively traverses a JSON-like structure and converts JSON strings into their
    correct Python object representations. It handles conversion of strings to Date, DateTime, or
    Undefined objects.

    Args:
        obj (Any): The object that needs to be changed into object.
        convert_str_to_date (bool): Enable conversion of str to Date and Datetime. Default is False
    Returns:
        Any: The transformed object with JSON strings converted into appropriate Python objects

    Notes:
        - If the input is a dictionary, it recursively parses each key-value pair.
        - If the input is a list, it recursively parses each item.
        - If the input is a string and convert_str_to_date flag is set to True it attempts to parse as a date or a datetime obj
    """
    ret = obj
    if isinstance(obj, dict):
        ret = {}
        for key, value in obj.items():
            ret[key] = _json_parser(value, convert_str_to_date=convert_str_to_date)

    elif isinstance(obj, list):
        ret = []
        for item in obj:
            ret.append(_json_parser(item, convert_str_to_date=convert_str_to_date))

    elif isinstance(obj, str) and convert_str_to_date:
        # Can be date/datetime string, the Undefined string or a real string
        try:
            ret = Date.fromisoformat(obj)
        except ValueError:
            try:
                ret = DateTime.fromisoformat(obj)
            except ValueError:
                pass

    if obj == Undefined.default_parse_string:
        ret = Undefined

    return ret

def is_dumps_serializable(obj):
    """
    Determines if an object can be serialized using JSON dumps.

    This function recursively checks whether the given object and all of its constituent parts
    are serializable into a JSON format. It handles basic data types, dates, custom objects
    implementing a `to_dict` method, and complex nested structures like lists and dictionaries.

    Args:
        obj (Any): The object to check for JSON serializability.

    Returns:
        bool: True if the object is serializable, False otherwise. Note that this function
              currently does not explicitly return False; it assumes all unhandled types are not serializable.

    Usage:
        This function is generally used to verify whether complex data structures can be safely
        serialized to JSON without throwing a TypeError. This is useful in scenarios where data
        integrity and correctness are crucial before performing serialization.
    """
    if isinstance(obj, (str, int, float, bool, type(None), DateTime, Date)):
        return True

    elif hasattr(obj, 'to_dict'):
        obj = obj.to_dict()
        is_dumps_serializable(obj)

        return True

    elif isinstance(obj, dict):
        for key, value in obj.items():
            is_dumps_serializable(key)  # Check if the key is serializable
            is_dumps_serializable(value)  # Check if the value is serializable
        return True

    elif isinstance(obj, (list, tuple)):
        for item in obj:
            is_dumps_serializable(item)
        return True

    elif obj is Undefined:
        return True

def dumps(obj: Any, **kwargs) -> bytes:
    """
    Serializes an object to a JSON formatted string in bytes. This function uses the `json.dumps` method for
    serialization, applying a custom default function to handle specific object types, then encodes the resulting
    JSON string into UTF-8 bytes.

    Args:
        obj (Any): The object to serialize to JSON format. This can include complex objects which are handled by the `_default` function.

    Returns:
        bytes: The JSON string serialized from the input object and encoded to UTF-8 bytes.

    Raises:
        TypeError: If the object contains types that are not directly serializable and no appropriate handling is provided in the `_default` function.

    References:
        Detailed discussion on JSON and byte encoding can be found here:
        https://bobbyhadz.com/blog/python-json-bytes-like-object-is-required-not-str
    """
    return json.dumps(obj, default=_default, **kwargs).encode('utf-8')

def loads(data: str, convert_str_to_date: bool = False) -> Any:
    """
    Deserializes a JSON document to a Python object. Optionally, it can convert string representations of dates
    back to date/datetime objects during deserialization. The function handles the deserialization process using
    `json.loads` and further processes the resulting object based on the `convert_str_to_date` flag.

    Args:
        data (str): The JSON string to deserialize.
        convert_str_to_date (bool): If True, attempts to convert date and datetime strings back to their respective date or datetime objects. This requires custom handling defined in `_json_parser`.

    Returns:
        Any: The Python object obtained from the JSON string. The type of the return depends on the content of the JSON string.

    Raises:
        JSONDecodeError: If the JSON data being deserialized is not properly formatted.

    Usage:
        Typically used when reading JSON data from a file or a network response to convert it into a usable Python object, with an option to handle date and datetime conversions.
    """
    return _json_parser(json.loads(data), convert_str_to_date=convert_str_to_date)
