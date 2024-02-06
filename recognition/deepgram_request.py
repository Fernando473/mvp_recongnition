import requests
import json

from deepgram import DeepgramClient, FileSource, PrerecordedOptions


def transcribe_audio(AUDIO_FILE):
    try:
        API_KEY = "86fce1189295c598f4fe347de1f656c330b17f59"
        deepgram = DeepgramClient(API_KEY)

        with open(AUDIO_FILE, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
            language="es"
        )

        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

        response_json = response.to_json(indent=4)

        response_data = json.loads(response_json)

        transcription = response_data["results"]["channels"][0]["alternatives"][0]["transcript"]
        return transcription

    except Exception as e:
        return f"Exception: {e}"


def transcribe_audio_with_deepgram(url):
    api_url = "https://api.deepgram.com/v1/listen?language=es&model=nova"
    api_key = "86fce1189295c598f4fe347de1f656c330b17f59"

    headers = {
        "Authorization": f"Token {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "url": url,
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()

        result = response.json()
        return result['results']['channels'][0]['alternatives'][0]['transcript']
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        raise e
