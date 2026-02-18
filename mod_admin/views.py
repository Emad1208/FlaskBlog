from flask import session,render_template, request, abort, flash
from . import admin
from mod_users.models import User
from mod_users.forms import LogingForm



@admin.route('/')
def index():
    return 'Hello from admin index,'



@admin.route('/login/', methods = ['GET','POST'])
def login_admin():
    form = LogingForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            abort(400)
        user = User.query.filter(User.email.ilike('{}'.format(form.email.data))).first()
        print(user)
        if not user:
            flash("The Email doesn't exist", category= 'error')
            return render_template('admin/login.html', form = form)
        if not user.check_password(form.password.data):
            flash("Incorrect Credential", category= 'warning')
            return render_template('admin/login.html', form = form)
        session['email'] = user.email
        session['user_id'] = user.id
        return 'Logged in successfuly!'
    if session.get('email'):
        return "You are already logged in"
    return render_template('admin/login.html', form = form)