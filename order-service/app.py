from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def get_orders():
    return jsonify({"orders": ["Order1", "Order2"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
