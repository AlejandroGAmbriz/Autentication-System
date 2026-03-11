"""Contain the logic of the system request
"""
import sqlite3
import bcrypt
from constants import DB_ACCOUNT, DB_REQUEST

class SystemActions():

    def __init__(self, user: str, password: str):
        self.user = user
        self.password = password
        self.role = None

        self.conn_account = sqlite3.connect(DB_ACCOUNT)
        self.cursor_account = self.conn_account.cursor()
        self.conn_account.commit()

        self.conn_request = sqlite3.connect(DB_REQUEST)
        self.cursor_request = self.conn_request.cursor()
        self.conn_request.commit()

    def log_verification(self) -> bool:
        """Check if the password and the user are in the DB (the password must be hashed)."""
        self.cursor_account.execute(
            "SELECT password, type FROM usuarios WHERE email = ?",
            (self.user,)
        )
        resultado = self.cursor_account.fetchone()

        if resultado is None:
            return False

        hashed_password, user_type = resultado

        if bcrypt.checkpw(self.password.encode("utf-8"), hashed_password.encode("utf-8")):
            self.role = user_type
            return True

        return False

    def create_request(self, account_id: str, owner_id: str, title: str, description: str) -> bool:
        if not RolAcces(self.role).can_create_request():
            return False

        self.cursor_request.execute("""
        INSERT INTO requests (account_id, owner_ID, create_date, status, description, title)
        VALUES (?, ?, datetime('now'), 'open', ?, ?)
        """, (account_id, owner_id, description, title))
        self.conn_request.commit()
        return True

    def show_request(self, request_id: int, current_user_id: str) -> dict | None:
        self.cursor_request.execute("SELECT * FROM requests WHERE id = ?", (request_id,))
        row = self.cursor_request.fetchone()
        if row:
            owner_id = row[2] 
            if RolAcces(self.role).can_view_request(owner_id, current_user_id):
                return {
                    "id": row[0],
                    "account_id": row[1],
                    "owner_ID": row[2],
                    "create_date": row[3],
                    "status": row[4],
                    "description": row[5],
                    "title": row[6]
                }
        return None

    def mod_status_request(self, request_id: int, new_status: str) -> bool:
        if not RolAcces(self.role).can_change_status():
            return False

        self.cursor_request.execute("""
        UPDATE requests SET status = ? WHERE id = ?
        """, (new_status, request_id))
        self.conn_request.commit()
        return True

    def remove_request(self, request_id: int) -> bool:
        if not RolAcces(self.role).can_delete_request():
            return False

        self.cursor_request.execute("DELETE FROM requests WHERE id = ?", (request_id,))
        self.conn_request.commit()
        return True



class RolAcces():

    def __ini__(self, role: str):
        self.role = role

    def can_create_request(self) -> bool:
        return self.role in ["client", "employee", "admin"]

    def can_view_request(self, owner_id: str, current_user_id: str) -> bool:
        if self.role == "client":
            return owner_id == current_user_id
        return self.role in ["employee", "admin"]

    def can_change_status(self) -> bool:
        return self.role in ["employee", "admin"]

    def can_delete_request(self) -> bool:
        return self.role == "admin"
