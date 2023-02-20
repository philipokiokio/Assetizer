from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.database import db_engine
from src.assets import models, route

app: FastAPI = FastAPI()
models.Base.metadata.create_all(bind=db_engine)

origins: list = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(route.asset_router)


@app.get("/", status_code=200)
def server_root() -> dict:
    return {
        "message": "Hello, I am Hope the Server for the Assetizer Project",
        "doc": "/docs/",
    }
