import uvicorn
import fastapi
api = fastapi.FastAPI()

templates = Jinja2Templates("templates")

@api.get("/")
def index():
    return "Hello Weather App!"



if __name__ == "__main__":
    uvicorn.run(api,port=8000,host="0.0.0.0")