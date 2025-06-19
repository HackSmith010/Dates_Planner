import os
from dotenv import load_dotenv
from googlesearch import search
import requests

load_dotenv()
GOOGLE_CSE_API_KEY = os.getenv("GOOGLE_CSE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

def search_cafes(prompt):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_CSE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": prompt + " romantic cafe"
    }
    res = requests.get(url, params=params)
    if res.status_code == 200:
        return res.json().get("items", [])
    return []
