import fastapi
from fastapi import Depends
from models.location import Location
from services import weather_report
from app_cache.weather_cache import set_weather_cache, get_cached_weather

router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
async def weather_api(loc: Location = Depends()):
    weather = get_cached_weather(loc.city, loc.country)
    if weather:
        return weather
    weather = await weather_report.get_weather_report_async(loc.city, loc.country)
    set_weather_cache(loc.city, loc.country,weather)
    return weather
