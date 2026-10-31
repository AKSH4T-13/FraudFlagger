import sqlite3

def create_database():

    conn = sqlite3.connect("fraudalert.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            account_type TEXT,
            base_amount REAL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            amount REAL,
            risk_level TEXT,
            created_at TEXT
        )
    """)

    # Add timestamp to existing database
    try:
        cur.execute("ALTER TABLE transactions ADD COLUMN created_at TEXT")
    except sqlite3.OperationalError:
        pass

    conn.commit()
    conn.close()