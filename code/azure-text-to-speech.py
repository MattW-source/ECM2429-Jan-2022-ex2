# To use this example set a subscription key and a region
# 
# export AZURE_API_SUBSCRIPTION_KEY=
# export AZURE_REGION=uksouth
# In Windows use SET rather than export


import requests
import os
import logging

logging.basicConfig(level=logging.DEBUG)

key = os.getenv("AZURE_API_SUBSCRIPTION_KEY")
region = os.getenv("AZURE_REGION","uksouth")

url = f'https://{region}.tts.speech.microsoft.com/cognitiveservices/v1'

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Content-Type': 'application/ssml+xml',
    'X-Microsoft-OutputFormat': 'riff-16khz-16bit-mono-pcm'
    # RIFF is also known as WAV.
    # Other formats are supported by the Azure API but will require decoding
    # before playing. e.g. 'audio-16khz-128kbitrate-mono-mp3'
}

text = "Hola. My Name Is Werner Brandes. My Voice Is My Passport. Verify Me."
#voice = "en-US-GuyRUS"
voice = "es-ES-Laura"

data = f"""
<speak version='1.0' xml:lang='en-US'>
 <voice xml:lang='en-US' xml:gender='Male' name='{voice}'>{text}</voice>
</speak>"""

response = requests.post(url, data=data, headers=headers)

logging.info(str(response))

# Requests returns binary content in response.content
# If the data was zipped by the server, requests will unzip it by default.
# https://docs.python-requests.org/en/master/user/quickstart/#binary-response-content

with open("output.wav", "wb") as out:
    out.write(response.content)

#from play import play
#play('output.wav')

