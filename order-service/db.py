import psycopg2
import os

def get_db_connection():
    return psycopg2.connect(
        host="order-db",
        database="ordersdb",
        user="postgres",
        password="password"
    )
