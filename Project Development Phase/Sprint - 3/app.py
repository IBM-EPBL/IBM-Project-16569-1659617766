from flask import Flask, render_template, redirect, send_file, session 
from flask_session import Session

from routes.users import userBp
from routes.dash import dashBp
from routes.crud import crudBp

from dotenv import load_dotenv

import os

load_dotenv()        
app = Flask(__name__ )
app.secret_key = os.environ["APP_SECRET_KEY"]
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

app.register_blueprint(userBp)
app.register_blueprint(dashBp)
app.register_blueprint(crudBp)

@app.route("/")
def index():
    if session.get("active") == None:
        return render_template("index.html")
    else:
        return redirect("/dash")

@app.route("/logout")
def logout():
    session.clear()        
    return redirect("/")

@app.route('/favicon.ico')
def favicon():
    return send_file("static/img/logo.svg")

if __name__ == '__main__':
    app.run(debug=True)