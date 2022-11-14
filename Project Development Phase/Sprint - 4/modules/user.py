from werkzeug.security import generate_password_hash, check_password_hash
from flask import session
from modules.db import Db

class User(Db):
    def __init__(self) -> None:
        super().__init__()

    def register(self, form) -> bool:
        return self.insert(
            "users", [
                form['username'], 
                form['email'], 
                generate_password_hash(form['password'])
            ]
        )
            
    def login(self, form):
        try:
            data = self.get("users", f"username='{form['username']}'")
            if len(data) != 0:
                if check_password_hash(data[2], form["password"]):
                    session["active"] = data[0]
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(e)
            return False