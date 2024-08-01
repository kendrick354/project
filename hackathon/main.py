from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.us_scans import router as us_scans_router
from app.patients import router as patients_router
from pydantic import BaseModel, Field
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from datetime import date
import gridfs
from fastapi.responses import StreamingResponse
from pymongo import MongoClient
import logging
from io import BytesIO

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Define allowed origins
origins = [
    "http://localhost:3000",  # Ensure this matches the port your React app is running on
    "http://127.0.0.1:3000",  # Include this if you access the app using this URL
    "https://localhost:5173",  # Include this if needed
    "http://localhost:5173"    # Include this if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_DETAILS = "mongodb+srv://admin:ZmQvsr76Dkk3oyPU@cluster0.92giasc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_DETAILS)
db = client["patient_data"]
us_scans_collection = db["US_scans"]
fs = gridfs.GridFS(db)

@app.get("/")
def read_root():
    return {"Ping": "pong"}



app.include_router(us_scans_router, prefix="/us_scans", tags=["us_scans"])
app.include_router(patients_router, prefix="/patients", tags=["patients"])
