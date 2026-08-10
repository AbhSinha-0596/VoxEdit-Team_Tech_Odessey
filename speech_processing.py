import os
import requests
from dotenv import load_dotenv
import tempfile
from huggingface_hub import InferenceClient
load_dotenv()

client = InferenceClient(
    provider="hf-inference",
    api_key=os.getenv("HF_API_KEY")
)


RIME_URL = "https://users.rime.ai/v1/rime-tts"
RIME_HEADERS = {
    "Authorization": f"Bearer {os.getenv('RIME_API_KEY')}",
    "Content-Type": "application/json",
    "Accept":"audio/wav"
}

def speech_to_text(audio_bytes: bytes) -> str:
    """response = requests.post(
        HF_API,
        headers=HF_HEADERS,
        data=audio_bytes,
        timeout=120
    )"""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_bytes)
        temp_audio_path = temp_audio.name

    try:
        response = client.automatic_speech_recognition(
            temp_audio_path, 
            model="openai/whisper-large-v3"
        )

        if(isinstance(response, dict)):
            return response.get("text","").strip()
        
        return str(response).strip()
    
    except Exception as e:
        return f"[Speech recognition error: {e}]"

    finally:
        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)


def text_to_speech(text: str):
    payload = {
        "text": text,
        "speaker": "celeste",
        "modelId": "coda"
    }
    r = requests.post(url=RIME_URL, headers=RIME_HEADERS, json=payload, timeout=60)
    """r.raise_for_status()
    with open(out_file, "wb") as f:
        f.write(r.content)
    return out_file""
    if r.status_code != 200:
        raise Exception(f"Rime TTS error {r.status_code}: {r.text}")

    output_path = "response.wav"
    with open(output_path, "wb") as f:
        f.write(r.content)

    return output_path
