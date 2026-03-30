from flask import Flask, Blueprint
from flask_cors import CORS
import importlib
import os

app = Flask(__name__)
CORS(app)

# Load all routes from the routes folder
routes_dir = 'routes'
for filename in os.listdir(routes_dir):
    if filename.endswith('.py') and filename != '__init__.py':
        module_name = filename[:-3]
        module = importlib.import_module(f'{routes_dir}.{module_name}')
        
        # Dynamically register all Blueprints in the module
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, Blueprint):
                app.register_blueprint(attr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)