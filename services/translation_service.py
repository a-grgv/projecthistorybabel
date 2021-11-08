"""
This module contains methods to translate text using Azure Translation API
"""

from typing import List

import requests

from utils.service_constants import TRANSLATE_REQUEST_PARAMS, TRANSLATE_URL, TRANSLATE_HEADERS


def translate_text(text: str) -> List[dict]:
    """
    Translate given text
    :param text: Text to be translated
    :return: List of translations from detected languages
    """
    body = [{
        'text': text
    }]

    request = requests.post(TRANSLATE_URL, params=TRANSLATE_REQUEST_PARAMS, headers=TRANSLATE_HEADERS, json=body)
    response = request.json()
    return response
