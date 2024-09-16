import sqlite3
from flask import g

DATABASE = 'database.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def create_tables():
    db = get_db()
    cursor = db.cursor()

    # Manual Page State Tablosu
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS manual_page_state (
            user_id INTEGER PRIMARY KEY,
            selected_duration INTEGER
        )
    ''')

    # Settings Page State Tablosu
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS settings_page_state (
            user_id INTEGER PRIMARY KEY,
            valve_opening_amount INTEGER,
            default_open INTEGER
        )
    ''')

    # Irrigation Timer State Tablosu
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS irrigation_timer_state (
            user_id INTEGER PRIMARY KEY,
            selected_date TEXT,
            selected_time TEXT,
            selected_hours INTEGER,
            selected_minutes INTEGER,
            selected_duration INTEGER
        )
    ''')

    db.commit()
