import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

def call_together_ai(prompt):
    import os
    import requests

    TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
    url = "https://api.together.xyz/inference"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "prompt": prompt,
        "max_tokens": 600,
        "temperature": 0.85
    }

    res = requests.post(url, headers=headers, json=body)
    if res.status_code == 200:
        try:
            return res.json()["choices"][0]["text"].strip()
        except (KeyError, IndexError):
            return None
    return None

def generate_card_details(user_prompt, cafes_info):
    formatted_list = ""
    for i, cafe in enumerate(cafes_info, start=1):
        formatted_list += f"{i}. {cafe['name']} — {cafe['address']}\n"

    prompt = f"""
You're a romantic date planner AI.

Here’s what the user wants:
"{user_prompt}"

Here are 5 potential cafes/places:
{formatted_list}

Now generate a romantic date suggestion for each spot in this format (in markdown):

📍 **Cafe Name, Area**  
🕰️ Best time: your suggested 2-hour window  
🎶 Short vibe description (like fairy lights, music, beachy)  
💸 Approx ₹[amount] for two  
✨ “One cute line about why it’s a great date spot”

Write 10-12 cards only, based on your favorite ones from above. Keep it fun, warm, and vivid.
"""

    return call_together_ai(prompt)

