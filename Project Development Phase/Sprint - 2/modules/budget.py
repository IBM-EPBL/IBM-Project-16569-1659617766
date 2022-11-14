from flask import session
from modules.db import Db

class Budget(Db):
    def __init__(self) -> None:
        """
            CREATE TABLE budgets (
                bid VARCHAR(32) UNIQUE NOT NULL,
                bname VARCHAR(30) NOT NULL,
                bdate VARCHAR(12) NOT NULL,
                bamount INTEGER NOT NULL,
                bwallet VARCHAR(32) NOT NULL,
                username VARCHAR(30) NOT NULL
            )
        """
        super().__init__()
    
    def addBudget(self, form) -> bool:
        print(form)
        return self.insert(
            "budgets", [
                self.generateId(),
                form["name"],
                form["date"],
                form["amount"],
                form["wallet"],
                session["active"]
            ]
        )
    
    def deleteBudget(self,form) -> bool:
        self.delete(
            "budgets", f"bid='{form['bid']}'"
        )
        return True

    def getBudgets(self) -> dict:
        return {
            "user" : session["active"],
            "data" : self.getall(
                "budgets", "username='{}'".format(session['active'])
            )
        }