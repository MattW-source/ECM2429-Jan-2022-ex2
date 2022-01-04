import requests
import os

key = os.getenv("AZURE_API_SUBSCRIPTION_KEY")
region = os.getenv("AZURE_REGION","uksouth")

headers = {
    'Ocp-Apim-Subscription-Key': key
}

url = f'https://{region}.tts.speech.microsoft.com/cognitiveservices/voices/list'


def get_voices():
    r = requests.get(url, headers=headers)
    voice_list= []

    for voice in r.json():
        voice_list.append(voice['ShortName'])
    return voice_list

if __name__ == "__main__":
    voice_list = get_voices()
    print(voice_list)
