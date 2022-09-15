import fastapi
from fastapi import Depends
from models.location import Location
from services import weather_report

router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
def weather_api(loc: Location = Depends()):
    return weather_report.get_weather_report(loc.city, loc.state, loc.country)
