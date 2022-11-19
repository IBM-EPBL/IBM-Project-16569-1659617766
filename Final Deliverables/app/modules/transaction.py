from flask import session
from modules.db import Db

class Transaction(Db):
    def __init__(self) -> None:
        """
            CREATE TABLE transactions (
                tid VARCHAR(32) UNIQUE NOT NULL,
                tdate VARCHAR(12) NOT NULL,
                descp VARCHAR(1000) NOT NULL,
                wallet VARCHAR(32) NOT NULL,
                ttype VARCHAR(7) NOT NULL,
                category VARCHAR(20) NOT NULL,
                amount INTEGER NOT NULL,
                attachment VARCHAR(100),
                username VARCHAR(30) NOT NULL
            )
        """
        super().__init__()
    
    def addTransaction(self, form) -> bool:
        date, descp, wallet, ttype, category, famount, attachment = form["date"], form["descp"], form["wallet"], form["ttype"], form["category"], form["amount"], form["attachment"]
        
        if attachment == '':
            attachment = "None"
        
        data = self.get("wallets", f"wid='{wallet}'")                
        if ttype == "income":            
            amount = data[2] + int(famount)            
        elif ttype == "expense":    
            amount = data[2] - int(famount)
            if amount < 0:
                return False

        if self.execute(f"UPDATE wallets SET wamount={amount} WHERE wid='{data[0]}'"):
            return self.insert(
                    "transactions", [
                        self.generateId(),
                        date, descp, wallet, ttype, category, famount, attachment,                    
                        session["active"]
                    ]
                )
        else:
            return False
            
    def getTransactions(self) -> dict:
        return {
            "user" : session["active"],
            "data" : self.getall(
                "transactions", "username='{}'".format(session['active'])
            )
        }
    
    def deleteTransaction(self, form) -> bool:
        transaction = self.get(
            "transactions", f"tid='{form['tid']}'"
        )
        wallet = self.get(
            "wallets", f"wid='{transaction[3]}'"
        )
        if transaction[4] == "income":
            amount = wallet[2] - transaction[6]
        else:
            amount = wallet[2] + transaction[6]

        if self.execute(
            f"UPDATE wallets SET wamount={amount} WHERE wid='{transaction[3]}'"
        ):
            return self.delete(
                "transactions" , f"tid='{form['tid']}'"
            )
        else:
            return False