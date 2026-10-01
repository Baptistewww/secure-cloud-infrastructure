import os

import psycopg
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)


def get_db_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        sslmode="require",
        connect_timeout=10
    )


@app.route("/")
def home():
    return "Secure Cloud Infrastructure Project"


@app.route("/db")
def database_test():
    try:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1;")
                cursor.fetchone()

        return "Database connection successful!"

    except Exception:
        return "Database connection failed.", 500


if __name__ == "__main__":
    app.run(debug=True)