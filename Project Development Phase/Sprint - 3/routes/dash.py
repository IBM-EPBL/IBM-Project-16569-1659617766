from flask import Blueprint, render_template, redirect, session, request

from modules.wallet import Wallet
from modules.budget import Budget
from modules.transaction import Transaction

import requests
import os 


dashBp = Blueprint("dash", __name__, url_prefix="/dash")

@dashBp.route("/")
def dashIndex():
    if session.get("active") != None:
        return render_template("dash.html", title="Home", wallets = Wallet().aboutWallets(), budgets = len(Budget().getBudgets()["data"]))
    else:
        return redirect("/")

@dashBp.route("/transactions")
def transactions():
    return render_template("transactions.html" , title = "Transactions", transactions = Transaction().getTransactions())

@dashBp.route("/news", methods = ['GET'])
def news():    
    if request.args.get("q") != None:
        return render_template("news.html", title = f"News | {request.args.get('q')}", news = requests.get(f'https://newsapi.org/v2/everything?q=economics+{request.args.get("q")}&apiKey={os.environ["NEWS_API_KEY"]}').json())
    else:
        return render_template("news.html", title = "News", news = requests.get(f'https://newsapi.org/v2/everything?q=economics&apiKey={os.environ["NEWS_API_KEY"]}').json())

@dashBp.route("/calc", methods = ['GET'])
def calc():        
    return render_template("calc.html", title = "Calc")


@dashBp.route("/wallets")
def wallets():
    return render_template("wallets.html", title = "Wallets" ,wallets = Wallet().getWallets())

@dashBp.route("/budgets")
def budgets():
    return render_template("budgets.html", title = "Budgets", budgets = Budget().getBudgets(), wallets = Wallet().getWallets() , int = int)
