from flask import Blueprint, request, jsonify
from model.nivel_ansiedad import NivelAnsiedad
from utils.db import db

nivelansiedades = Blueprint('nivelansiedades', __name__)

@nivelansiedades.route('/nivelansiedades/v1', methods=['GET'])
def get_mensaje():
    result = {"data": 'Hola, NivelAnsiedades'}
    return jsonify(result)

@nivelansiedades.route('/nivelansiedades/v1/listar', methods=['GET'])
def listar_nivelansiedades():
    niveles = NivelAnsiedad.query.all()
    result = {
        "data": [nivel.__dict__ for nivel in niveles],
        "status_code": 200,
        "msg": "Se recuperó la lista de Niveles de Ansiedad sin inconvenientes"
    }
    for nivel in result["data"]:
        nivel.pop('_sa_instance_state', None)  # Eliminar metadata de SQLAlchemy
    return jsonify(result), 200

@nivelansiedades.route('/nivelansiedades/v1/agregar', methods=['POST'])
def agregar_nivelansiedad():
    data = request.json
    nuevo_nivel = NivelAnsiedad(
        descripcion=data['descripcion']
    )
    db.session.add(nuevo_nivel)
    db.session.commit()
    return jsonify({
        "status_code": 201,
        "msg": "Nivel de Ansiedad agregado exitosamente",
        "data": nuevo_nivel.__dict__
    }), 201

@nivelansiedades.route('/nivelansiedades/v1/actualizar/<int:id>', methods=['PUT'])
def actualizar_nivelansiedad(id):
    data = request.json
    nivel = NivelAnsiedad.query.get_or_404(id)
    nivel.descripcion = data.get('descripcion', nivel.descripcion)
    db.session.commit()
    return jsonify({
        "status_code": 200,
        "msg": "Nivel de Ansiedad actualizado exitosamente",
        "data": nivel.__dict__
    }), 200

@nivelansiedades.route('/nivelansiedades/v1/eliminar/<int:id>', methods=['DELETE'])
def eliminar_nivelansiedad(id):
    nivel = NivelAnsiedad.query.get_or_404(id)
    db.session.delete(nivel)
    db.session.commit()
    return jsonify({
        "status_code": 200,
        "msg": "Nivel de Ansiedad eliminado exitosamente"
    }), 200
