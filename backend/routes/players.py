from flask import Blueprint

players_bp = Blueprint('players', __name__)

@players_bp.route('/players', methods=['GET'])
def get_players():
    return {"message": "List of players"}