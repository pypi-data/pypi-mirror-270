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
from typing import Any
from everysk.config import settings

from everysk.core.datetime import DateTime
from everysk.core.fields import ChoiceField, StrField, DateTimeField, ListField, _min_max_validate

from everysk.sdk.entities.tags import Tags

###############################################################################
#   Currency Field Implementation
###############################################################################
class CurrencyField(ChoiceField):
    """
    A field for currency codes with validation capabilities.

    This class extends the standard ChoiceField and adds validation for the values
    added or inserted into it.
    """
    _choices: list[str] = None

    def __init__(self, default: str = None, choices: list = None, readonly: bool = False, required: bool = False, required_lazy: bool = True, empty_is_none: bool = False, **kwargs) -> None:

        super().__init__(default=default, choices=choices, readonly=readonly, required=required, required_lazy=required_lazy, empty_is_none=empty_is_none, **kwargs)

    @property
    def choices(self) -> list[str]:
        """
        Get the available choices for the field.

        Returns:
            A list of available choices.
        """
        if not self._choices:
            self._choices = self._get_all_available_currencies()
        return self._choices

    @choices.setter
    def choices(self, value: list[str]) -> None:
        """
        Set the available choices for the field.

        Args:
            value (list[str]): The available choices.
        """
        self._choices = value

    def _get_all_available_currencies(self) -> list[str]:
        """
        Get all available currencies.

        Returns:
            A list of all available currencies.
        """
        # market_data_engine = MarketDataEngine()
        # all_available_currencies = market_data_engine.get_all_available_currencies_list()
        # all_available_currencies.append(None)
        # return all_available_currencies
        # TODO
        return [None, 'BTC', 'USD', 'CAD', 'GBP', 'EUR', 'CHF', 'HUF', 'CZK', 'DKK', 'NOK', 'ISK', 'SEK', 'ZAR', 'BRL', 'JPY', 'AUD', 'HKD', 'ILS', 'OMR', 'PLN', 'RON', 'RUB', 'IDR', 'MYR', 'KRW', 'INR', 'NZD', 'PHP', 'SGD', 'CNY', 'VND', 'TWD', 'THB', 'PEN', 'MXN', 'CLP', 'BWP', 'GHS', 'KES', 'TRY', 'COP', 'AED', 'ARS', 'CNH', 'EGP', 'FJD', 'JOD', 'SAR', 'UAH']

###############################################################################
#   Entity Name Field Implementation
###############################################################################
class EntityNameField(StrField):
    """
    This class is a subclass of StrField and provides specific validation for name, including
    size limits and pattern matching.

    Attributes:
        min_size (int): The minimum allowed size for the list (default is the value from settings).
        max_size (int): The maximum allowed size for the list (default is the value from settings).
    """
    attr_type = str

    def __init__(
        self,
        default: Any = None,
        regex: str = None,
        min_size: int = settings.ENTITY_NAME_MIN_LENGTH,
        max_size: int = settings.ENTITY_NAME_MAX_LENGTH,
        readonly: bool = False,
        required: bool = False,
        required_lazy: bool = True,
        empty_is_none: bool = True,
        **kwargs
    ) -> None:
        super().__init__(default=default, regex=regex, min_size=min_size, max_size=max_size, readonly=readonly, required=required, required_lazy=required_lazy, empty_is_none=empty_is_none, **kwargs)

###############################################################################
#   Entity Description Field Implementation
###############################################################################
class EntityDescriptionField(StrField):
    """
    This class is a subclass of StrField and provides specific validation for description, including
    size limits and pattern matching.

    Attributes:
        min_size (int): The minimum allowed size for the list (default is the value from settings).
        max_size (int): The maximum allowed size for the list (default is the value from settings).
    """
    attr_type = str

    def __init__(
        self,
        default: Any = None,
        regex: str = None,
        min_size: int = settings.ENTITY_DESCRIPTION_MIN_LEN,
        max_size: int = settings.ENTITY_DESCRIPTION_MAX_LEN,
        readonly: bool = False,
        required: bool = False,
        required_lazy: bool = False,
        empty_is_none: bool = False,
        **kwargs
    ) -> None:
        super().__init__(default=default, regex=regex, min_size=min_size, max_size=max_size, readonly=readonly, required=required, required_lazy=required_lazy, empty_is_none=empty_is_none, **kwargs)

###############################################################################
#   Entity Link UID Field Implementation
###############################################################################
class EntityLinkUIDField(StrField):
    """
    This class is a subclass of StrField and provides specific validation for link uid, including
    size limits and pattern matching.

    Attributes:
        min_size (int): The minimum allowed size for the list (default is the value from settings).
        max_size (int): The maximum allowed size for the list (default is the value from settings).
    """
    attr_type = str

    def __init__(
        self,
        default: Any = None,
        regex: str = None,
        min_size: int = settings.ENTITY_LINK_UID_MIN_LENGTH,
        max_size: int = settings.ENTITY_LINK_UID_MAX_LENGTH,
        readonly: bool = False,
        required: bool = False,
        required_lazy: bool = False,
        empty_is_none: bool = True,
        **kwargs
    ) -> None:
        super().__init__(default=default, regex=regex, min_size=min_size, max_size=max_size, readonly=readonly, required=required, required_lazy=required_lazy, empty_is_none=empty_is_none, **kwargs)

###############################################################################
#   Entity Workspace Field Implementation
###############################################################################
class EntityWorkspaceField(StrField):
    """
    This class is a subclass of StrField and provides specific validation for workspace, including
    size limits and pattern matching.

    Attributes:
        min_size (int): The minimum allowed size for the list (default is the value from settings).
        max_size (int): The maximum allowed size for the list (default is the value from settings).
    """
    attr_type = str

    def __init__(
        self,
        default: Any = None,
        regex: str = None,
        min_size: int = settings.ENTITY_WORKSPACE_MIN_LENGTH,
        max_size: int = settings.ENTITY_WORKSPACE_MAX_LENGTH,
        readonly: bool = False,
        required: bool = False,
        required_lazy: bool = True,
        empty_is_none: bool = True,
        **kwargs
    ) -> None:
        super().__init__(default=default, regex=regex, min_size=min_size, max_size=max_size, readonly=readonly, required=required, required_lazy=required_lazy, empty_is_none=empty_is_none, **kwargs)

###############################################################################
#   Entity DateTime Field Implementation
###############################################################################
class EntityDateTimeField(DateTimeField):
    """
    This class is a subclass of StrField and provides specific validation for date, including
    size limits and pattern matching.

    Attributes:
        min_size (int): The minimum allowed size for the list (default is the value from DateTime market start).
        max_size (int): The maximum allowed size for the list (default is one day delta from now).
    """
    attr_type = DateTime

    def __init__(
        self,
        default: Any = None,
        min_date: DateTime = None,
        max_date: DateTime = None,
        force_time: str = 'MIDDAY',
        required: bool = False,
        readonly: bool = False,
        required_lazy: bool = True,
        empty_is_none: bool = True,
        **kwargs
    ) -> None:
        super().__init__(default, min_date=min_date, max_date=max_date, force_time=force_time, required=required, readonly=readonly, required_lazy=required_lazy, empty_is_none=empty_is_none, **kwargs)

    def validate(self, attr_name: str, value: Any, attr_type: type = None) -> None:
        """
        Checks if value is greater than min and lower than max including both values.
        """
        min_date = self.min_date if self.min_date is not None else DateTime.market_start()
        max_date = self.max_date if self.max_date is not None else DateTime.now().delta(1, 'D').force_time('LAST_MINUTE')
        _min_max_validate(min_date, max_date, value, attr_name)
        return super().validate(attr_name, value, attr_type)

###############################################################################
#   Entity Tags Field Implementation
###############################################################################
class EntityTagsField(ListField):
    """
    This class is a subclass of ListField and provides specific validation for tags, including
    size limits and pattern matching.

    Attributes:
        min_size (int): The minimum allowed size for the list (default is the value from settings).
        max_size (int): The maximum allowed size for the list (default is the value from settings).
    """
    attr_type = Tags

    def __init__(
        self,
        default: Any = None,
        min_size: int = settings.ENTITY_MIN_TAG_SIZE,
        max_size: int = settings.ENTITY_MAX_TAG_SIZE,
        readonly: bool = False,
        required: bool = False,
        required_lazy: bool = False,
        empty_is_none: bool = False,
        **kwargs
    ) -> None:
        if default is not None and not isinstance(default, Tags):
            default = Tags(default)
        super().__init__(default=default, min_size=min_size, max_size=max_size, readonly=readonly, required=required, required_lazy=required_lazy, empty_is_none=empty_is_none, **kwargs)

    def clean_value(self, value: Any) -> Any:
        """
        This method ensures that the provided value is in the expected format before assigning it to an attribute.
        If the value is None, it is replaced with an empty TagsList. If it is not already a TagsList instance,
        it is converted into one.
        """
        value = super().clean_value(value)
        if value is None:
            value = Tags()
        elif not isinstance(value, Tags):
            value = Tags(value)
        return value
