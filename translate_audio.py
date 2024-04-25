import openai
import requests
import json

def transcribe_audio(audio_path):
    """Use Whisper to transcribe the audio file to text."""
    openai.api_key = 'your_openai_api_key'
    
    with open(audio_path, "rb") as audio_file:
        response = openai.Audio.transcriptions.create(
            audio=audio_file,
            model="whisper-large"
        )
    return response['text']

def translate_text(text, source_lang, target_lang):
    """Translate text using Llama2 API."""
    headers = {
        'Authorization': 'Bearer your_llama2_api_key',
        'Content-Type': 'application/json',
    }
    data = {
        "text": text,
        "source_language": source_lang,
        "target_language": target_lang
    }
    response = requests.post('https://api.llama2.example.com/translate', headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['translated_text']
    else:
        print("Failed to translate text:", response.text)
        return None

def main(audio_path, source_lang='en', target_lang='es'):
    """Transcribe and translate an audio file."""
    print("Transcribing audio...")
    text = transcribe_audio(audio_path)
    print("Original text:", text)

    print("Translating text...")
    translated_text = translate_text(text, source_lang, target_lang)
    print("Translated text:", translated_text)

if __name__ == "__main__":
    audio_path = "path_to_your_audio_file.mp3"
    main(audio_path)
