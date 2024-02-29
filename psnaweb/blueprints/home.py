#from flask import Blueprint, render_template, redirect, url_for, request, session
import json
from src.Auth import Auth


from flask import Blueprint, render_template, session

bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/")
def home():
    return render_template('index.html', session=session)


@bp.route("/login")
def login():
    return render_template('login.html', session=session)


@bp.route("/register")
def register():
    return render_template('register.html', session=session)


@bp.route("/student_dashboard")
def student_dashboard():
    return render_template('parking.html', session=session)


@bp.route("/tutor_dashboard")
def tutor_dashboard():
    return render_template('payment.html', session=session)


@bp.route("/cancel")
def cancel():
    return render_template('cancel.html', session=session)


@bp.route("/contact")
def contact():
    return render_template('contact.html', session=session)


@bp.route("/confirm")
def confirm():
    # Placeholder for the /confirm route
    pass
