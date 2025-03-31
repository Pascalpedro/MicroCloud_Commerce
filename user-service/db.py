import psycopg2
import os

def get_db_connection():
    return psycopg2.connect(
        host="user-db",
        database="usersdb",
        user="postgres",
        password="password"
    )
