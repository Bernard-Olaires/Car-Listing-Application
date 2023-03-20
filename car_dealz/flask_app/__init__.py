from flask import Flask  
# Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "bird is the word" # Creating a secret key for our session