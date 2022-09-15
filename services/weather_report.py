import os
from typing import Optional
from dotenv import load_dotenv
import httpx

load_dotenv(verbose=True)
API_KEY = os.environ.get("API_KEY")


async def get_weather_report_async(city: str, country: str) -> dict:
    q = f"{city},{country}"
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={q}&APPID={API_KEY}&units=metric"
    async with httpx.AsyncClient() as client:
        resp = await client.get(URL)
        resp.raise_for_status()
    return resp.json()
