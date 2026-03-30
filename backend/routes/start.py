import os

from flask import Blueprint, jsonify, request
import subprocess
import mcrcon
import configload

config = configload.Config()

startup_bp = Blueprint('startup', __name__)

@startup_bp.route('/api/startup', methods=['GET', 'POST'])
def startup():
    if request.method == 'POST':
        if request.json and request.json.get('action') == 'start':
                subprocess.Popen(['bash', f'{os.path.dirname(__file__)}/../mcstart.sh'])
                return jsonify({'status': 'Minecraft server starting...'}), 200
        elif request.json and request.json.get('action') == 'stop':
            try:
                with mcrcon.MCRcon("localhost", config.RCON_PASSWORD, config.RCON_PORT) as mcr:
                    mcr.command("stop")
                return jsonify({'status': 'Minecraft server stopping...'}), 200
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        else:
            return jsonify({'error': 'Invalid action'}), 400
    else:
        result = subprocess.run(["systemctl", "-q", "is-active", 'minecraft.service'])
        if result.returncode == 0:
            return jsonify({'status': 'running'}), 200
        else:
            return jsonify({'status': 'stopped'}), 200
    