"""
Tee basic functionality ofther databast.I imports the libraries questionary, sqlite3 and hashlib.
"""
import questionary
import sqlite3
import hashlib

# THIS PART LAUNCHES THE DATABASE IF IT NOT ALREADY EXISTS.
def launch_database():
    """
    Launch of the database if it not already exists.
    The database consists of three tables: users, habits, and progress.
    """
    from os.path import join, dirname, abspath
    db_path = join(dirname(abspath(__file__)), 'main_db.db')

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            firstname text,
            lastname text,
            username text PRIMARY KEY,
            password text,
            age text,
            sex text,
            height real,
            weight real,
            race text,
            occupation text,
            geographical_area text,
            medical_history text
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            habit_name text,
            owner text, 
            category text,
            periodicity text,
            datetime_of_creation datetime
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            habit_name text,
            periodicity text, 
            owner text, 
            datetime_of_completion datetime
        )
    """)
    conn.commit()
    conn.close()