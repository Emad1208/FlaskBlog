from flask import session,render_template, request, abort, flash
from . import admin
from mod_users.models import User
from mod_users.forms import LogingForm
from .utils import admin_only_view


@admin.route('/')
@admin_only_view
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
        if not user.is_admin():
            flash("You don't have the permition", category= 'warning')
            return render_template('admin/login.html', form = form)
        session['email'] = user.email
        session['user_id'] = user.id
        session['role'] = user.role
        return 'Logged in successfuly!'
    if session.get('role') == 1:
        return "You are already logged in"
    return render_template('admin/login.html', form = form)