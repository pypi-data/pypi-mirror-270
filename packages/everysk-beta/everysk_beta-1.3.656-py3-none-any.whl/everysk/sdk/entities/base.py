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

from everysk.config import settings
from everysk.core.fields import StrField, DateTimeField, ListField
from everysk.core.datetime import DateTime, Date
from everysk.core.object import MetaClass as ObjMetaClass

from everysk.sdk.base import BaseSDK
from everysk.sdk.engines.cryptography import generate_random_id
from everysk.sdk.entities.query import Query
from everysk.sdk.entities.script import Script

###############################################################################
#   Query MetaClass Implementation
###############################################################################
class QueryMetaClass(ObjMetaClass):
    """
    Metaclass for the Query class that allows for the query attribute to be accessed
    directly from the entity class.

    Example usage:
        To access the query attribute from the entity class:
        >>> MyClass.query
        Query()
    """
    def __getattribute__(cls, __name: str) -> Any:
        """
        Get the query attribute from the entity class.
        """
        if __name == 'query':
            return Query(cls)
        return super().__getattribute__(__name)

###############################################################################
#   Script MetaClass Implementation
###############################################################################
class ScriptMetaClass(QueryMetaClass):
    """
    Metaclass for the Script class that allows for the script attribute to be accessed
    directly from the entity class.

    Example usage:
        To access the script attribute from the entity class:
        >>> MyClass.script
        Script()
    """
    def __getattribute__(cls, __name: str) -> Any:
        """
        Get the script attribute from the entity class.
        """
        if __name == 'script':
            return Script(cls)
        return super().__getattribute__(__name)

###############################################################################
#   Base Entity Implementation
###############################################################################
class BaseEntity(BaseSDK, metaclass=QueryMetaClass):
    """
    Base class for all entities in the SDK library that provides common functionality. This class
    should not be instantiated directly, but rather should be subclassed by other entity classes.

    Attributes:
        id (str): The unique identifier of the entity.
        version (str): The version of the entity.
        created_on (DateTime): The date and time the entity was created.
        updated_on (DateTime): The date and time the entity was last updated.

    Example usage:
        To create a new entity:
        >>> my_entity = MyEntity(id="my_id", workspace="my_workspace", name="my_name", description="my_description")
    """
    _orderable_attributes = ListField(default=['id', 'created_on', 'updated_on'])

    query: Query = None

    created_on = DateTimeField(empty_is_none=True, required_lazy=True)
    updated_on = DateTimeField(empty_is_none=True, required_lazy=True)

    version = StrField(default=settings.ENTITY_DEFAULT_VERSION, required_lazy=True)

    @staticmethod
    def get_id_prefix() -> str:
        """
        Get the prefix for the unique identifier for this entity.

        Returns:
            str: The prefix for the unique identifier.

        Raises:
            NotImplementedError: This method should be overridden in subclasses.
        """
        raise NotImplementedError()

    @classmethod
    def generate_id(cls) -> str:
        """
        Generate a unique ID for an entity instance.

        Returns:
            str: The generated unique ID.

        Example usage:
            To generate a unique ID for an entity instance:
            >>> unique_id = MyEntity.generate_id()
        """
        prefix: str = cls.get_id_prefix()
        unique_id: str = generate_random_id(length=settings.ENTITY_ID_LENGTH)
        return f'{prefix}{unique_id}'

    @classmethod
    def validate_id(cls, entity_id: str) -> bool:
        """
        Validate an entity's ID.

        Args:
            entity_id str: The ID to be validated.

        Returns:
            bool: True if the ID is valid, False otherwise.

        Example usage:
            To validate an entity's ID:
            >>> is_valid = MyEntity.validate_id(my_id)
        """
        if entity_id:
            try:
                cls(id=entity_id)
                return True
            except Exception: # pylint: disable=broad-exception-caught
                pass
        return False

    def validate(self) -> bool:
        """
        Validate the entity's attributes.

        This method performs validation checks on the entity's attributes to ensure they meet
        the required criteria. If all required fields are present, the validation is considered
        successful and the method returns True. If any required field is missing, it raises a
        RequiredFieldError exception.

        Args:
            self (Self): The entity instance to validate.

        Returns:
            bool: True if the validation is successful.

        Raises:
            RequiredFieldError: If any required field is missing.

        Example usage:
            To validate an entity:

            >>> is_valid = my_entity.validate()
            >>> if is_valid:
            >>>     # Handle the valid entity
            >>> else:
            >>>     # Handle the invalid entity
        """
        self.validate_required_fields()
        return True

    @classmethod
    def check(cls, entity_dict: dict) -> Self:
        """
        Check the entity properties.

        Args:
            entity_dict (dict): The entity properties.

        Returns:
            BaseEntity: The entity object.

        Raises:
            FieldValueError: If the entity properties are invalid.
            RequiredFieldError: If a required field is missing.
        """
        entity: Self = cls(**entity_dict)
        entity.validate()
        return entity

    def to_dict(self, with_internals: bool = True) -> dict:
        """
        Convert the entity to a JSON-serializable dictionary.

        This method converts the entity object into a dictionary that can be easily
        serialized to JSON.

        Args:
            self (Self): The entity instance to convert.
            with_internals (bool, optional): Whether to include internal parameters. Defaults to True.

        Returns:
            dict: A dictionary representation of the entity.

        Raises:
            NotImplementedError: This method should be implemented in subclasses.
        """
        dct: dict = super().to_dict(with_internals=with_internals)

        if 'date' in self:
            dct['date'] = Date.strftime_or_null(self.date) # pylint: disable=no-member
            dct['date_time'] = DateTime.strftime_or_null(self.date) # pylint: disable=no-member

        if 'created_on' in self:
            dct.pop('created_on')
            dct['created'] = self.created_on.timestamp() if self.created_on is not None else None

        if 'updated_on' in self:
            dct.pop('updated_on')
            dct['updated'] = self.updated_on.timestamp() if self.updated_on is not None else None

        if 'tags' in self:
            dct['tags'] = list(dct['tags']) if dct['tags'] is not None else None

        return dct

    def _entity_to_query(self) -> Query:
        """
        This method converts the entity object into a query object.

        Returns:
            Query: A query object.

        Example usage:
            >>> entity = Entity()
            >>> query = entity._entity_to_query()
            >>> query
            Query()
        """
        query: Query = type(self).query

        if self.workspace is not None:
            query = query.where('workspace', self.workspace)
        if self.link_uid is not None:
            query = query.where('link_uid', self.link_uid)
        if self.name is not None:
            query = query.where('name', self.name)
        if self.date is not None:
            query = query.where('date', self.date)
        if self.tags:
            query = query.where('tags', self.tags)

        return query

    @classmethod
    def retrieve(cls, entity_id: str) -> Self | None:
        """
        Retrieve an entity by its ID.

        Args:
            entity_id (str): The unique identifier of the entity to retrieve.

        Returns:
            Self: An instance of the class representing the retrieved entity.
            None: If not found

        Example usage:
            To retrieve an entity by its ID:

            >>> entity = MyClass.retrieve("entity_id_here")
            >>> if entity:
            >>>    # Handle the retrieved entity
            >>> else:
            >>>    # Entity not found
        """
        entity_dict: dict | None = cls.get_response(params={'entity_id': entity_id})

        if entity_dict is None:
            return None

        return cls(**entity_dict)

    @classmethod
    def create(cls, entity_dict: dict) -> Self:
        """
        Create a new entity using provided attributes from a dictionary.

        Args:
            entity_dict (dict): A dictionary representing the entity's attributes.

        Returns:
            Self: An instance of the class representing the newly created entity.

        Example usage:
            To create a new entity with attributes from a dictionary and optional keyword arguments:

            >>> entity_data = {'property1': value1, 'property2': value2}
            >>> new_entity = MyClass.create(entity_data)
        """
        entity_dict_: dict = cls.get_response(params={'entity_dict': entity_dict})

        return cls(**entity_dict_)

    @classmethod
    def modify(cls, entity_id: str, overwrites: dict) -> Self | None:
        """
        Modify an existing entity by updating its attributes using the provided overwrites.

        Args:
            entity_id (str): The unique identifier of the entity to modify.
            overwrites (dict): A dictionary containing attribute updates to apply to the entity.

        Returns:
            Self: An instance of the class representing the modified entity.
            None: If not found

        Example usage:
            To modify an existing entity by updating its attributes with overwrites:

            >>> entity_id_to_modify = "entity_id_here"
            >>> attribute_updates = {'property1': new_value1, 'property2': new_value2}
            >>> modified_entity = MyClass.modify(entity_id_to_modify, attribute_updates)
        """
        entity_dict: dict | None = cls.get_response(params={'entity_id': entity_id, 'overwrites': overwrites})

        if entity_dict is None:
            return None

        return cls(**entity_dict)

    @classmethod
    def remove(cls, entity_id: str) -> Self | None:
        """
        Remove an entity by its unique identifier.

        Args:
            entity_id (str): The unique identifier of the entity to remove.

        Returns:
            Self: An instance of the class representing the removed entity.
            None: If not found

        Example usage:
            To remove an entity by its unique identifier:

            removed_entity = MyClass.remove("entity_id_here")
            >>> if removed_entity:
            >>>     # Handle the removed entity
            >>> else:
            >>>     # Entity not found
        """
        entity_dict: dict | None = cls.get_response(params={'entity_id': entity_id})

        if entity_dict is None:
            return None

        return cls(**entity_dict)

    @classmethod
    def clone(cls, entity_id: str, overwrites: dict) -> Self | None:
        """
        Clone an existing entity by creating a new one based on provided overwrites.

        Args:
            entity_id (str): The unique identifier of the entity to clone.
            overwrites (dict): A dictionary containing attribute updates to apply to the new cloned entity.

        Returns:
            Self: An instance of the class representing the newly cloned entity.
            None: If not found.

        Example usage:
            To clone an existing entity by creating a new one with attribute overwrites and optional keyword arguments:

            >>> entity_id_to_clone = "entity_id_here"
            >>> attribute_overwrites = {'property1': new_value1, 'property2': new_value2}
            >>> cloned_entity = MyClass.clone(entity_id_to_clone, attribute_overwrites)
        """
        entity_dict: dict | None = cls.get_response(params={'entity_id': entity_id, 'overwrites': overwrites})

        if entity_dict is None:
            return None

        return cls(**entity_dict)

    @classmethod
    def create_many(cls, entity_dict_list: list[dict]) -> list[Self | None]:
        """
        Create multiple new entities using provided dictionaries..

        Args:
            entity_dict_list (List[dict]): A list of dictionaries, each representing an entity's attributes.

        Returns:
            List[Self | None]: A list of instances of the class representing the newly created entities, or None for entities not found.

        Example usage:
            To create multiple entities using a list of dictionaries:

            >>> entity_data_list = [{'property1': value1}, {'property2': value2}]
            >>> created_entities = MyClass.create_many(entity_data_list)
        """
        entities: list[dict | None] = cls.get_response(params={'entity_dict_list': entity_dict_list})

        return [cls(**entity_dict) if entity_dict is not None else None for entity_dict in entities]

    @classmethod
    def modify_many(cls, entity_id_list: list[str], overwrites: dict | list[dict]) -> list[Self | None]:
        """
        Modify multiple existing entities by updating their attributes using the provided overwrites.

        Args:
            entity_id_list (List[str]): A list of unique identifiers for the entities to modify.
            overwrites (Union[dict, List[dict]]): A dictionary or a list of dictionaries containing attribute updates
                to apply to the entities.

        Returns:
            List[Self | None]: A list of instances of the class representing the modified entities, or None for entities not found.

        Example usage:
            To modify multiple existing entities by updating their attributes with overwrites:

            >>> entity_ids_to_modify = ["entity_id1", "entity_id2"]
            >>> attribute_overwrites = [{'property1': new_value1}, {'property2': new_value2}]
            >>> modified_entities = MyClass.modify_many(entity_ids_to_modify, attribute_overwrites)
        """
        entities: list[dict | None] = cls.get_response(params={'entity_id_list': entity_id_list, 'overwrites': overwrites})

        return [cls(**entity_dict) if entity_dict is not None else None for entity_dict in entities]

    @classmethod
    def remove_many(cls, entity_id_list: list[str]) -> list[Self | None]:
        """
        Remove multiple entities by their unique identifiers.

        Args:
            entity_id_list (List[str]): A list of unique identifiers for the entities to remove.

        Returns:
            List[Self | None]: A list of instances of the class representing the removed entities, or None for entities not found.

        Example usage:
            To remove multiple entities by their unique identifiers:

            >>> entity_ids_to_remove = ["entity_id1", "entity_id2"]
            >>> removed_entities = MyClass.remove_many(entity_ids_to_remove)
            >>> for entity in removed_entities:
            >>>     # Handle each removed entity
        """
        entities: list[dict | None] = cls.get_response(params={'entity_id_list': entity_id_list})

        return [cls(**entity_dict) if entity_dict is not None else None for entity_dict in entities]

    @classmethod
    def clone_many(cls, entity_id_list: list[str], overwrites: dict | list[dict]) -> list[Self | None]:
        """
        Clone multiple existing entities by creating new ones based on provided overwrites.

        Args:
            entity_id_list (List[str]): A list of unique identifiers for the entities to clone.
            overwrites (Union[dict, List[dict]]): A dictionary or a list of dictionaries containing attribute updates
                to apply to the new cloned entities.

        Returns:
            List[Self | None]: A list of instances of the class representing the newly copied entities, or None for entities not found.

        Example usage:
            To clone multiple existing entities by creating new ones with attribute overwrites:

            >>> entity_ids_to_clone = ["entity_id1", "entity_id2"]
            >>> attribute_overwrites = [{'property1': new_value1}, {'property2': new_value2}]
            >>> copied_entities = MyClass.clone_many(entity_ids_to_clone, attribute_overwrites)
        """
        entities: list[dict | None] = cls.get_response(params={'entity_id_list': entity_id_list, 'overwrites': overwrites})

        return [cls(**entity_dict) if entity_dict is not None else None for entity_dict in entities]

    def load(self, offset: int = None) -> Self | None:
        """
        Load an entity from the database and return it as an instance of the class.

        Args:
            self (Self): The entity instance to load.
            offset (int, optional): The offset to use for pagination. Defaults to None.

        Returns:
            Self: An instance of the class representing the loaded entity.
            None: If not found.

        Example usage:
            >>> entity_to_load = MyClass(property1="value1", property2="value2")
            >>> loaded_entity = entity_to_load.load()
        """
        if self.id:
            return type(self).retrieve(self.id)

        query = self._entity_to_query()
        return query.load(offset=offset)

    def save(self) -> Self:
        """
        Save the entity to the database and return the saved entity as an instance of the class.

        Args:
            self (Self): The entity instance to save.

        Returns:
            Self: An instance of the class representing the saved entity.

        Example usage:
            To save an entity:

            >>> entity_to_save = MyClass(id="entity_id_here", property1="value1", property2="value2")
            >>> saved_entity = entity_to_save.save()
        """
        entity_dict: dict = self.get_response(self_obj=self)
        return self.__class__(**entity_dict)

    def delete(self) -> Self | None:
        """
        Delete the entity from the database and return the deleted entity as an instance of the class.

        Returns:
            Self: An instance of the class representing the deleted entity.
            None: If not found.

        Example usage:
            To delete an entity:

            >>> entity_to_delete = MyClass(id="entity_id_here")
            >>> deleted_entity = entity_to_delete.delete()
        """
        entity_dict: dict | None = self.get_response(self_obj=self)

        if entity_dict is None:
            return None

        return self.__class__(**entity_dict)
