import os
import json
import requests
import re
from dotenv import load_dotenv

load_dotenv()

MISTRAL_URL = "https://api.mistral.ai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('MISTRAL_API_KEY')}",
    "Content-Type": "application/json"
}

SYSTEM_PROMPT = """
You convert image editing requests into JSON commands.

Supported actions:
brightness {factor}
saturation {factor}
sharpness {factor}
blur {radius}
warmth {intensity}
background_blur

If the user requests single or multiple edits, return a JSON array.

Examples:

Single:
{"action":"brightness","factor":1.3}

Multiple:
[
  {"action":"brightness","factor":1.2},
  {"action":"warmth","intensity":20},
  {"action":"blur","radius":2}
]

Return ONLY valid JSON.
"""

def route_command(user_text):
    payload = {
        "model": "mistral-small-latest",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ],
        "temperature": 0
    }

    r = requests.post(MISTRAL_URL, headers=HEADERS, json=payload, timeout=60)
    r.raise_for_status()

    content = r.json()["choices"][0]["message"]["content"]
    
    if content.startswith("```"):
        content = re.sub(r"^```(?:json)?", "", content)
        content = content.rstrip("`").strip()

    if not content:
        raise ValueError("LLM returned an empty response")

    return json.loads(content)