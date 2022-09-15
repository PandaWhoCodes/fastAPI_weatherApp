import fastapi
from fastapi import Depends
from models.location import Location
from services import weather_report

router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
async def weather_api(loc: Location = Depends()):
    return await weather_report.get_weather_report_async(
        loc.city, loc.state, loc.country
    )
