from flask import Flask, jsonify
import os
import sys


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

print(app.config, file=sys.stderr)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
