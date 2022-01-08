'''
 Azure Text To Speech API Working Sample using Requests
'''

import requests
import os
import logging
logging.basicConfig(level=logging.DEBUG)

# Message you want to convert to speech
message = "Hello World. This is a text message converted to speech using Microsoft Azure."

# Get subscription key for service
key = os.getenv("AZURE_API_SUBSCRIPTION_KEY")

# Get region if provided, otherwise default to uksouth
region = os.getenv("AZURE_REGION","uksouth")

# url to the endpoint that will perform our text to speech request
voice_api_url = f'https://{region}.tts.speech.microsoft.com/cognitiveservices/v1'

#####################################################################
# Make request to text to speech service                            #
#####################################################################

# Set options and provide our subscription key
headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Content-Type': 'application/ssml+xml',
    'X-Microsoft-OutputFormat': 'audio-48khz-192kbitrate-mono-mp3'
}

# Set which voice to use. You can obtain a list of valid voices from azurevoices.py
voice = "en-US-ChristopherNeural"

# Data to send as part of the request. Contains the voice and message we want to use.
data = f"""
 <speak version='1.0' xml:lang='en-US'>
 <voice xml:lang='en-US' xml:gender='Male' name='{voice}'>{message}</voice>
 </speak>"""

# Send our request to the voice api and save the result in voice_response
voice_response = requests.post(voice_api_url, data=data, headers=headers)

# Requests returns binary content in response.content
# If the data was zipped by the server, requests will unzip it by default.
# https://docs.python-requests.org/en/master/user/quickstart/#binary-response-content

# save the converted audio to a file called "output.wav" in the same directory as the program
with open("output.wav", "wb") as out:
    out.write(voice_response.content)
