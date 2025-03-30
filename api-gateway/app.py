import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users')
def users():
    response = requests.get("http://user-service:5001")
    return response.json()

@app.route('/orders')
def orders():
    response = requests.get("http://order-service:5002")
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
