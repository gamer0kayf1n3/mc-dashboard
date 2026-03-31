from flask import Blueprint

players_bp = Blueprint('players', __name__, url_prefix='/api')

@players_bp.route('/players', methods=['GET'])
def get_players():
    return {"message": "List of players"}