from azurevoices import *

test_get_voices(requests_mock):
    requests_mock.get('https://uksouth.tts.speech.microsoft.com/cognitiveservices/voices/list',
            json=response_json)

    data = get_voices()
    
