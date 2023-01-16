import requests
from fastapi import FastAPI

uriSchema = "http://"
host = "localhost"
port = "9358"
apiUri = f"{uriSchema}{host}:{port}"
app = FastAPI()

from pydantic import BaseModel


class ReserveArguments(BaseModel):
    seconds: int


@app.get("/")
async def root():
    return {"name": "agones-gameserver-api", "status": "operational"}


@app.post("/ready")
async def ready():
    response = requests.post(f"{apiUri}/ready", data={})
    return response.json()


@app.post("/health")
async def health():
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{apiUri}/health", headers=headers, data="{}")
    return response.json()


@app.post("/reserve")
async def reserve(reserveArguments: ReserveArguments):
    print(reserveArguments.seconds)
    headers = {"Content-Type": "application/json"}
    json = {"seconds": reserveArguments.seconds}
    response = requests.post(f"{apiUri}/reserve", headers=headers, json=json)
    return response.json()


@app.post("/allocate")
async def allocate():
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{apiUri}/allocate", headers=headers, data="{}")
    return response.json()


@app.post("/shutdown")
async def shutdown():
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{apiUri}/shutdown", headers=headers, data={})
    return response.json()


@app.get("/gameserver")
async def gameserver():
    response = requests.get(f"{apiUri}/gameserver")
    return response.json()
