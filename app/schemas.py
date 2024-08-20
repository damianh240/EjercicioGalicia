# app/schemas.py
from pydantic import BaseModel

class WorkerBase(BaseModel):
    name: str
    position: str

class WorkerCreate(WorkerBase):
    pass

class Worker(WorkerBase):
    id: int

    class Config:
        orm_mode = True