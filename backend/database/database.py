# This module is for the database connection and connection helper methods

import psycopg
import os

# Return a connection to the database
def get_connection() -> psycopg.Connection:
    print("DB_NAME =", os.getenv("DB_NAME"))
    print("DB_USER =", os.getenv("DB_USER"))
    print("DB_HOST =", os.getenv("DB_HOST"))
    print("DB_PORT =", os.getenv("DB_PORT"))

    return psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )

# ========================== fetch operations =================================

# Fetch one or multiple results
def fetch_results(conn, query, params = None):
    with conn.cursor() as cur:
        cur.execute(query, params or ())
        return cur.fetchall()
    
# Only fetch one result
def fetch_one_result(conn, query, params = None):
    with conn.cursor() as cur:
        cur.execute(query, params or ())
        return cur.fetchone()
    
# =============================================================================