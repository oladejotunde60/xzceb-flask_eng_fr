import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
text_to_translate = input("Enter text to translate:")

# Translation instance
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

# Translation function: English to French

def english_to_french(english_text):
    """
# Translation function: English to French
    """
    english_text = language_translator.translate(
    text=text_to_translate,
    model_id='en-fr').get_result()
    return english_text

    # Translation function: French to English
def french_to_english(french_text):
    """
# Translation function: French to English
    """
    french_text = language_translator.translate(
    text=text_to_translate,
    model_id='fr-en').get_result()
    return french_text
