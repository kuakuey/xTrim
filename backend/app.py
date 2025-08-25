from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import desc
from database import db, SQLALCHEMY_DATABASE_URI
from models import Usuario, Consumo

app = Flask(__name__)
CORS(app)  # 👈 habilita CORS para todas las rutas

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def root():
    return "API para proyecto Xtrim"

@app.route("/consumo/<cedula>")
def get_consumo(cedula):
    # 1. Buscar usuario por cédula
    user = Usuario.query.filter_by(cedula=cedula).first()
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    
    # 2. Buscar consumo
    consumo = Consumo.query.filter_by(usuario_id=user.id).order_by(desc(Consumo.id)).first()
    if not consumo:
        return jsonify({"error": "Consumo no encontrado para este usuario"}), 404
    
    # 3. Construir respuesta
    resultado = {
        "datos": {
            "id": user.id,
            "nombre": user.name,
            "cedula": user.cedula,
            "telefono": user.telefono
        },
        "consumo": {
            "saldo": consumo.saldo,
            "datos": consumo.datos,
            "minutos": consumo.minutos
        }
    }

    return jsonify(resultado), 200

if __name__ == '__main__':
    app.run(debug=True)