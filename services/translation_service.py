import os

import requests, uuid

# Add your subscription key and endpoint
subscription_key = os.environ["TRANSLATION_KEY"]
endpoint = "https://api.cognitive.microsofttranslator.com"

path = '/translate'
location = 'germanywestcentral'
params = {
    'api-version': '3.0',
    'to': ['en']
}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}


def translate_text(text):
    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return response
