from flask import Blueprint, request
from modules.transaction import Transaction

transactionsBp = Blueprint('transactionsBp', __name__, url_prefix="/transactions")

@transactionsBp.route("/add", methods = ["POST"])
def transAdd():
    if Transaction().addTransaction(request.form):
        return {
            "status": "success"
        }
    else:
        return {
            "status": "failed"
        }