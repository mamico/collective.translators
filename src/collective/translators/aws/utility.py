from plone import api

import boto3


class AWSTranslatorFactory:
    order = 30

    @property
    def translator(self):
        access_key = api.portal.get_registry_record(
            "collective.translators.interfaces.IAWSTranslateControlPanel.access_key"
        )
        secret_key = api.portal.get_registry_record(
            "collective.translators.interfaces.IAWSTranslateControlPanel.secret_key"
        )
        region_name = api.portal.get_registry_record(
            "collective.translators.interfaces.IAWSTranslateControlPanel.region_name"
        )
        return boto3.client(
            "translate",
            region_name=region_name,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )

    def is_available(self):
        try:
            enabled = api.portal.get_registry_record(
                "collective.translators.interfaces.IAWSTranslateControlPanel.enabled"
            )
            return enabled
        except api.exc.InvalidParameterError:
            return False

    def available_languages(self):
        try:
            # Check if the translator client is available
            if not self.translator:
                return ["Not set"]

            # Get all available languages
            response = self.translator.list_languages(DisplayLanguageCode="en")

            # Extract source languages
            source_lang_codes = [
                lang["LanguageCode"].lower() for lang in response["Languages"]
            ]

            # Create a list of tuples (source_lang, target_lang)
            translation_pairs = [
                (source_lang, target_lang)
                for source_lang in source_lang_codes
                for target_lang in source_lang_codes
            ]

            return translation_pairs

        except boto3.exceptions.Boto3Error:
            return ["Not set"]

    def translate_content(self, content, source_language, target_language):
        try:
            res = self.translator.translate_text(
                Text=content,
                SourceLanguageCode=source_language,
                TargetLanguageCode=target_language,
            )
            return res["TranslatedText"]
        except boto3.exceptions.Boto3Error:
            # Retry with autodetect
            try:
                res = self.translator.translate_text(
                    Text=content, TargetLanguageCode=target_language
                )
                return res["TranslatedText"]
            except boto3.exceptions.Boto3Error:
                return "Language not supported"


AWSTranslator = AWSTranslatorFactory()
