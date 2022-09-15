import os
from typing import Optional
from dotenv import load_dotenv
import requests

load_dotenv(verbose=True)
API_KEY = os.environ.get("API_KEY")


def get_weather_report(city: str, state: Optional[str], country: str) -> dict:
    q = f"{city},{country}"
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={q}&APPID={API_KEY}"
    resp = requests.get(URL)
    resp.raise_for_status()
    return resp.json()
