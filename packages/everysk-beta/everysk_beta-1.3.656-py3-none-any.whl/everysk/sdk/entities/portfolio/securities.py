# -*- coding: utf_8 -*-
###############################################################################
#
# (C) Copyright 2023 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################

###############################################################################
#   Imports
###############################################################################
from typing import Self, Any

from everysk.core.exceptions import HttpError, SDKError, FieldValueError
from everysk.core.http import HttpSDKPOSTConnection

from everysk.sdk.entities.base_list import EntityList
from everysk.sdk.entities.portfolio.security import Security

###############################################################################
#   Securities Implementation
###############################################################################
class Securities(EntityList):

    _attr_type: Security = Security

    def _validate(self, value: dict) -> Security:
        """
        Validates a dictionary value and converts it into a `Security` object.

        Args:
            value (dict): A dictionary representing the security data.

        Returns:
            Security: A `Security` object created from the provided dictionary.

        Raises:
            FieldValueError: If the provided value is not a valid dictionary.
            TypeError: If the provided value is not of dictionary type.

        Example usage:
            >>> from my_module import Security
            >>> security_data = {'symbol': 'AAPL', 'name': 'Apple Inc.', 'price': 150.0}
            >>> validated_security = self._validate(security_data)
            >>> isinstance(validated_security, Security)
            True
        """
        if not isinstance(value, dict):
            raise FieldValueError("Security: The value must be a dict.") from TypeError
        return self._attr_type(**value)

    def validate(self) -> bool:
        """
        Validates the required fields of each security in the collection.

        This method iterates through the collection of securities and calls the
        `validate_required_fields` method for each security to ensure that all
        required fields are present and have valid values.

        Returns:
            bool: True if validation succeeds for all securities, otherwise False.

        Example usage:
            >>> from everysk.sdk.entities.portfolio.securities import Securities
            >>> security_data = [{'symbol': 'AAPL', 'name': 'Apple Inc.', 'price': 150.0},
            ...                  {'symbol': 'GOOGL', 'name': 'Alphabet Inc.', 'price': 2800.0}]
            >>> security_collection = Securities(security_data)
            >>> security_collection.validate()
            True
        """
        for security in self:
            security.validate_required_fields()
        return True

    @staticmethod
    def from_lists(security_list: list[list[Any]]) -> Self:
        """
        Create a Securities collection from a list of lists representing securities.

        This static method takes a list of lists where each inner list represents a security.
        The first inner list (header) is used to extract attribute names, and the subsequent
        lists are used to create individual `Security` objects within a `Securities` collection.

        Args:
            security_list (list[list[Any]]): A list of lists where each inner list represents a security.

        Returns:
            Self: A `Securities` collection containing `Security` objects created from the provided data.

        Example usage:
            >>> from everysk.sdk.entities.portfolio.securities import Securities
            >>> security_data = [
            ...     ['symbol', 'name', 'price'],
            ...     ['AAPL', 'Apple Inc.', 150.0],
            ...     ['GOOGL', 'Alphabet Inc.', 2800.0]
            ... ]
            >>> securities_collection = Securities.from_lists(security_data)
            >>> len(securities_collection)
            2
        """
        header: list[str] = security_list.pop(0)
        return Securities([
            Securities._attr_type.from_list(sec_as_list, header)
            for sec_as_list in security_list
        ])

    @staticmethod
    def diff(securities_a: list[dict], securities_b: list[dict], accessor: str = 'comparable') -> dict:
        """
        Diff two securities list. The securities list are compared by the
        accessor provided. The accessor is used to compare the securities
        list. The accessor must be a key in the securities list.

        Args:
            securities_a (Securities): Securities list to compare.
            securities_b (Securities): Securities list to compare.
            accessor (str): Accessor to compare.

        Returns:
            dict: Diff result.
                Keys:
                    added_positions (Securities): Added positions.
                    removed_positions (Securities): Removed positions.
                    partial_positions (Securities): Partial positions.
                    equal_positions (Securities): Equal positions.
        """
        try:
            response: dict = HttpSDKPOSTConnection(
                cls_name='Securities',
                params={
                    'securities_a': securities_a,
                    'securities_b': securities_b,
                    'accessor': accessor
                }
            ).get_response()
        except HttpError as error:
            raise SDKError(error.msg) from error

        return response

    def to_dict(self, with_internals: bool = True) -> list[dict]:
        """
        Convert the Securities collection to a list of dictionaries.

        This method converts each `Security` object in the collection to a dictionary representation.

        Args:
            with_internals (bool, optional): Indicates whether to include internal attributes in the dictionaries.
                Defaults to True.

        Returns:
            list[dict]: A list of dictionaries representing the securities in the collection.

        Example usage:
            >>> from everysk.sdk.entities.portfolio.securities import Securities
            >>> security_data = [{'symbol': 'AAPL', 'name': 'Apple Inc.', 'price': 150.0},
            ...                  {'symbol': 'GOOGL', 'name': 'Alphabet Inc.', 'price': 2800.0}]
            >>> securities_collection = Securities(security_data)
            >>> securities_dict = securities_collection.to_dict()
            >>> len(securities_dict)
            2
        """
        return [security.to_dict(with_internals=with_internals) for security in self]

    def consolidate(self, consolidation_keys) -> Self:
        """
        Consolidate securities list. If no consolidation keys are provided,
        the securities list is returned as is. Otherwise, the securities list
        is consolidated by the provided keys.

        Args:
            consolidation_keys (List[str]): List of keys to consolidate
            by (e.g. ['symbol', 'instrument_class']). If no keys are provided,
            the securities list is returned as is.

        Returns:
            Securities: Consolidated securities list.
        """
        try:
            response: dict = HttpSDKPOSTConnection(
                cls_name='Securities', params={'consolidation_keys': consolidation_keys}
            ).get_response()
        except HttpError as error:
            raise SDKError(error.msg) from error

        return type(self)(**response)

    def remove_errors(self) -> Self:
        """
        Create a new Securities collection with securities having a status other than 'ERROR'.

        This method filters the current Securities collection, creating a new collection that
        includes only securities with a status attribute other than 'ERROR'.

        Returns:
            Self: A new Securities collection containing securities without the 'ERROR' status.

        Example usage:
            >>> from everysk.sdk.entities.portfolio.securities import Securities
            >>> security_data = [{'symbol': 'AAPL', 'status': 'OK'},
            ...                  {'symbol': 'GOOGL', 'status': 'ERROR'},
            ...                  {'symbol': 'MSFT', 'status': 'OK'}]
            >>> securities_collection = Securities(security_data)
            >>> filtered_securities = securities_collection.remove_errors()
            >>> len(filtered_securities)
            2
        """
        return Securities([security for security in self if security.status != 'ERROR'])

    def to_lists(self, header: list[str] = None) -> list[list[Any]]:
        """
        Convert the Securities collection to a list of lists.

        This method converts each `Security` object in the collection to a list representation.

        Args:
            header (list[str], optional): A list of strings representing the header row. If not provided,
                the method will create a header based on the keys of the first security in the collection.

        Returns:
            list[list[Any]]: A list of lists representing the securities in the collection, including the header.

        Example usage:
            >>> from everysk.sdk.entities.portfolio.securities import Securities
            >>> security_data = [{'symbol': 'AAPL', 'name': 'Apple Inc.', 'price': 150.0},
            ...                  {'symbol': 'GOOGL', 'name': 'Alphabet Inc.', 'price': 2800.0}]
            >>> securities_collection = Securities(securities=security_data)
            >>> securities_list = securities_collection.to_lists()
            >>> len(securities_list)
            3  # Including the header row
        """
        if header is None:
            first_security: Security = self[0]
            extra_data: dict = first_security.get('extra_data') or {}
            header = list(first_security.keys()) + list(extra_data.keys())
            header = self._attr_type.sort_header(header)

        security_list: list[list[Any]] = [security.to_list(header=header) for security in self]
        security_list.insert(0, header)

        return security_list
