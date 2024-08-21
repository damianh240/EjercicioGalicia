# app/schemas.py
from pydantic import BaseModel
from typing import Optional

class WorkerBase(BaseModel):
    name: str
    position: str

class WorkerUpdate(BaseModel):
    name: Optional[str] = None
    position: Optional[str] = None

    class Config:
        orm_mode = True

class WorkerCreate(WorkerBase):
    pass

class Worker(WorkerBase):
    id: int

    class Config:
        orm_mode = True