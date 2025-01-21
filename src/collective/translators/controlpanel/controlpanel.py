from collective.translators.interfaces import IDeeplControlPanel
from plone.app.registry.browser import controlpanel
from plone.base import PloneMessageFactory as _


# from plone.i18n.interfaces import ILanguageSchema
# from Products.statusmessages.interfaces import IStatusMessage
# from z3c.form import button


class DeeplControlPanel(controlpanel.RegistryEditForm):
    id = "DeeplControlPanel"
    label = _("Deepl Translation Service")
    schema = IDeeplControlPanel
