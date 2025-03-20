from collective.translators import _
from collective.translators.interfaces import IAWSTranslateControlPanel
from collective.translators.interfaces import IDeeplControlPanel
from collective.translators.interfaces import IDeepSeekControlPanel
from collective.translators.interfaces import ILibreTranslateControlPanel
from plone.app.registry.browser import controlpanel
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


class AWSTranslateControlPanel(controlpanel.RegistryEditForm):
    id = "AWSTranslateControlPanel"
    label = _("AWS Translate Service")
    schema = IAWSTranslateControlPanel


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
class AWSTranslateRegistryConfigletPanel(RegistryConfigletPanel):
    """AWS Translate control panel"""

    schema = IAWSTranslateControlPanel
    schema_prefix = "aws_translate"
    configlet_id = "aws-translate-controlpanel"
    configlet_category_id = "Products"
    title = _("AWS Translate Settings")
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
