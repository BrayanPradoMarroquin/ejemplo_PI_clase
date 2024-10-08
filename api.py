from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def api():
    
    return jsonify({'message': 'Hello, World!'})

@app.route('/datos', methods=['POST'])
def datos():
    data = request.json
    print(data)
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')