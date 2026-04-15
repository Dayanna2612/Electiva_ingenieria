from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db

router = APIRouter()


@router.post("/aerolineas", response_model=schemas.AerolineaResponse)
def crear_aerolinea(aerolinea: schemas.AerolineaCreate, db: Session = Depends(get_db)):
    return crud.crear_aerolinea(db, aerolinea)


@router.get("/aerolineas")
def listar_aerolineas(db: Session = Depends(get_db)):
    return crud.listar_aerolineas(db)


@router.post("/vuelos")
def crear_vuelo(vuelo: schemas.VueloCreate, db: Session = Depends(get_db)):
    return crud.crear_vuelo(db, vuelo)