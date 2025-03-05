from collective.translators.interfaces import IDeeplControlPanel
from collective.translators.interfaces import IAmazonTranslateControlPanel
from collective.translators.interfaces import ILibreTranslateControlPanel
from plone.app.registry.browser import controlpanel
from plone.base import PloneMessageFactory as _
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.component import adapter
from zope.interface import Interface


# from plone.i18n.interfaces import ILanguageSchema
# from Products.statusmessages.interfaces import IStatusMessage
# from z3c.form import button


class DeeplControlPanel(controlpanel.RegistryEditForm):
    id = "DeeplControlPanel"
    label = _("Deepl Translation Service")
    schema = IDeeplControlPanel

class AmazonTranslateControlPanel(controlpanel.RegistryEditForm):
    id = "AmazonTranslateControlPanel"
    label = _("Amazon Translate Service")
    schema = IAmazonTranslateControlPanel

class LibreTranslateControlPanel(controlpanel.RegistryEditForm):
    id = "LibreTranslateControlPanel"
    label = _("Libre Translate Service")
    schema = ILibreTranslateControlPanel

@adapter(Interface, Interface)
class DeeplRegistryConfigletPanel(RegistryConfigletPanel):
    """Deepl control panel"""

    schema = IDeeplControlPanel
    schema_prefix = "deepl"
    configlet_id = "deepl-controlpanel"
    configlet_category_id = "Products"
    title = "Deepl Settings"
    group = "Products"

@adapter(Interface, Interface)
class AmazonTranslateRegistryConfigletPanel(RegistryConfigletPanel):
    """Amazon Translate control panel"""

    schema = IAmazonTranslateControlPanel
    schema_prefix = "amazon_translate"
    configlet_id = "amazon-translate-controlpanel"
    configlet_category_id = "Products"
    title = "Amazon Translate Settings"
    group = "Products"

@adapter(Interface, Interface)
class LibreTranslateRegistryConfigletPanel(RegistryConfigletPanel):
    """Libre Translate control panel"""

    schema = ILibreTranslateControlPanel
    schema_prefix = "libretranslate"
    configlet_id = "libre-translate-controlpanel"
    configlet_category_id = "Products"
    title = "Libre Translate Settings"
    group = "Products"