# services/users/project/__init__.py
from flask import Flask, jsonify

app = Flask(__name__)

app.config.from_object('project.config.DevelopmentConfig') # set config

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!!'
    })
