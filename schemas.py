from pydantic import BaseModel

class AppointmentBase(BaseModel):
    date: str
    reason: str

class AppointmentCreate(AppointmentBase):
    patient_id: int

class Appointment(AppointmentBase):
    id: int
    patient_id: int

    class Config:
        orm_mode = True


class PatientBase(BaseModel):
    name: str
    email: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    appointments: list[Appointment] = []

    class Config:
        orm_mode = True
