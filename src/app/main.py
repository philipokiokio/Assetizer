from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.daabase import DB_URL

app: FastAPI = FastAPI()


origins: list = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=200)
def server_root() -> dict:
    return {
        "message": "Hello, I am Hope the Server for the Assetizer Project",
        "doc": "/docs/",
    }
