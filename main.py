from fastapi import FastAPI
from app.routers import patients, appointments

app = FastAPI()

app.include_router(patients.router, prefix="/patients", tags=["Patients"])
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])
