import deepl


class DeeplTranslatorFactory:
    order = 30

    # TODO: manage settings in the registry
    # Free API -> https://api-free.deepl.com
    # Pro API -> https://api.deepl.com

    server_url = "https://api-free.deepl.com"
    auth_key = "1234"
    autodetect_source_language = False

    @property
    def translator(self):
        return deepl.Translator(server_url=self.server_url, auth_key=self.auth_key)

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
