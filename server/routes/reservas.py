from flask import Blueprint, jsonify

reservas_bp = Blueprint('reservas', __name__)

@reservas_bp.route('/reservas', methods=['POST'])
def reserve_seat():
    return jsonify(message="Reserva confirmada!")
