from flask import session
from modules.db import Db

class Wallet(Db):
    def __init__(self) -> None:
        """
            CREATE TABLE wallets (
                wid VARCHAR(32) UNIQUE NOT NULL,
                wname VARCHAR(30) NOT NULL,
                wamount INTEGER NOT NULL,
                username VARCHAR(30) NOT NULL
            )
        """
        super().__init__()
    
    def addWallet(self, form) -> bool:
        self.insert(
            "wallets", [
                self.generateId(),
                form["wname"],
                form["wamount"],
                session["active"]
            ]
        )
        return True
    
    def deleteWallet(self,form) -> bool:
        if self.delete(
                "transactions", f"wallet='{form['wid']}'"
            ) and self.delete(
                "budgets", f"bwallet='{form['wid']}'"
            ):
            return self.delete(
                "wallets", f"wid='{form['wid']}'"
            )
        else:
            return False

    def getWallet(self, wid) -> bool:
        return {
            "status" : "success",
            "data": self.get(
                "wallets", f"wid='{wid}'"
            )
        }

    def getWallets(self) -> dict:
        return {
            "user" : session["active"],
            "data" : self.getall(
                "wallets", "username='{}'".format(session['active'])
            )
        }

    def aboutWallets(self) -> dict:
        wallets = self.getall("wallets", f"username='{session['active']}'")
        bal = 0
        for wallet in wallets:
            bal += wallet[2]
        return {
            "total" : bal,
            "count" : len(wallets)
        }

    