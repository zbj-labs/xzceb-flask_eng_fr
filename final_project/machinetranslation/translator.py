import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """
    translate the text input in english to french and return the french text
    """
    try:
        translation = language_translator.translate(
            text=englishText,
            model_id='en-fr').get_result()
        frenchText = translation['translations'][0]['translation']
    except:
        frenchText = None

    return frenchText

def frenchToEnglish(frenchText):
    """
    translate the text input in french to english and return the english text
    """
    try:
        translation = language_translator.translate(
            text=frenchText,
            model_id='fr-en').get_result()
        englishText = translation['translations'][0]['translation']
    except:
        englishText = None

    return englishText
