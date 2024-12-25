import psycopg2
from bot.config import DB_PARAMS

def get_connection():
    return psycopg2.connect(**DB_PARAMS)

def close_connection(connection):
    if connection:
        connection.close()
