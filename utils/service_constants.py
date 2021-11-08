import os
import uuid

TRANSLATE_SUBSCRIPTION_KEY = os.environ["TRANSLATION_KEY"]
TRANSLATE_ENDPOINT = "https://api.cognitive.microsofttranslator.com"
TRANSLATE_PATH = '/translate'
TRANSLATE_LOCATION = 'germanywestcentral'
TRANSLATE_REQUEST_PARAMS = {
    'api-version': '3.0',
    'to': ['en']
}
TRANSLATE_URL = TRANSLATE_ENDPOINT + TRANSLATE_PATH
TRANSLATE_HEADERS = {
    'Ocp-Apim-Subscription-Key': TRANSLATE_SUBSCRIPTION_KEY,
    'Ocp-Apim-Subscription-Region': TRANSLATE_LOCATION,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

SPACY_ENGLISH_MODEL = "en_core_web_sm"
