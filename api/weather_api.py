import fastapi

router = fastapi.APIRouter()


@router.get("/api/weather")
def weather_api():
    return "test"
