from flask import session
from . import admin



@admin.route('/')
def index():
    return 'Hello from admin index,'



@admin.route('/login/')
def login_admin():
    session['name']= 'emad'
    print(session.get('name'))
    return 'Hello from login admin'