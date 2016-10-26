from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/get_image', methods=['POST'])
def get_image():
    return 'Get Image'

# app.run(host='0.0.0.0', debug=True, threaded=True)

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)