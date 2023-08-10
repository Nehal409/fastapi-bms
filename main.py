from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastsocket import create_socketio_app

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_socketio_app(app)

