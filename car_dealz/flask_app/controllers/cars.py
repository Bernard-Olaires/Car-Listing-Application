from flask import render_template,redirect,session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.car import Car

# car dashboard route

@app.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        return redirect("/")
    logged_in_user = User.get_user_by_id(session["user_id"])
    cars = Car.get_all_cars()
    return render_template("dashboard.html", logged_in_user = logged_in_user, cars = cars)


# car view route 

@app.route('/view/car/<int:id>')
def view_car(id):
    if "user_id" not in session:
        return redirect("/")
    logged_in_user = User.get_user_by_id(session["user_id"])
    car_to_show = Car.car_to_show(id)
    return render_template("car-details.html", logged_in_user = logged_in_user, car = car_to_show)


# car add route 

@app.route('/add/car')
def add_car():
    if "user_id" not in session:
        return redirect('/')
    logged_in_user = User.get_user_by_id(session["user_id"])
    return render_template("add-car.html", logged_in_user = logged_in_user)

@app.route('/create/car', methods=['POST'])
def create_car():
    if "user_id" not in session:
        return redirect('/')
    if Car.validate_car(request.form):
        Car.create_car(request.form)
        return redirect("/dashboard")
    return redirect('/add/car')

@app.route('/edit/car/<int:id>')
def edit_car(id):
    if "user_id" not in session:
        return redirect('/')
    logged_in_user = User.get_user_by_id(session["user_id"])
    car_to_show = Car.car_to_show(id)
    return render_template("edit-car.html", logged_in_user = logged_in_user, car = car_to_show)

@app.route('/update/car/<int:id>', methods=['POST'])
def update_car(id):
    if "user_id" not in session:
        return redirect('/')
    if Car.validate_car(request.form):
        Car.update_car(request.form)
    return redirect("/dashboard")

@app.route('/delete/car/<int:id>')
def delete_car(id):
    if "user_id" not in session:
        return redirect('/')
    Car.delete_car(id)
    return redirect("/dashboard")