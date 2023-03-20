from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    if "user_id" not in session:
        return render_template("index.html")
    return redirect("/dashboard")

@app.route('/user/register', methods=["POST"])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    user_id = User.add_user(request.form)
    session["user_id"] = user_id
    return redirect("/dashboard")

@app.route('/user/login', methods=["POST"])
def login():
    logged_in_user = User.validate_login(request.form)
    if not logged_in_user:
        return redirect("/")
    session["user_id"] = logged_in_user.id
    return redirect("/dashboard")

# @app.route('/dashboard')
# def dashboard():
#     if "user_id" not in session:
#         return redirect("/")
#     logged_in_user = User.get_user_by_id(session["user_id"])
#     return render_template("dashboard.html", logged_in_user = logged_in_user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')