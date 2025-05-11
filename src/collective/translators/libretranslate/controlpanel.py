from collective.translators import _
from collective.translators.interfaces import IControlPanel
from plone.app.registry.browser import controlpanel
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.component import adapter
from zope.interface import Interface

import zope.schema


class ILibreTranslateControlPanel(IControlPanel):
    api_key = zope.schema.TextLine(
        title=_("API Key"),
        description=_("The API key for the Libre translate translation service."),
        required=False,
    )


class LibreTranslateControlPanel(controlpanel.RegistryEditForm):
    id = "LibreTranslateControlPanel"
    label = _("Libre Translate Service")
    schema = ILibreTranslateControlPanel


@adapter(Interface, Interface)
class LibreTranslateRegistryConfigletPanel(RegistryConfigletPanel):
    """Libre Translate control panel"""

    schema = ILibreTranslateControlPanel
    schema_prefix = "libretranslate"
    configlet_id = "libre-translate-controlpanel"
    configlet_category_id = "Products"
    title = _("Libre Translate Settings")
    group = "Products"
