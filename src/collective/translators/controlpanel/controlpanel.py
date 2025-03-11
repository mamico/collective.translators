from collective.translators.interfaces import IDeeplControlPanel
from collective.translators.interfaces import IAmazonTranslateControlPanel
from collective.translators.interfaces import ILibreTranslateControlPanel
from collective.translators.interfaces import IDeepSeekControlPanel
from plone.app.registry.browser import controlpanel
from collective.translators import _
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

class DeepSeekControlPanel(controlpanel.RegistryEditForm):
    id = "DeepSeekControlPanel"
    label = _("DeepSeek Translation Service")
    schema = IDeepSeekControlPanel

@adapter(Interface, Interface)
class DeeplRegistryConfigletPanel(RegistryConfigletPanel):
    """Deepl control panel"""

    schema = IDeeplControlPanel
    schema_prefix = "deepl"
    configlet_id = "deepl-controlpanel"
    configlet_category_id = "Products"
    title = _("Deepl Settings")
    group = "Products"

@adapter(Interface, Interface)
class AmazonTranslateRegistryConfigletPanel(RegistryConfigletPanel):
    """Amazon Translate control panel"""

    schema = IAmazonTranslateControlPanel
    schema_prefix = "amazon_translate"
    configlet_id = "amazon-translate-controlpanel"
    configlet_category_id = "Products"
    title = _("Amazon Translate Settings")
    group = "Products"

@adapter(Interface, Interface)
class LibreTranslateRegistryConfigletPanel(RegistryConfigletPanel):
    """Libre Translate control panel"""

    schema = ILibreTranslateControlPanel
    schema_prefix = "libretranslate"
    configlet_id = "libre-translate-controlpanel"
    configlet_category_id = "Products"
    title = _("Libre Translate Settings")
    group = "Products"

@adapter(Interface, Interface)
class DeepSeekRegistryConfigletPanel(RegistryConfigletPanel):
    """DeepSeek control panel"""

    schema = IDeepSeekControlPanel
    schema_prefix = "deepseek"
    configlet_id = "deepseek-controlpanel"
    configlet_category_id = "Products"
    title = _("DeepSeek Settings")
    group = "Products"