from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models.user import User

class Car:
    DB = "car_dealz"
    
    def __init__(self, data):
        self.id = data['id']
        self.seller = data['seller']
        self.price = data['price']
        self.model = data['model']
        self.make = data['make']
        self.year = data['year']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None
        
    # get_all_cars classmethod to get all cars info from database
    
    @classmethod
    def get_all_cars(cls):
        query = """
        SELECT * FROM cars 
        LEFT JOIN users on users.id = cars.user_id;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        print("__ GET ALL CARS __", results)
        cars = []
        for row in results:
            car = cls(row)
            car_creator_info = {
                "id":row['users.id'],
                "first_name":row['first_name'],
                "last_name":row['last_name'],
                "email":row['email'],
                "password":row['password'],
                "created_at":row['created_at'],
                "updated_at":row['updated_at']
            }
            creator = User(car_creator_info)
            car.creator = creator
            cars.append(car)
        return cars
    
    # get_car_by_id classmethod to get one car info from database
    
    @classmethod
    def car_to_show(cls, car_id):
        data = {"id" : car_id}
        query = """
        SELECT * FROM cars 
        LEFT JOIN users on users.id = cars.user_id;
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        result = result[0]
        car = cls(result)
        print("__ CAR TO SHOW __", car)
        car.creator = User(
                {
                    "id":result['users.id'],
                    "first_name":result['first_name'],
                    "last_name":result['last_name'],
                    "email":result['email'],
                    "password":result['password'],
                    "created_at":result['created_at'],
                    "updated_at":result['updated_at']
                }
            )
        return car
    
    # add_car classmethod to add a car listing 
    
    @classmethod
    def create_car(cls, data):
        query = """
        INSERT INTO cars (price, model, make, year, description, user_id) 
        VALUES (%(price)s, %(model)s, %(make)s, %(year)s, %(description)s, %(user_id)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        print ("__ CREATE CAR __ ",result)
        return result
    
    # update_car classmethod to update car listing 

    @classmethod
    def update_car(cls, data):
        query = """
        UPDATE cars SET price=%(price)s, model=%(model)s, make=%(make)s, year=%(year)s, description=%(description)s WHERE user_id = %(user_id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        print("__ UPDATING CAR __", result)
        return result

    
    # delete_car classmethod to delete car listing 
    
    @classmethod
    def delete_car(cls, car_id):
        data = {"id" : car_id}
        query = """
        DELETE FROM cars WHERE id=%(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        print ("__ DELETING CAR __", result)
        return result
    
    #validate_car staticmethod to validate car info
    
    @staticmethod
    def validate_car(car):
        is_valid = True
        if len(car['price']) < 3:
            flash("Car cannot be under $0")
            is_valid = False
        if len(car['year']) < 3:
            flash("Year cannot be left blank")
            is_valid = False 
        if len(car['model']) < 3:
            flash("Model Cannot Be Left Blank")
            is_valid = False
        if len(car['make']) < 3:
            flash("Make Cannot Be Left Blank")
            is_valid = False
        if len(car['description']) < 3:
            flash("Description Cannot Be Left Blank")
            is_valid = False
        return is_valid