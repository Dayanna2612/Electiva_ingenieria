from pydantic import BaseModel, field_validator
from datetime import datetime

# -------- PASAJERO --------
class PasajeroCreate(BaseModel):
    nombre: str
    apellido: str
    documento: str
    telefono: str

# -------- RESERVA --------
class ReservaCreate(BaseModel):
    id_pasajero: int

# -------- VUELO --------
class VueloCreate(BaseModel):
    id_aerolinea: int
    id_origen: int
    id_destino: int
    fecha_salida: datetime
    fecha_llegada: datetime
    precio_base: float

    @field_validator("fecha_llegada")
    def validar_fechas(cls, v, values):
        if "fecha_salida" in values and v <= values["fecha_salida"]:
            raise ValueError("La llegada debe ser mayor que la salida")
        return v

    @field_validator("precio_base")
    def validar_precio(cls, v):
        if v <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        return v