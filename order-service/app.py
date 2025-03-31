from flask import Flask, jsonify
import psycopg2
from db import get_db_connection

app = Flask(__name__)

@app.route('/orders')
def get_orders():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders;")
    orders = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify({"orders": orders})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
