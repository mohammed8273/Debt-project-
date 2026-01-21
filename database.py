    # database.py
import sqlite3

DB_NAME = "Debts.db"

def connect():
    """open connect"""
    return sqlite3.connect(DB_NAME)

def create_table():
    """إcreate ttables"""
    conn = connect()
    c = conn.cursor()
    
    
    c.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT,
        address TEXT
    )
    """)
    
  
    c.execute("""
    CREATE TABLE IF NOT EXISTS debts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        amount REAL,
        note TEXT,
        date TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers (id)
    )
    """)
    
    conn.commit()
    conn.close()

    

    

    








