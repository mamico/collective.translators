"""Module where all interfaces, events and exceptions live."""

from collective.translators import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IBrowserLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IDeeplControlPanel(Interface):
    enabled = schema.Bool(
        description=_("Translation service enabled"),
        default=True,
    )

    order = schema.Int(
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
