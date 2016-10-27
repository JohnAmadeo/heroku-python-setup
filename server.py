from flask import Flask, request, jsonify
import os
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/hi')
def hi():
    return 'Hi'

@app.route('/get_image', methods=['POST'])
def get_image():
    return 'Get Image'

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)