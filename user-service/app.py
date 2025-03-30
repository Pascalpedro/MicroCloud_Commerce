from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def get_users():
    return jsonify({"users": ["Pedro", "Pascal"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
