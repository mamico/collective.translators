import requests


class LibreTranslateTranslatorFactory:
    order = 30

    # TODO: manage settings in the registry

    server_url = "http://localhost:5000"
    api_key = ""
    autodetect_source_language = False
    timeout = 5

    def is_available(self):
        # TODO
        return True

    def available_languages(self):
        # TODO
        return []

    def translate_content(self, content, source_language, target_language, format=None):
        if self.autodetect_source_language:
            source_language = "auto"

        # guess format
        if format is None:
            if "<" in content and ">" in content:
                format = "html"
            else:
                format = "text"

        res = requests.post(
            f"{self.server_url}/translate",
            json={
                "q": content,
                "source": source_language,
                "target": target_language,
                "format": format,
                "alternatives": 0,
                "api_key": self.api_key,
            },
            timeout=self.timeout,
        ).json()
        return res["translatedText"]


LibreTranslateTranslator = LibreTranslateTranslatorFactory()
