from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# -------- CONEXIÓN DB --------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------- ROOT --------
@app.get("/")
def inicio():
    return {"mensaje": "API sistema de vuelos funcionando"}

# -------- PASAJEROS --------
@app.post("/pasajeros")
def crear_pasajero(pasajero: schemas.PasajeroCreate, db: Session = Depends(get_db)):
    return crud.crear_pasajero(db, pasajero)

@app.get("/pasajeros/{id}")
def historial_pasajero(id: int, db: Session = Depends(get_db)):
    return db.query(models.Reserva).filter(models.Reserva.id_pasajero == id).all()

# -------- RESERVAS --------
@app.post("/reservas")
def crear_reserva(reserva: schemas.ReservaCreate, db: Session = Depends(get_db)):
    return crud.crear_reserva(db, reserva)

# -------- VUELOS --------
@app.post("/vuelos")
def crear_vuelo(vuelo: schemas.VueloCreate, db: Session = Depends(get_db)):
    return crud.crear_vuelo(db, vuelo)

@app.get("/vuelos")
def listar_vuelos(db: Session = Depends(get_db)):
    return db.query(models.Vuelo).all()

@app.get("/vuelos/fecha")
def buscar_por_fecha(fecha: str, db: Session = Depends(get_db)):
    return db.query(models.Vuelo).filter(models.Vuelo.fecha_salida >= fecha).all()

@app.get("/vuelos/aerolinea/{id}")
def vuelos_por_aerolinea(id: int, db: Session = Depends(get_db)):
    return db.query(models.Vuelo).filter(models.Vuelo.id_aerolinea == id).all()

@app.get("/vuelos/ciudad")
def buscar_por_ciudad(ciudad: str, db: Session = Depends(get_db)):
    return db.query(models.Vuelo).join(
        models.Aeropuerto, models.Vuelo.id_origen == models.Aeropuerto.id_aeropuerto
    ).filter(models.Aeropuerto.ciudad == ciudad).all()

# -------- TIQUETES --------
@app.post("/tiquetes")
def agregar_tiquete(id_reserva: int, id_vuelo: int, asiento: str, precio: float, db: Session = Depends(get_db)):
    return crud.agregar_tiquete(db, id_reserva, id_vuelo, asiento, precio)