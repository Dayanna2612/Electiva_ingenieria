from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, TIMESTAMP
from database import Base

class Aerolinea(Base):
    __tablename__ = "aerolineas"

    id_aerolinea = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    pais_origen = Column(String(100))


class Aeropuerto(Base):
    __tablename__ = "aeropuertos"

    id_aeropuerto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    ciudad = Column(String(100))
    pais = Column(String(100))


class Vuelo(Base):
    __tablename__ = "vuelos"

    id_vuelo = Column(Integer, primary_key=True, index=True)
    id_aerolinea = Column(Integer, ForeignKey("aerolineas.id_aerolinea"))
    id_origen = Column(Integer, ForeignKey("aeropuertos.id_aeropuerto"))
    id_destino = Column(Integer, ForeignKey("aeropuertos.id_aeropuerto"))
    fecha_salida = Column(TIMESTAMP, nullable=False)
    fecha_llegada = Column(TIMESTAMP, nullable=False)
    precio_base = Column(DECIMAL(10, 2), nullable=False)


class Pasajero(Base):
    __tablename__ = "pasajeros"

    id_pasajero = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100))
    documento = Column(String(50))
    telefono = Column(String(20))


class Reserva(Base):
    __tablename__ = "reservas"

    id_reserva = Column(Integer, primary_key=True, index=True)
    id_pasajero = Column(Integer, ForeignKey("pasajeros.id_pasajero"))
    total = Column(DECIMAL(10, 2), default=0)


class Tiquete_Aereo(Base):
    __tablename__ = "tiquetes_aereos"

    id_tiquete = Column(Integer, primary_key=True, index=True)
    id_vuelo = Column(Integer, ForeignKey("vuelos.id_vuelo"))
    id_reserva = Column(Integer, ForeignKey("reservas.id_reserva"))
    asiento = Column(String(10))
    clase = Column(String(50))
    precio = Column(DECIMAL(10, 2))
    estado = Column(String(50), default="Disponible")