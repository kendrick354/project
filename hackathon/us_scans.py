# app/us_scans.py
from io import BytesIO
from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from datetime import date
import gridfs
from fastapi.responses import StreamingResponse
from pymongo import MongoClient
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Pydantic base model class used to integrate with MongoDB 
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object ID")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class USScan(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    US_scan_ID: int
    Coordinates: str
    Scan_Date: str
    Diagnosis: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, doc):
        return cls(
            id=doc.get("_id"),
            US_scan_ID=doc.get("US scan ID"),
            Coordinates=doc.get("Coordinates"),
            Scan_Date=doc.get("Scan Date"),
            Diagnosis=doc.get("Diagnosis")
        )



MONGO_DETAILS = "mongodb+srv://admin:ZmQvsr76Dkk3oyPU@cluster0.92giasc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_DETAILS)
db = client["patient_data"]
fs = gridfs.GridFS(db)
us_scans_collection = db["US_scans"]

router = APIRouter()
app = FastAPI()

# Get all scans 
@router.get("/", response_model=List[USScan])
def get_all_us_scans():
    cursor = us_scans_collection.find()
    scans = [USScan.from_mongo(scan) for scan in cursor]
    return scans

@router.get("/id/{scan_id}", response_model=USScan)
def get_us_scan_by_id(scan_id: str):
    logger.info(f"Fetching US scan with ID {scan_id}")
    try:
        # Cast scan_id to integer
        scan_id_int = int(scan_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid scan ID format")

    # Query the database with the integer ID
    scan = us_scans_collection.find_one({"US scan ID": scan_id_int})
    if scan:
        return USScan.from_mongo(scan)
    raise HTTPException(status_code=404, detail="US scan not found")
# Get image by image ID
@router.get("/images/{image_id}")
def get_image(image_id: str):
    try:
        logger.info(f"Fetching image with ID {image_id}")
        filename = image_id + ".png"
        # Fetch the image from GridFS
        file = fs.find_one({"filename": filename})
        content = file.read()
        return StreamingResponse(BytesIO(content), media_type="image/png")
    except Exception as e:
        logger.error(f"Error fetching image: {e}")
        raise HTTPException(status_code=404, detail="Image not found")

app.include_router(router, prefix="/us_scans", tags=["US Scans"])
