from msilib.schema import Directory
import uvicorn
import fastapi
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.staticfiles import StaticFiles

from api import weather_api
from views import home

api = fastapi.FastAPI()
api.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates("templates")


def configure_routing():
    api.include_router(home.router)
    api.include_router(weather_api.router)


def configure():
    configure_routing()


if __name__ == "__main__":
    configure()
    uvicorn.run(api, port=8000, host="0.0.0.0")

