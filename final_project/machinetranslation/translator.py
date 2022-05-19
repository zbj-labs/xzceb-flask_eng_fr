"""
    Uses IBM Watson's Language Translator to translate text
    from English to French and vice-versa.
"""
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

api_key = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    translate the text input in english to french and return the french text
    """
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text = translation['translations'][0]['translation']
    except:
        french_text = None

    return french_text

def french_to_english(french_text):
    """
    translate the text input in french to english and return the english text
    """
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        english_text = translation['translations'][0]['translation']
    except:
        english_text = None

    return english_text
