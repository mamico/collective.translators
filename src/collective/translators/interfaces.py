"""Module where all interfaces, events and exceptions live."""

from collective.translators import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IBrowserLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IBaseControlPanel(Interface):
    enabled = schema.Bool(
        title=_("Enabled"),
        description=_("Translation service enabled"),
        default=True,
    )

    order = schema.Int(
        title=_("Order"),
        description=_("Ordering service translation"),
        default=30,
        required=True,
    )

    source_languages = schema.List(
        title=_("Source languages"),
        required=False,
        default=[],
        missing_value=[],
        value_type=schema.Choice(
            vocabulary="plone.app.vocabularies.AvailableContentLanguages"
        ),
    )

    target_languages = schema.List(
        title=_("Target languages"),
        required=False,
        default=[],
        missing_value=[],
        value_type=schema.Choice(
            vocabulary="plone.app.vocabularies.AvailableContentLanguages"
        ),
    )


class IDeeplControlPanel(IBaseControlPanel):
    api_key = schema.TextLine(
        title=_("API Key"),
        description=_("The API key for the Deepl translation service."),
        required=False,
    )


class IDeepSeekControlPanel(IBaseControlPanel):
    api_key = schema.TextLine(
        title=_("API Key"),
        description=_("The API key for the DeepSeek service."),
        required=False,
    )


class IAWSTranslateControlPanel(IBaseControlPanel):
    access_key = schema.TextLine(
        title=_("Access key"),
        description=_("The key for the access to AWS Translate service."),
        required=False,
    )

    secret_key = schema.TextLine(
        title=_("Secret key"),
        description=_("The secret key for the access to AWS Translate service."),
        required=False,
    )

    region_name = schema.TextLine(
        title=_("Region"),
        description=_("The region for the AWS Translate service."),
        required=True,
        default="eu-west-3",
    )


class ILibreTranslateControlPanel(IBaseControlPanel):
    api_key = schema.TextLine(
        title=_("API Key"),
        description=_("The API key for the Libre translate translation service."),
        required=False,
    )
