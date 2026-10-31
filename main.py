from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import sqlite3
from datetime import datetime, timedelta

from db import create_database
from fraud_detection import get_base_amount, get_daily_limit, detect_fraud

app = FastAPI()

create_database()


# Database connection
def connect():
    return sqlite3.connect("fraudalert.db")


# Open website
@app.get("/")
def home():
    return FileResponse("index.html")


@app.get("/style.css")
def css():
    return FileResponse("style.css")


# Input models
class Customer(BaseModel):
    name: str
    category: str


class Transaction(BaseModel):
    customer_id: int
    amount: float


# Register customer
@app.post("/customer")
def add_customer(data: Customer):

    conn = connect()
    cur = conn.cursor()

    base = get_base_amount(data.category)

    cur.execute("""
        INSERT INTO customers (name, account_type, base_amount)
        VALUES (?, ?, ?)
    """, (data.name, data.category, base))

    conn.commit()
    conn.close()

    return {"message": "Customer registered successfully"}


# Get customers
@app.get("/customers")
def get_customers():

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM customers")
    data = cur.fetchall()

    conn.close()

    return [
        {"id": c[0], "name": c[1]}
        for c in data
    ]


# Check transaction
@app.post("/transaction")
def check_transaction(data: Transaction):

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT base_amount, account_type FROM customers WHERE id=?",
        (data.customer_id,)
    )

    customer = cur.fetchone()

    if customer is None:
        conn.close()
        return {"message": "Customer not found"}

    base = customer[0]
    category = customer[1]

    now = datetime.now()

    today = now.strftime("%Y-%m-%d")

    five_minutes = (
        now - timedelta(minutes=5)
    ).strftime("%Y-%m-%d %H:%M:%S")

    # Calculate daily transaction amount
    cur.execute("""
        SELECT SUM(amount) FROM transactions
        WHERE customer_id=? AND date(created_at)=?
    """, (data.customer_id, today))

    daily_total = cur.fetchone()[0] or 0

    # Count recent transactions
    cur.execute("""
        SELECT COUNT(*) FROM transactions
        WHERE customer_id=? AND created_at>=?
    """, (data.customer_id, five_minutes))

    count = cur.fetchone()[0]

    limit = get_daily_limit(category)

    # Detect risk and reason
    risk, reason = detect_fraud(
        data.amount,
        base,
        daily_total,
        limit,
        count
    )

    # Save transaction
    cur.execute("""
        INSERT INTO transactions
        (customer_id, amount, risk_level, reason, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data.customer_id,
        data.amount,
        risk,
        reason,
        now.strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()

    return {
        "risk_level": risk,
        "reason": reason
    }


# Transaction history
@app.get("/transactions")
def get_transactions():

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT transactions.id, customers.name,
        transactions.amount, transactions.risk_level,
        transactions.reason
        FROM transactions
        JOIN customers
        ON transactions.customer_id = customers.id
        ORDER BY transactions.id DESC
    """)

    data = cur.fetchall()

    conn.close()

    return [
        {
            "id": t[0],
            "name": t[1],
            "amount": t[2],
            "risk": t[3],
            "reason": t[4]
        }
        for t in data
    ]