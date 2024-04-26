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
from everysk.core.fields import ListField, StrField, DictField

from everysk.sdk.entities.query import Query
from everysk.sdk.entities.script import Script
from everysk.sdk.entities.base import BaseEntity, ScriptMetaClass
from everysk.sdk.entities.fields import EntityNameField, EntityDescriptionField, EntityLinkUIDField, EntityWorkspaceField, EntityDateTimeField, EntityTagsField

###############################################################################
#   Report Implementation
###############################################################################
class Report(BaseEntity, metaclass=ScriptMetaClass):
    """
    This class represents a report entity object and provides methods to validate and manage the entity's data.

    Attributes:
        script (Script): The script object associated with the report.
        id (StrField): The unique identifier of the report.
        workspace (EntityWorkspaceField): The workspace of the report.
        name (EntityNameField): The name of the report.
        tags (EntityTagsField): The tags of the report.
        description (EntityDescriptionField): The description of the report.
        link_uid (EntityLinkUIDField): The link UID of the report.
        date (EntityDateTimeField): The date associated with the report.
        widgets (ListField): A list of widgets associated with the report.
        url (StrField): The URL of the report.
        authorization (StrField): The authorization string for accessing the report.
        config_cascaded (DictField): A dictionary of cascaded configuration settings.
        layout_content (DictField): A dictionary representing the layout content of the report.

        version (StrField): The version of the report.
        created_on (DateTimeField): The created on date of the report.
        updated_on (DateTimeField): The updated on date of the report.

    Example usage:
        >>> from everysk.sdk.entities.report.base import Report
        >>> report = Report()
        >>> report.script = 'my_script'
        >>> report.id = 'repo_12345678'
        >>> report.name = 'My Report'
        >>> report.tags = ['tag1', 'tag2']
        >>> report.description = 'This is a sample report.'
        >>> report.workspace = 'my_workspace'
        >>> report.date = '20220101'
        >>> report.widgets = [{'type': 'chart', 'data': {...}}, {'type': 'table', 'data': {...}}]
        >>> report.url = '/sefdsf5s54sdfsksdfs5'
        >>> report.authorization = 'private'
        >>> report.data_hash = 'hash123'
        >>> report.config_cascaded = {'setting1': 'value1', 'setting2': 'value2'}
        >>> report.layout_content = {'section1': {...}, 'section2': {...}}
        >>> report.create()
        >>> report.to_dict()
        {
            'id': 'repo_12345678',
            'script': 'my_script',
            'name': 'My Report',
            'description': 'This is a sample report.',
            'tags': ['tag1', 'tag2'],
            'link_uid': None,
            'workspace': 'my_workspace',
            'date': '20220101',
            'widgets': [{'type': 'chart', 'data': {...}}, {'type': 'table', 'data': {...}}],
            'url': '/sefdsf5s54sdfsksdfs5',
            'authorization': 'private',
            'config_cascaded': {'setting1': 'value1', 'setting2': 'value2'},
            'layout_content': {'section1': {...}, 'section2': {...}}
        }
    """

    script: Script = None
    _orderable_attributes = ListField(default=['date', 'created_on', 'updated_on', 'name'])

    id = StrField(regex=settings.REPORT_ID_REGEX, max_size=settings.REPORT_ID_MAX_SIZE, required_lazy=True, empty_is_none=True)

    name = EntityNameField()
    description = EntityDescriptionField()
    tags = EntityTagsField()
    link_uid = EntityLinkUIDField()
    workspace = EntityWorkspaceField()
    date = EntityDateTimeField()

    widgets = ListField()
    url = StrField(required_lazy=True)
    authorization = StrField(default=None, regex=settings.REPORT_AUTHORIZATION_REGEX, required_lazy=True)
    config_cascaded = DictField(required_lazy=True)
    layout_content = DictField(required_lazy=True)

    def validate(self) -> bool:
        """
        This method validates the entity object and raises an exception if it is not
        valid. The validation is performed by calling the `validate` method of each field
        of the entity.

        Args:
            self (Self): The entity object to be validated.

        Raises:
            FieldValueError: If the entity object is not valid.

        Returns:
            bool: True if the entity object is valid, False otherwise.

        Example usage:
            >>> entity = Entity()
            >>> entity.validate()
            True
        """
        return self.get_response(self_obj=self)

    @staticmethod
    def get_id_prefix() -> str:
        """
        Returns the prefix of the report id field value.

        Returns:
            str: The prefix of the report id field value.

        Example usage:
            >>> Report.get_id_prefix()
            'repo_'
        """
        return settings.REPORT_ID_PREFIX

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
        dct: dict = super().to_dict(with_internals)

        relative_url = None
        absolute_url = None
        if self.url is not None:
            relative_url: str = f'{settings.REPORT_URL_PATH}{self.url}'
            absolute_url: str = f'{settings.APP_URL}{relative_url}'

        dct['url'] = absolute_url
        dct['absolute_url'] = absolute_url
        dct['relative_url'] = relative_url

        dct['authorization'] = dct['authorization'].upper() if dct['authorization'] else None

        dct.pop('config_cascaded')
        dct.pop('layout_content')
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
