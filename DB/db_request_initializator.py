import sqlite3
from datetime import datetime
from classes.constants import DB_REQUEST

def get_connection():
    return sqlite3.connect(DB_REQUEST)

def create_database():
    """
    Crea la base de datos y la tabla requests con restricción en el campo status.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id TEXT NOT NULL,
                owner_ID TEXT NOT NULL,
                create_date TEXT NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('open', 'close')),
                description TEXT,
                title TEXT NOT NULL
            )
        """)

def insert_initial_requests():
    """
    Inserta 6 entradas iniciales en la tabla requests.
    Cada cuenta tendrá 2 solicitudes asociadas.
    """
    accounts = [
        ("1", "Ad_01"),
        ("2", "Em_01"),
        ("3", "Cl_01"),
        ("4", "Cl_02"),
    ]

    requests_data = []
    for acc_id, owner in accounts:
        for i in range(1, 3):
            requests_data.append((
                acc_id,
                owner,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "open" if i % 2 == 0 else "close",
                f"Descripción de la solicitud {i} para {owner}",
                f"Título {i} de {owner}"
            ))

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.executemany("""
            INSERT INTO requests (account_id, owner_ID, create_date, status, description, title)
            VALUES (?, ?, ?, ?, ?, ?)
        """, requests_data)
        conn.commit()

if __name__ == "__main__":
    create_database()
    insert_initial_requests()
