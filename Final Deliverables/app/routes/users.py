from flask import Blueprint, session, request
from modules.user import User

userBp = Blueprint('userBp', __name__)

@userBp.route('/signup', methods=['POST'])
def signup():
    if session.get('active') == None:
        if User().register(request.form):
            return {
                'status': "success"
            }
        else:
            return {
                'status': "failed"
            }
    else:
        return {
            'status': "failed",
            "message": "Unauthorized"
        }

@userBp.route('/login', methods=['POST'])
def login():
    if session.get('active') == None:
        if User().login(request.form):        
            return {
                'status': "success"
            }
        else:
            return {
                'status': "failed"
            }
    else:
        return {
            'status': "failed",
            "message": "Unauthorized"
        }