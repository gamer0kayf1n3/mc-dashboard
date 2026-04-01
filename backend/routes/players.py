import os

from flask import Blueprint, jsonify, request
import subprocess
import mcrcon
import configload

config = configload.Config()

players_bp = Blueprint('players', __name__, url_prefix='/api')

@players_bp.route('/players', methods=['GET'])
def get_players():
    players = []
    #try:
    with mcrcon.MCRcon("localhost", config.RCON_PASSWORD, config.RCON_PORT) as mcr:
        response = mcr.command("list")
        players = response.strip().split(": ")[-1].split(", ") if ": " in response else []
    return jsonify({'players': players}), 200
    #except Exception as e:
    #    return jsonify({'error': str(e)}), 500