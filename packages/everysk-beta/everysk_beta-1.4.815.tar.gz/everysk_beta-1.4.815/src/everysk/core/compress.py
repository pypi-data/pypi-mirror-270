###############################################################################
#
# (C) Copyright 2023 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################
import pickle
import zlib
from typing import Any
from everysk.core.serialize import dumps, loads

## Public functions
def compress_json(obj: Any) -> str:
    """
    This function first serializes the input object into a JSON string using the dumps function.
    Then it compresses the JSON string using zlib compression.
    The output is a bytes object which may contain non-printable characters due to compression

    Args:
        obj (Any):
            The JSON-serializable object to compress

    Usage:
        >>> data = {'key': 'value'}
        >>> compressed_data = compress_json(data)
        >>> print(compressed_data)
        >>> b'x\x9c\xcbH\xcd\xc9\xc9W(....)' # Example of the compressed data

    Returns:
        str: The compressed string representation of the JSON-serialized object
    """
    return zlib.compress(dumps(obj))

def decompress_json(data: str, convert_str_to_date: bool = False) -> Any:
    """
    Decompress data with zlib and transform to an obj with loads function.
    The input data should be a zlib-compressed string.
    The returned object may be any valid JSON-serializable Python object

    Args:
        data (str): the zlib-compressed string to decompress and deserialized data
        convert_str_to_date (bool): Enable conversion of str to Date and Datetime. Default is True
    Usage:
        >>> from everysk.core.compress import decompress_json
        >>> compressed_data = b'x\x9c\xabV\xcaN\xadT\xb2RP*K\xcc)MU\xaa\x05\x00+\xaf\x05A'
        >>> decompressed_data = decompress_json(compressed_data)
        >>> print(decompressed_data)
        >>> {'key': 'value'} # Example of the decompressed data'

    Returns:
        Any: The Python object reconstructed from the decompressed and deserialized
    """
    return loads(zlib.decompress(data), convert_str_to_date=convert_str_to_date)

def compress_pickle(obj: Any) -> str:
    """
    Convert obj to string with pickle dumps then uses zlib to compress it.
    The output is a bytes object which may contain non-printable characters due to compression.

    Args:
        obj (Any): The Python object to compress

    Example:
        >>> data = {'key': 'value'}
        >>> compressed_data = compress_pickle(data)
        >>> print(compressed_data)
        >>> b'x\x9c\xabV*I,.Q(...)'  # Example compressed string output

    Returns:
        str: The compressed string representation of the serialized object.
    """
    return zlib.compress(pickle.dumps(obj))

def decompress_pickle(data: str) -> Any:
    """
    Decompress data with zlib and transform to a obj with pickle loads.
    The input data should be a zlib-compressed string generated from a pickled Python object.

    Args:
        data (str): The zlib-compressed string to decompress and deserialize.

    Example:
        >>> compressed_data = b'x\x9c\xabV\xcaN\xadT\xb2RP*K\xcc)MU\xaa\x05\x00+\xaf\x05A' # Example compressed data
        >>> decompressed_data = decompress_pickle(compressed_data)
        >>> print(decompressed_data)
        >>> {'key': 'value'}  # Example decompressed object output

    Returns:
        Any:
            The Python object reconstructed from the decompressed and deserialized data.
    """
    return pickle.loads(zlib.decompress(data))
