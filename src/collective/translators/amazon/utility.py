import boto3



class AmazonTranslatorFactory:
     
     order = 30

     aws_access_key_id = ""
     aws_secret_access_key = ""
     region_name = "eu-west-3"

     @property
     def translator(self):
         return boto3.client("translate", region_name=self.region_name, 
                             aws_access_key_id=self.aws_access_key_id, 
                             aws_secret_access_key=self.aws_secret_access_key)
     
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