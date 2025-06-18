import requests
import json

# Gemini API Key (never expose this in production!)
API_KEY = "AIzaSyBiF5-GEJgbXuLYxCUv3c7AWmElz-YO7O0"

# Base URL for Gemini REST API (flash model)
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# Instruction used in every prompt
BASE_INSTRUCTION = """
You are a medical assistant AI specialized in neurology and epilepsy.
Explain in simple terms, avoid medical jargon unless necessary.
If a seizure is detected, include care tips, symptoms, and suggest basic medicines or lifestyle changes.
Always respond with empathy and clarity.
"""

def ask_gemini(user_query):
    full_prompt = BASE_INSTRUCTION + f"\n\nUser Query: {user_query}\n\nAI:"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": full_prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        content = response.json()
        return content['candidates'][0]['content']['parts'][0]['text']
    else:
        return f"❌ Gemini API Error {response.status_code}: {response.text}"
