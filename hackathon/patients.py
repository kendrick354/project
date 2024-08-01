from typing import List, Optional
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from bson import ObjectId
from pymongo import MongoClient

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

# Patient Pydantic model
class Patient(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    patient_id: int
    patient_name: str
    age: int
    height: int
    weight: int
    history: str
    scan_id: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, doc):
        return cls(
            id=doc.get("_id"),
            patient_id=doc.get("Patient ID"),
            patient_name=doc.get("Patient Name"),
            age=doc.get("Age"),
            height=doc.get("Height (cm)"),
            weight=doc.get("Weight (kg)"),
            history=doc.get("History of breast cancer"),
            scan_id=doc.get("US scan ID")
        )

MONGO_DETAILS = "mongodb+srv://admin:ZmQvsr76Dkk3oyPU@cluster0.92giasc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_DETAILS)

db = client["patient_data"]
patients_collection = db["patients"]

router = APIRouter()

# Get all patients 
@router.get("/", response_model=List[Patient])
def get_all_patients():
    cursor = patients_collection.find()
    scans = [Patient.from_mongo(scan) for scan in cursor]
    return scans

# Get patient by patient ID
@router.get("/{patient_id}", response_model=List[Patient])
def get_patient_by_id(patient_id: int):
    patient = []
    ans = patients_collection.find_one({"Patient ID": patient_id})
    if ans:
        patient.append(Patient.from_mongo(ans))
        return patient
    raise HTTPException(status_code=404, detail="Patient not found")

# Get patient by patient name
@router.get("/patient_name/{patient_name}", response_model=List[Patient])
def get_patient_by_name(patient_name: str):
    patient_name = patient_name.replace("_", " ")
    patients = []
    for patient in patients_collection.find({"Patient Name": {"$regex": patient_name, "$options": "i"}}):
        patients.append(Patient.from_mongo(patient))
    if not patients:
        raise HTTPException(status_code=404, detail="No patients found")
    return patients

# # Add patient to the collection of patients
# @router.post("/", response_model=Patient)
# def create_patient(patient: Patient):
#     patient_dict = jsonable_encoder(patient)
#     new_patient = patients_collection.insert_one(patient_dict)
#     created_patient = patients_collection.find_one({"_id": new_patient.inserted_id})
#     return Patient.from_mongo(created_patient)

# Update patient by ID
@router.put("/id/{id}", response_model=Patient)
def update_patient(id: str, patient: Patient):
    patient_dict = jsonable_encoder(patient)
    update_result = patients_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": patient_dict}
    )

    if update_result.modified_count == 1:
        updated_patient = patients_collection.find_one({"_id": ObjectId(id)})
        if updated_patient:
            return Patient.from_mongo(updated_patient)

    existing_patient = patients_collection.find_one({"_id": ObjectId(id)})
    if existing_patient:
        return Patient.from_mongo(existing_patient)
    
    raise HTTPException(status_code=404, detail="Patient not found")

# # Delete patient by ID
# @router.delete("/id/{id}")
# def delete_patient(id: str):
#     delete_result = patients_collection.delete_one({"_id": ObjectId(id)})
#     if delete_result.deleted_count == 1:
#         return {"detail": "Patient deleted"}
#     raise HTTPException(status_code=404, detail="Patient not found")
