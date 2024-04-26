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
from typing import Any, TYPE_CHECKING

import csv
import six

from everysk.config import settings

from everysk.core.string import to_string
from everysk.core.fields import ListField, StrField, FloatField, BoolField

from everysk.sdk.entities.base import BaseEntity, ScriptMetaClass
from everysk.sdk.entities.script import Script
from everysk.sdk.entities.fields import EntityNameField, EntityDescriptionField, EntityLinkUIDField, EntityWorkspaceField, EntityDateTimeField, EntityTagsField, CurrencyField
from everysk.sdk.entities.portfolio.securities import Securities

if TYPE_CHECKING:
    from io import StringIO

###############################################################################
#   Securities Field Implementation
###############################################################################
class SecuritiesField(ListField):
    attr_type = Securities

    def __init__(self, default: Any = None, required_lazy: bool = True, **kwargs) -> None:
        """
        This method initializes the field.

        Args:
            default (Any): The default value of the field.
            required_lazy (bool): True if the field is required, False otherwise.
            **kwargs (dict): The keyword arguments of the field.
        """
        super().__init__(default=default, required_lazy=required_lazy, **kwargs)

    def clean_value(self, value: Any) -> Securities:
        """
        This method cleans the value of the field.

        Args:s
            value (Any): The value to be cleaned.

        Returns:
            Securities: The cleaned value.
        """
        if isinstance(value, list):
            value = self.attr_type(value)
        return super().clean_value(value)

###############################################################################
#   Portfolio Implementation
###############################################################################
class Portfolio(BaseEntity, metaclass=ScriptMetaClass):
    """
    This class represents a portfolio entity object and provides methods to validate
    and convert the entity object to a dictionary or a CSV string representation.

    Attributes:
        script (Script): The script object associated to the entity.
        id (StrField): The unique identifier of the portfolio.
        workspace (EntityWorkspaceField): The workspace of the portfolio.
        name (EntityNameField): The name of the portfolio.
        tags (EntityTagsField): The tags of the portfolio.
        link_uid (EntityLinkUIDField): The link uid of the portfolio.
        description (EntityDescriptionField): The description of the portfolio.
        nlv (FloatField): The nlv of the portfolio.
        base_currency (CurrencyField): The base currency of the portfolio.
        date (EntityDateTimeField): The date of the portfolio.
        securities (SecuritiesField): The securities of the portfolio.
        level (StrField): The level of the portfolio.

        version (StrField): The version of the portfolio.
        created_on (DateTimeField): The created on date of the portfolio.
        updated_on (DateTimeField): The updated on date of the portfolio.

    Example usage:
        >>> from everysk.sdk.entities.portfolio.base import Portfolio
        >>> portfolio = Portfolio()
        >>> portfolio.workspace = 'my_workspace'
        >>> portfolio.name = 'My Portfolio'
        >>> portfolio.tags = ['tag1', 'tag2']
        >>> portfolio.nlv = 1000.0
        >>> portfolio.base_currency = 'USD'
        >>> portfolio.date = '20210101'
        >>> portfolio.securities = ['sec1', 'sec2', 'sec3']
        >>> portfolio.save()
        >>> portfolio.to_dict()
        {
            'id': 'port_12345678',
            'workspace': 'my_workspace',
            'name': 'My Portfolio',
            'tags': ['tag1', 'tag2'],
            'nlv': 1000.0,
            'base_currency': 'USD',
            'date': '20210101',
            'securities': ['sec1', 'sec2', 'sec3'],
            'version': 'v1',
            'created_on': '2021-01-01T00:00:00.000000Z',
            'updated_on': '2021-01-01T00:00:00.000000Z',
            'level': 'portfolio'
        }

    """
    script: Script
    _orderable_attributes = ListField(default=['date', 'created_on', 'updated_on', 'name']) # TODO changed to ReadonlyListField

    id = StrField(regex=settings.PORTFOLIO_ID_REGEX, max_size=settings.PORTFOLIO_ID_MAX_SIZE, required_lazy=True, empty_is_none=True)

    name = EntityNameField()
    description = EntityDescriptionField()
    tags = EntityTagsField()
    link_uid = EntityLinkUIDField()
    workspace = EntityWorkspaceField()

    nlv = FloatField(min_size=0.0, max_size=float('inf'))
    base_currency = CurrencyField()
    date = EntityDateTimeField()
    securities = SecuritiesField(min_size=0, max_size=settings.PORTFOLIO_MAX_SIZE, required_lazy=True)
    level = StrField(min_size=1, max_size=settings.PORTFOLIO_LEVEL_MAX_LENGTH)

    check_securities = BoolField(default=False)

    ###############################################################################
    #   Portfolio Basics Implementation
    ###############################################################################

    @staticmethod
    def get_id_prefix() -> str:
        """
        Returns the prefix of the portfolio id field value.

        Returns:
            str: The prefix of the portfolio id field value.

        Example usage:
            >>> Portfolio.get_id_prefix()
            'port_'
        """
        return settings.PORTFOLIO_ID_PREFIX

    def validate(self) -> bool:
        """
        This method validates the entity object and raises an exception if it is not
        valid. The validation is performed by calling the `validate` method of each field
        of the entity.

        Args:
            self (Self): The entity object to be validated.

        Raises:
            FieldValueError: If the entity object is not valid.
            RequiredFieldError: If a required field is missing.

        Returns:
            bool: True if the entity object is valid, False otherwise.

        Example usage:
            >>> entity = Entity()
            >>> entity.validate()
            True
        """
        return self.get_response(self_obj=self)

    def to_csv(self) -> str:
        """
        This method converts the entity object into a CSV string representation of the
        entity object.

        Returns:
            str: A CSV string representation of the entity.

        Example usage:
            >>> entity = Entity()
            >>> entity.to_csv()
            "name,date,base_currency,nlv,description,tags,securities
            My Portfolio,2021-01-01,USD,1000.0,My Portfolio Description,tag1 tag2,sec1,sec2,sec3"
        """
        def write_row(csv_writer_: Any, line: list[str], length: int) -> None:
            out: list[str] = line + ([''] * (length - len(line)))
            out = [to_string(s) if s is not None else None for s in out]
            csv_writer_.writerow(out)
            return None

        csv_file: StringIO = six.StringIO()
        csv_writer: Any = csv.writer(csv_file)

        date_: str = self.date.strftime()
        nlv_: str = '' if not self.nlv else to_string(self.nlv)
        pre_headers: list[str] = [self.name, date_, self.base_currency, nlv_, self.description, ' '.join(self.tags)]

        securities_as_lists: list[list[str]] = self.securities.to_lists()

        headers: list[str] = securities_as_lists[0]
        headers_len: int = len(headers)
        write_row(csv_writer, pre_headers, headers_len)
        write_row(csv_writer, headers, headers_len)

        for sec_as_list in securities_as_lists[1:]:
            write_row(csv_writer, sec_as_list, headers_len)

        out: str = csv_file.getvalue()
        csv_file.close()
        return out
