import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
text_to_translate = 'Your content you want translate here'
model_id = 'en-es'
# Prepare the Authenticator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)
# Translate
translation = language_translator.translate(
    text=text_to_translate,
    model_id=model_id).get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))
