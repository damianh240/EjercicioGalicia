# app/crud.py
from sqlalchemy.orm import Session
import models
import schemas

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

def update_worker(db: Session,worker_id: int, worker_update: schemas.WorkerUpdate):
    db_worker = db.query(models.Worker).filter(models.Worker.id == worker_id).first()
    if not db_worker:
        return None
    update_data = worker_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_worker, key, value)
    db.commit()
    db.refresh(db_worker)
    return db_worker

def delete_worker(db: Session, worker_id: int):
    db_worker = db.query(models.Worker).filter(models.Worker.id == worker_id).first()
    if not db_worker:
        return None
    #Elimina el trabajado de la base
    db.delete(db_worker)

    #Guarda los cambios en la DB
    db.commit()
    return db_worker   
