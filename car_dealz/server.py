from flask_app import app 
from flask_app.controllers import users, cars #import from controllers folder

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=8000)    # Run the app in debug mode, port= 8000 for MAC users cause port 5000 is being taken up by cloud

