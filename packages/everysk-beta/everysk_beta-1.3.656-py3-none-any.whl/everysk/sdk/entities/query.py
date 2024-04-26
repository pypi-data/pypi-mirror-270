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
from typing import Any, Self, Generator, TypedDict, Callable

from everysk.core.fields import StrField, IntField, ListField, BoolField
from everysk.core.datetime import DateTime
from everysk.core.string import is_string_object, normalize_string_to_search

from everysk.sdk.base import BaseSDK

###############################################################################
#   Query Page Implementation
###############################################################################
class QueryPage(TypedDict):
    """
    A dictionary containing the paginated list of entities and a next page token.

    Attributes:
        entities (list[Any]): The list of entities for the current page.
        next_page_token (str): The token representing the next page of results.
    """
    entities: list[Any] = None
    next_page_token: str = None

###############################################################################
#   Query Implementation
###############################################################################
class Query(BaseSDK):
    """
    This class allows you to build a query to retrieve entities from the data source
    based on certain conditions. The query can be executed to retrieve a single entity,
    a list of entities, or a paginated list of entities.

    Attributes:
        _klass (Any): The class of the entity to be queried.
        _clean_order (set): The set of properties by which to sort the query.
        _find_or_fail (bool): A boolean value indicating whether the query should return an error if no entity is found.
        filters (list): The list of filter conditions for the query.
        order (list): The list of properties by which to sort the query.
        projection (list): The list of properties to include or exclude in the query result.
        distinct_on (list): The list of properties for which the resulting entities should be distinct.
        limit (int): The maximum number of entities to retrieve.
        offset (int): The number of initial entities to skip before starting retrieval.
        page_size (int): The number of entities to retrieve per page.
        page_token (str): The token representing the desired page of results.

    Example usage:
        To create a query to retrieve a single entity:
        entity = Query(MyEntity).where('property_name', 'value').load()

        To create a query to retrieve a list of entities:
        entities = Query(MyEntity).where('property_name', 'value').loads()

        To create a query to retrieve a paginated list of entities:
        entities_page = Query(MyEntity).where('property_name', 'value').page()
    """

    _klass: Callable = None
    _clean_order: set = None
    _find_or_fail = BoolField(default=False)

    # QUERY PARAMETERS
    filters = ListField()
    order = ListField()
    projection = ListField()

    # LOAD / LOADS PARAMETERS
    limit = IntField()
    offset = IntField()

    # PAGE / PAGES PARAMETERS
    page_size = IntField()
    page_token = StrField()

    def __init__(self, _klass: Callable, filters: list | None = None, order: list | None = None, projection: list | None = None, distinct_on: list | None = None,
                 limit: int | None = None, offset: int | None = None, page_size: int | None = None, page_token: str | None = None):

        super().__init__(_klass=_klass, _clean_order=None, filters=None, order=None, projection=None, distinct_on=None, limit=None,
                         offset=None, page_size=None, page_token=None)

        self._klass = _klass
        self._clean_order = set()

        order = [] if order is None else order
        self.order = []
        for property_name in order:
            self.sort_by(property_name)

        filters = [] if filters is None else filters
        self.filters = []
        for filter_set in filters:
            self.where(*filter_set)

        if projection is not None:
            self.set_projection(projection)

        distinct_on = [] if distinct_on is None else distinct_on
        self.set_distinct_on(distinct_on)

        if limit is not None:
            self.set_limit(limit)

        if offset is not None:
            self.set_offset(offset)

        if page_size is not None:
            self.set_page_size(page_size)

        if page_token is not None:
            self.set_page_token(page_token)

    def where(self, *args) -> Self:
        """
        Adds a filter condition to the query.

        Args:
            *args: Variable number of arguments. Expected formats are:
                - (property_name, value)
                - (property_name, operator, value)

        Returns:
            self: The Query object with the added filter condition.

        Raises:
            ValueError: If the number of arguments is not 2 or 3, indicating an incorrect format.
            ValueError: If the operator is not '=' and property_name is not one of ('date', 'created_on', 'updated_on').

        Example usage:
            To create a query with a filter condition:
            query = Query(MyEntity).where('property_name', 'value')

            To create a query with a filter condition using an operator:
            query = Query(MyEntity).where('property_name', '>', 'value')
        """
        property_name: str = args[0]
        operator: str | None = None
        value: str | None = None

        if len(args) == 2:
            operator = '='
            value = args[1]
        elif len(args) == 3:
            operator = args[1]
            value = args[2]
        else:
            raise ValueError('Query \'where\' function expects 2 or 3 arguments')

        # Validate the operator for certain properties
        if operator != '=' and property_name not in ('date', 'created_on', 'updated_on'):
            raise ValueError(f'Filter by {property_name} operator must be \'=\'')

        # Handle special case for 'tags' property
        if property_name == 'tags':
            self.filters.extend([('tags', '=', tag.lower().strip()) for tag in value])

            return self

        # Handle special case for 'date' property
        if property_name == 'date':
            if is_string_object(value):
                value = DateTime.fromisoformat(value).replace(hour=12)

            self.filters.append((property_name, operator, value))

            return self

        # Handle special case for 'name' property
        if property_name == 'name':
            value = normalize_string_to_search(value)

            limit: str = f'{value[:-1]}{chr(ord(value[-1]) + 1)}'
            self.filters.append((property_name, '<', limit))
            self.filters.append((property_name, '>=', value))

            return self

        # Regular filter condition
        self.filters.append((property_name, operator, value))

        return self

    def sort_by(self, property_name: str) -> Self:
        """
        Add a property by which to sort the query and return the instance.
        This method updates the query's order based on the provided property_name.

        Parameters:
            - property_name (str): The name of the property to sort by. It can optionally
            contain hyphens, which will be removed.

        Returns:
            - Query: The instance of the current object.

        Raises:
            - ValueError: If the provided property_name is not sortable or if the
            property_name is duplicated in the current order.

        Example usage:
            To create a query with a sort condition:
            >>> query = Query(MyEntity).sort_by('property_name')

        """
        clean_name: str = property_name.replace('-', '')

        if clean_name not in self._klass._orderable_attributes: # pylint: disable=protected-access
            raise ValueError(f'{clean_name} is not sortable')

        if clean_name in self._clean_order:
            raise ValueError(f'Duplicated order property: {clean_name} in {self.order}')

        self.order.append(property_name)
        self._clean_order.add(clean_name)

        return self

    def set_projection(self, projection: list | str) -> Self:
        """
        Set the projection attributes for the query and return the instance.

        This method sets the desired properties that should be returned in the query result.
        The properties can either be set to include (using the property name) or to exclude
        (prefixing the property name with '-'). Both inclusion and exclusion should not be set
        in the same query.

        Parameters:
            - projection (Union[List, str]): A property name as a string or a list of property names
            indicating which properties to include or exclude in the query result.

        Returns:
            - Query: The instance of the current object.

        Raises:
            - ValueError: If both projection and inverse projection are set in the same query or
            if the projection properties do not belong to the entity kind.

        Example usage:
            To create a query with a projection condition:
            >>> query = Query(MyEntity).set_projection('property_name')

            To create a query with an inverse projection condition:
            >>> query = Query(MyEntity).set_projection('-property_name')

            To create a query with a projection condition using a list:
            >>> query = Query(MyEntity).set_projection(['property_name_1', 'property_name_2'])
        """

        if is_string_object(projection):
            projection = [projection]

        count: int = sum(property_name.startswith('-') for property_name in projection)
        if not (count == 0 or count == len(projection)):
            raise ValueError('Projection and Inverse Projection should not be set in the same query')

        entity_properties: set = set(self._klass().keys()) # pylint: disable=protected-access
        projection_properties: set = set([property_name.replace('-', '') for property_name in projection])
        difference: set = projection_properties.difference(entity_properties)

        if difference:
            difference_: str = ', '.join(difference)
            raise ValueError(f'Projection properties does not belongs to {self._klass.__name__}: {difference_}')

        self.projection = projection

        return self

    def set_distinct_on(self, distinct_on: list | str) -> Self:
        """
        Set the attributes for which the query results should be distinct.

        This method allows you to specify properties such that the resulting entities
        of the query are distinct with respect to these properties.

        Parameters:
            - distinct_on (Union[List, str]): A property name as a string or a list of property names
            for which the resulting entities should be distinct.

        Returns:
            - Query: The instance of the current object, allowing for method chaining.

        Example usage:
            To create a query with a distinct condition:
            >>> query = Query(MyEntity).set_distinct_on('property_name')

            To create a query with a distinct condition using a list:
            >>> query = Query(MyEntity).set_distinct_on(['property_name_1', 'property_name_2'])
        """

        if is_string_object(distinct_on):
            distinct_on = [distinct_on]

        self.distinct_on = distinct_on
        return self

    def set_limit(self, limit: int) -> Self:
        """
        Set the maximum number of results the query should return.

        This method defines the maximum number of entities to retrieve from the database
        when the query is executed.

        Parameters:
            - limit (int): The maximum number of results to retrieve.

        Returns:
            - Query: The instance of the current object, allowing for method chaining.

        Example usage:
            To create a query with a limit condition:
            >>> query = Query(MyEntity).set_limit(10)
        """
        self.limit = limit
        return self

    def set_offset(self, offset: int) -> Self:
        """
        Set the starting point from which to retrieve the results in the query.

        This method specifies the number of initial results to skip before starting to
        retrieve entities when the query is executed.

        Parameters:
            - offset (int): The number of results to skip before retrieval begins.

        Returns:
            - Query: The instance of the current object, allowing for method chaining.

        Example usage:
            To create a query with an offset condition:
            >>> query = Query(MyEntity).set_offset(10)
        """
        self.offset = offset
        return self

    def set_page_size(self, page_size: int) -> Self:
        """
        Set the number of results to be returned per page for the query.

        This method determines how many entities are retrieved at once in a paginated
        manner when the query is executed.

        Parameters:
            - page_size (int): The number of results to retrieve per page.

        Returns:
            - Query: The instance of the current object, allowing for method chaining.

        Example usage:
            To create a query with a page size condition:
            >>> query = Query(MyEntity).set_page_size(10)
        """
        self.page_size = page_size
        return self

    def set_page_token(self, page_token: str) -> Self:
        """
        Set the token representing a specific page of results in the query.

        This method determines the starting point for retrieving entities based on the
        provided page token when the query is executed.

        Parameters:
            - page_token (str): The token representing the desired page of results.

        Returns:
            - Query: The instance of the current object, allowing for method chaining.

        Example usage:
            To create a query with a page token condition:
            >>> query = Query(MyEntity).set_page_token('page_token')
        """
        self.page_token = page_token
        return self

    def set_find_or_fail(self, find_or_fail: bool) -> Self:
        """
        Set the find_or_fail attribute for the query and return the instance.

        This method sets the desired find_or_fail attribute that should be returned in the query result.

        Parameters:
            - find_or_fail (bool): A boolean value indicating whether the query should return an error if no entity is found.

        Returns:
            - Query: The instance of the current object.

        Example usage:
            To create a query with a find_or_fail condition:
            >>> query = Query(MyEntity).set_find_or_fail(True)
        """
        self._find_or_fail = find_or_fail
        return self

    def load(self, offset: int = Undefined) -> Any:
        """
        Fetch a single entity based on the query with an optional offset.

        This method retrieves a single entity from the data source based on the conditions
        specified in the query. An optional offset can be provided to skip a certain number
        of results before fetching the desired entity.

        Parameters:
            - offset (int, optional): The number of results to skip before fetching the entity.
            Defaults to None, meaning no results are skipped.

        Returns:
            - Any: An instance of the entity, or None if no entity matches the query.

        Example usage:
            To create a query with a load condition:
            >>> entity = Query(MyEntity).where('property_name', 'value').load()
        """
        entity: Any | None = self.get_response(self_obj=self, params={'offset': offset})

        if entity is not None:
            entity = self._klass(**entity)

        return entity

    def loads(self, limit: int = Undefined, offset: int = Undefined) -> list[Any]:
        """
        Fetch a list of entities based on the query with optional limit and offset.

        This method retrieves multiple entities from the data source based on the conditions
        specified in the query. Optional limit and offset parameters can be provided to control
        the number of returned entities and the starting point, respectively.

        Parameters:
            - limit (int, optional): The maximum number of entities to retrieve. Defaults to None,
            meaning there's no specific limit.
            - offset (int, optional): The number of initial entities to skip before starting retrieval.
            Defaults to None, meaning no entities are skipped.

        Returns:
            - List[Any]: A list of instances of the entity. Returns an empty list if no entities match
            the query.

        Example usage:
            To create a query with a loads condition:
            >>> entities = Query(MyEntity).where('property_name', 'value').loads()
        """
        entities: list[dict] = self.get_response(self_obj=self, params={'limit': limit, 'offset': offset})

        entities: list[Any] = [self._klass(**entity) for entity in entities]

        return entities

    def page(self, page_size: int = Undefined, page_token: str = Undefined) -> QueryPage:
        """
        Fetch a paginated list of entities based on the query.

        This method retrieves a paginated set of entities from the data source based on the conditions
        specified in the query. A specific page size and an optional page token can be provided to
        control pagination.

        Parameters:
            - page_size (int, optional): The number of entities to retrieve per page. Defaults to 20.
            - page_token (str, optional): The token representing the desired page of results. Defaults to None,
            meaning the first page is retrieved.

        Returns:
            - Any: A dictionary containing the paginated list of entities and potentially other metadata
            related to pagination.

        Example usage:
            To create a query with a page condition:
            >>> entities_page = Query(MyEntity).where('property_name', 'value').page()
        """
        response: QueryPage = self.get_response(self_obj=self, params={'page_size': page_size, 'page_token': page_token})

        response['entities'] = [self._klass(**entity) for entity in response['entities']]

        return response

    def pages(self, page_size: int = Undefined) -> Generator[list[Any | None], None, None]:
        """
        Fetch paginated lists of entities based on the query.

        This method retrieves multiple pages of entities from the data source based on the conditions
        specified in the query. Each page will contain up to `page_size` entities. This function yields
        each page of entities as they are retrieved.

        Parameters:
        - page_size (int, optional): The number of entities to retrieve per page. Defaults to 20.

        Yields:
        - List[Any]: A list of entities for the current page.

        Note:
        This generator function will continue to fetch and yield pages until no more pages are available.

        Example usage:
        To create a query with a pages condition:
            >>> for entities in Query(MyEntity).where('property_name', 'value').pages():
            ...     print(entities)
        """
        next_page_token: Undefined | str = Undefined

        while True:
            result: QueryPage = self.page(page_size=page_size, page_token=next_page_token)
            yield result['entities']

            if not result['next_page_token']:
                break

            next_page_token = result['next_page_token']
