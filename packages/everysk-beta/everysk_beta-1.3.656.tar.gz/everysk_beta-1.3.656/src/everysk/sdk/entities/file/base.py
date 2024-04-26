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
from everysk.config import settings
from everysk.core.fields import ListField, StrField, ChoiceField

from everysk.sdk.engines.cryptography import generate_unique_id
from everysk.sdk.entities.query import Query
from everysk.sdk.entities.script import Script
from everysk.sdk.entities.base import BaseEntity, ScriptMetaClass
from everysk.sdk.entities.fields import EntityNameField, EntityDescriptionField, EntityLinkUIDField, EntityWorkspaceField, EntityDateTimeField, EntityTagsField

###############################################################################
#   File Implementation
###############################################################################
class File(BaseEntity, metaclass=ScriptMetaClass):
    """
    This class represents a file entity object and provides methods to validate and manage the entity's data.

    Attributes:
        script (Script): The script object associated with the file.
        id (StrField): The unique identifier of the file.
        workspace (EntityWorkspaceField): The workspace of the file.
        name (EntityNameField): The name of the file.
        tags (EntityTagsField): The tags of the file.
        description (EntityDescriptionField): The description of the file.
        link_uid (EntityLinkUIDField): The link UID of the file.
        date (EntityDateTimeField): The date associated with the file.
        data (StrField): The file data in base64 format.
        url (StrField): The URL of the file.
        content_type (ChoiceField): The content type of the file.

        version (StrField): The version of the datastore.
        created_on (DateTimeField): The created on date of the datastore.
        updated_on (DateTimeField): The updated on date of the datastore.

    Example usage:
        >>> from everysk.sdk.entities.file.base import File
        >>> file = File()
        >>> file.script = 'my_script'
        >>> file.id = 'file_12345678'
        >>> file.name = 'My File'
        >>> file.tags = ['tag1', 'tag2']
        >>> file.description = 'This is a sample file.'
        >>> file.workspace = 'my_workspace'
        >>> file.date = DateTime.fromisoformat('20220101')
        >>> file.data = 'base64_encoded_data_here'
        >>> file.content_type = 'application/pdf'
        >>> file.url = '/1234567891011211234567890'
        >>> file.create()
        >>> file.to_dict()
        {
            'id': 'file_12345678',
            'script': 'my_script',
            'name': 'My File',
            'description': 'This is a sample file.',
            'tags': ['tag1', 'tag2'],
            'link_uid': None,
            'workspace': 'my_workspace',
            'date': '20220101',
            'data': 'base64_encoded_data_here',
            'content_type': 'application/pdf',
            'url': '/1234567891011211234567890'
            'created': '2021-01-01T00:00:00.000000Z',
            'updated': '2021-01-01T00:00:00.000000Z',
        }
    """

    script: Script
    _orderable_attributes = ListField(default=['date', 'created_on', 'updated_on', 'name'])

    id = StrField(regex=settings.FILE_ID_REGEX, max_size=settings.FILE_ID_MAX_SIZE, required_lazy=True, empty_is_none=True)

    name = EntityNameField()
    description = EntityDescriptionField()
    tags = EntityTagsField()
    link_uid = EntityLinkUIDField()
    workspace = EntityWorkspaceField()

    date = EntityDateTimeField()

    hash = StrField(default=None, max_size=settings.FILE_HASH_LENGTH, required_lazy=True)
    data = StrField(default=None, max_size=settings.FILE_DATA_MAX_SIZE_IN_BASE64, required_lazy=True)
    content_type = ChoiceField(default=None, choices=settings.FILE_CONTENT_TYPES, required_lazy=True)
    url = StrField(required_lazy=True)

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
            >>> file = File()
            >>> file.validate()
            True
        """
        return self.get_response(self_obj=self)

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
        dct['url'] = f"{settings.FILE_URL_PATH}{dct['url']}" if dct['url'] else None
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
        query = super()._entity_to_query()

        if self.url is not None:
            query = query.where('url', self.url)

        return query

    @staticmethod
    def get_id_prefix() -> str:
        """
        Returns the prefix of the file id field value.

        Returns:
            str: The prefix of the file id field value.

        Example usage:
            >>> File.get_id_prefix()
            'file_'
        """
        return settings.FILE_ID_PREFIX

    @staticmethod
    def generate_url() -> str:
        """
        Generate a unique url for the file.

        Returns:
            str: A unique url for the file.

        Example usage:
            >>> File.generate_url()
            '/1234567891011211234567890'
        """
        return f'/{generate_unique_id()}'
