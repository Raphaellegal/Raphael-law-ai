import sqlite3
import os


DATABASE_PATH = "app/database/raphael.db"


def get_connection():

    os.makedirs(
        "app/database",
        exist_ok=True
    )

    connection = sqlite3.connect(
        DATABASE_PATH,
        timeout=10
    )

    return connection


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            full_name TEXT NOT NULL,

            email TEXT NOT NULL UNIQUE,

            password_hash TEXT NOT NULL,

            category TEXT NOT NULL,

            role TEXT NOT NULL,

            verified INTEGER NOT NULL DEFAULT 0,

            verification_status TEXT NOT NULL DEFAULT 'not_required',

            subscription TEXT NOT NULL DEFAULT 'free'

        )
        """
    )

    connection.commit()

    connection.close()