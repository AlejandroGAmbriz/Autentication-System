import sqlite3
import bcrypt

DB_NAME = "data_base_account.db"

def hash_password(password: str) -> str:
    """
    Genera un hash seguro para la contraseña usando bcrypt.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def create_database():
    """
    Crea la base de datos y la tabla usuarios con restricción en el campo type.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            type TEXT NOT NULL CHECK(type IN ('admin', 'empleado', 'cliente'))
        )
    """)

    conn.commit()
    conn.close()

def insert_initial_users():
    """
    Inserta las cuentas iniciales con contraseñas hasheadas.
    """
    usuarios = [
        {"email": "Ad_01", "password": "01Ad", "type": "admin"},
        {"email": "Em_01", "password": "01Em", "type": "empleado"},
        {"email": "Cl_01", "password": "01Cl", "type": "cliente"},
        {"email": "Cl_02", "password": "Cl02", "type": "cliente"},
    ]

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for u in usuarios:
        hashed_pw = hash_password(u["password"])
        try:
            cursor.execute(
                "INSERT INTO usuarios (email, password, type) VALUES (?, ?, ?)",
                (u["email"], hashed_pw, u["type"])
            )
        except sqlite3.IntegrityError:
            print(f"Usuario {u['email']} ya existe, no se insertó.")

    conn.commit()
    conn.close()

def check_password(email: str, password: str) -> bool:
    """
    Verifica si la contraseña ingresada coincide con la almacenada.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM usuarios WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()

    if result:
        stored_hash = result[0]
        return bcrypt.checkpw(password.encode(), stored_hash.encode())
    return False

if __name__ == "__main__":
    create_database()
    insert_initial_users()
