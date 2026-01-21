# services.py
from database import connect
from datetime import date
from models import Customer, Debt

def add_customer(name, phone, address):
    
    conn = connect()
    c = conn.cursor()
    c.execute(
        "INSERT INTO customers (name, phone, address) VALUES (?, ?, ?)",
        (name, phone, address)
    )
    conn.commit()
    customer_id = c.lastrowid
    conn.close()
    return Customer(customer_id, name, phone, address)

def add_debt(customer_id, amount, note=""):
    
    conn = connect()
    c = conn.cursor()
    today = date.today().isoformat()
    c.execute(
        "INSERT INTO debts (customer_id, amount, note, date) VALUES (?, ?, ?, ?)",
        (customer_id, amount, note, today)
    )
    conn.commit()
    debt_id = c.lastrowid
    conn.close()
    return Debt(debt_id, customer_id, amount, today, note)

def get_all_customers():
    
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT id, name, phone, address FROM customers")
    rows = c.fetchall()
    conn.close()
    return [Customer(*row) for row in rows]

def get_debts_by_customer(customer_id):
    
    conn = connect()
    c = conn.cursor()
    c.execute(
        "SELECT id, customer_id, amount, date, note FROM debts WHERE customer_id=?",
        (customer_id,)
    )
    rows = c.fetchall()
    conn.close()
    return [Debt(*row) for row in rows]