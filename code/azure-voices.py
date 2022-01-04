import requests
import os

key = os.getenv("AZURE_API_SUBSCRIPTION_KEY")
region = os.getenv("AZURE_REGION","uksouth")

headers = {
    'Ocp-Apim-Subscription-Key': key
}

url = f'https://{region}.tts.speech.microsoft.com/cognitiveservices/voices/list'


r = requests.get(url, headers=headers)

for voice in r.json():
    print(voice['ShortName'])
