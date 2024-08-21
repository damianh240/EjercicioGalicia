# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import engine, SessionLocal, Base

app = FastAPI()

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def index():
    return RedirectResponse(url="/docs")
    #return {"message" : "Ejercicio Galicia"}

@app.post("/workers/", response_model=schemas.Worker)
def create_worker(worker: schemas.WorkerCreate, db: Session = Depends(get_db)):
    return crud.create_worker(db=db, worker=worker)

@app.get("/workers/", response_model=list[schemas.Worker])
def read_workers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    workers = crud.get_workers(db, skip=skip, limit=limit)
    return workers

@app.get("/workers/{worker_id}", response_model=schemas.Worker)
def read_worker(worker_id: int, db: Session =
                 Depends(get_db)):
    worker = crud.get_worker(db, worker_id=worker_id)
    if worker is None:
        raise HTTPException(status_code=404, detail="Worker not found")
    return worker

@app.put("/workers/{worker_id}", response_model=schemas.Worker)
def update_worker(worker_id: int, worker_update: schemas.WorkerUpdate, db: Session = Depends(get_db)):
    db_worker = crud.update_worker(db=db, worker_id=worker_id, worker_update=worker_update)
    if db_worker is None:
        raise HTTPException(status_code=404, detail="Worker not found")
    return db_worker

# Ruta para eliminar un trabajador
@app.delete("/workers/{worker_id}", response_model=schemas.Worker)
def delete_worker(worker_id: int, db: Session = Depends(get_db)):
    db_worker = crud.delete_worker(db, worker_id=worker_id)
    if db_worker is None:
        raise HTTPException(status_code=404, detail="Worker not found")
    return db_worker