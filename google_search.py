import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_CSE_API_KEY")
CX = os.getenv("GOOGLE_CSE_CX_ID")

def search_cafes(prompt):
    query = f"{prompt} site:tripadvisor.in OR site:zomato.com OR site:magicpin.in"
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX}"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json().get("items", [])
    return []
