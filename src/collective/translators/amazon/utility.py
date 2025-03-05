import boto3
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from collective.translators.interfaces import IAmazonTranslateControlPanel

class AmazonTranslatorFactory:

    order = 30

    @property
    def translator(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IAmazonTranslateControlPanel, prefix="amazon_translate")
        access_key = settings.access_key
        secret_key = settings.secret_key
        region_name = settings.region_name
        return boto3.client("translate", region_name=region_name, 
                            aws_access_key_id=access_key, 
                            aws_secret_access_key=secret_key)

    def is_available(self):
        return True

    def available_languages(self):
        return []

    def translate_content(self, content, source_language, target_language):
        content = content.lower()
        res = self.translator.translate_text(
            Text=content, SourceLanguageCode=source_language, TargetLanguageCode=target_language
        )
        return res["TranslatedText"]

AmazonTranslator = AmazonTranslatorFactory()