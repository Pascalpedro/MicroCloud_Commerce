import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    create_table()  # Create table before running app
    app.run(host="0.0.0.0", port=5001, debug=True)
