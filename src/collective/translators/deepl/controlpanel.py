from collective.translators import _
from collective.translators.interfaces import IControlPanel
from plone.app.registry.browser import controlpanel
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.component import adapter
from zope.interface import Interface

import zope.schema


class IDeeplControlPanel(IControlPanel):
    api_key = zope.schema.TextLine(
        title=_("API Key"),
        description=_("The API key for the Deepl translation service."),
        required=False,
    )


class DeeplControlPanel(controlpanel.RegistryEditForm):
    id = "DeeplControlPanel"
    label = _("Deepl Translation Service")
    schema = IDeeplControlPanel


@adapter(Interface, Interface)
class DeeplRegistryConfigletPanel(RegistryConfigletPanel):
    """Deepl control panel"""

    schema = IDeeplControlPanel
    schema_prefix = "deepl"
    configlet_id = "deepl-controlpanel"
    configlet_category_id = "Products"
    title = _("Deepl Settings")
    group = "Products"
