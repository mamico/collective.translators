import deepl   
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from collective.translators.interfaces import IDeeplControlPanel


class DeeplTranslatorFactory:
    order = 30

    # TODO: manage settings in the registry
    # Free API -> https://api-free.deepl.com
    # Pro API -> https://api.deepl.com

    server_url = "https://api-free.deepl.com"
    autodetect_source_language = False

    @property
    def translator(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IDeeplControlPanel, prefix="deepl")
        api_key = settings.api_key
        return deepl.Translator(server_url=self.server_url, auth_key=api_key)

    def is_available(self):
        return True

    def available_languages(self):
        # All
        return []

    def translate_content(self, content, source_language, target_language):
        if self.autodetect_source_language:
            res = self.translator.translate_text(content, target_lang=target_language)
        else:
            res = self.translator.translate_text(
                content, source_lang=source_language, target_lang=target_language
            )
        return res.text


DeeplTranslator = DeeplTranslatorFactory()
