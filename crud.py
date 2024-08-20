# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def get_worker(db: Session, worker_id: int):
    return db.query(models.Worker).filter(models.Worker.id == worker_id).first()

def get_workers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Worker).offset(skip).limit(limit).all()

def create_worker(db: Session, worker: schemas.WorkerCreate):
    db_worker = models.Worker(name=worker.name, position=worker.position)
    db.add(db_worker)
    db.commit()
    db.refresh(db_worker)
    return db_worker