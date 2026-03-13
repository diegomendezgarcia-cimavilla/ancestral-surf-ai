import sqlite3

DB="data/sensations.db"

def init_db():

    conn=sqlite3.connect(DB)

    c=conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS sensations(
    date TEXT,
    energy INTEGER,
    mood INTEGER,
    stress INTEGER,
    sleep INTEGER,
    surf INTEGER,
    cannabis INTEGER,
    fishing INTEGER,
    food INTEGER,
    notes TEXT
    )
    """)

    conn.commit()

    conn.close()


def insert_data(data):

    conn=sqlite3.connect(DB)

    c=conn.cursor()

    c.execute("""
    INSERT INTO sensations VALUES(
    date('now'),
    ?,?,?,?,?,?,?,?,?
    )
    """,data)

    conn.commit()

    conn.close()


def load_data():

    conn=sqlite3.connect(DB)

    c=conn.cursor()

    rows=c.execute("SELECT * FROM sensations").fetchall()

    conn.close()

    return rows
