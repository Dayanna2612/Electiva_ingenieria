import models

# -------- PASAJERO --------
def crear_pasajero(db, pasajero):
    nuevo = models.Pasajero(**pasajero.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# -------- RESERVA --------
def crear_reserva(db, reserva):
    nueva = models.Reserva(id_pasajero=reserva.id_pasajero, total=0)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

# -------- VUELO --------
def crear_vuelo(db, vuelo):
    nuevo = models.Vuelo(**vuelo.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# -------- TIQUETES --------
def asiento_ocupado(db, id_vuelo, asiento):
    return db.query(models.Tiquete_Aereo).filter(
        models.Tiquete_Aereo.id_vuelo == id_vuelo,
        models.Tiquete_Aereo.asiento == asiento
    ).first()

def agregar_tiquete(db, id_reserva, id_vuelo, asiento, precio):
    if asiento_ocupado(db, id_vuelo, asiento):
        raise Exception("Asiento ya ocupado")

    tiquete = models.Tiquete_Aereo(
        id_vuelo=id_vuelo,
        id_reserva=id_reserva,
        asiento=asiento,
        precio=precio,
        estado="Reservado"
    )

    db.add(tiquete)

    reserva = db.query(models.Reserva).get(id_reserva)
    reserva.total += precio

    db.commit()
    return tiquete