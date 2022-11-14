from flask import Blueprint, request, session

from modules.wallet import Wallet
from modules.budget import Budget
from modules.transaction import Transaction

crudBp = Blueprint("crudBp", __name__ )

@crudBp.route('/add/<group>', methods = ['POST'])
def create(group):
    if session.get("active") != None:       
        if group == "wallet":         
            if Wallet().addWallet(request.form):
                return {"status" : "success"}
            else:
                return {"status" : "failed"}
        elif group == "budget":         
            if Budget().addBudget(request.form):
                return {"status" : "success"}
            else:
                return {"status" : "failed"}
        elif group == "transaction":         
            if Transaction().addTransaction(request.form):
                return {"status" : "success"}
            else:
                return {"status" : "failed"}
        else:
            return {"status" : "failed","message": "Invalid Group"}
    else:
        return {"status": "failed","message": "Unauthorized"}

@crudBp.route('/get/<group>', methods = ['GET','POST'])
def get(group):
    if session.get("active") != None:
        if group == "wallet":      
            wallet = Wallet()
            if request.args.get("wid") == "all":
                return wallet.getWallets()            
            else:
                return wallet.getWallet(request.args.get('wid'))           
        else:
            return {"status" : "failed","message": "Invalid Group"}
    else:
        return {"status": "failed","message": "Unauthorized"}

@crudBp.route('/delete/<group>', methods = ['GET','POST'])
def delete(group):
    if session.get("active") != None:
        if group == "wallet":         
            if Wallet().deleteWallet(request.form):
                return {"status" : "success"}
            else:
                return {"status" : "failed"}
        elif group == "budget":         
            if Budget().deleteBudget(request.form):
                return {"status" : "success"}   
            else:
                return {"status" : "failed"}
        elif group == "transaction":
            if Transaction().deleteTransaction(request.form):
                return {"status" : "success"}   
            else:
                return {"status" : "failed"}
        else:
            return {"status" : "failed","message": "Invalid Group"}
    else:
        return {"status": "failed","message": "Unauthorized"}