from flask import Blueprint, render_template, redirect, url_for, request, session
from src import get_config
from src.Database import Database
from src.Auth import Auth

bp = Blueprint("api", __name__, url_prefix="/api")

db = Database.get_connection()

@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if all(key in request.form for key in ['username', 'password', 'team_name', 'register_no']):
            username = request.form['username']
            password = request.form['password']
            team_name = request.form['team_name']
            register_no = request.form['register_no']

            result = Auth.register(username, password, team_name, register_no)
            if result == "Registration successful":
                session['authenticated'] = True
                return redirect(url_for('student_dashboard'))
            else:
                return str(result)
    return render_template('register.html')

@bp.route("/student/login", methods=['POST'])
def student_login():
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        result = Auth.student_login(username, password)
        if result == "Login successful":
            session['authenticated'] = True
            return redirect(url_for('student_dashboard'))
        else:
            return str(result)

@bp.route("/tutor/login", methods=['POST'])
def tutor_login():
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        result = Auth.tutor_login(username, password)
        if result == "Login successful":
            session['authenticated'] = True
            return redirect(url_for('tutor_dashboard'))
        else:
            return str(result)

@bp.route("/student/dashboard")
def student_dashboard():
    if 'authenticated' in session and session['authenticated']:
        return render_template('student_dashboard.html')
    else:
        return redirect(url_for('home.login'))

@bp.route("/tutor/dashboard")
def tutor_dashboard():
    if 'authenticated' in session and session['authenticated']:
        return render_template('tutor_dashboard.html')
    else:
        return redirect(url_for('home.login'))

@bp.route("/function")
def function():
    if 'authenticated' in session and session['authenticated']:
        return render_template('function.html')
    else:
        return redirect(url_for('home.login'))
