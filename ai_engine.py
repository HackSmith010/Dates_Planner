import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def call_together_ai(prompt):
    url = "https://api.together.xyz/inference"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "prompt": prompt,
        "max_tokens": 500,
        "temperature": 0.8
    }
    res = requests.post(url, headers=headers, json=body)
    return res.json().get("output", None) if res.status_code == 200 else None

def generate_card_details(user_prompt, cafe_snippets):
    cafes_text = "\n\n".join([f"{c['title']}: {c['snippet']}" for c in cafe_snippets])
    prompt = f"""
User asked: "{user_prompt}"

Below are some cafes. For each one, return:
1. 📍 Name
2. 🕒 Best time
3. 🎶 Vibe
4. 💸 Approx cost
5. ✨ Short romantic reason why it's perfect

Cafes:
{cafes_text}

Format each cafe with emojis and in 5 lines, like:
📍 Cafe Name  
🕒 Best time  
🎶 Vibe  
💸 Approx cost  
✨ Comment
"""

    return call_together_ai(prompt)
