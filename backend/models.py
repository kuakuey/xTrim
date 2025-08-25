from database import db

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    telefono = db.Column(db.String(20))
    cedula = db.Column(db.String(20), unique=True)

class Consumo(db.Model):
    __tablename__ = "consumos"
    id = db.Column(db.Integer, primary_key=True)
    saldo = db.Column(db.Float)
    datos = db.Column(db.Float)
    minutos = db.Column(db.Integer)

    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
