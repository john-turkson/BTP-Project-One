from flask import Flask, request, jsonify
from passwordHash import generateHashedPassword, verifyPassword
from database import db_insert_decorator
from database import databaseCommands
from flask_cors import CORS



# Create's an application that is nammed after the name of the file
server = Flask(__name__)

# Enable CORS for all routes in Flask Server
CORS(server)



@server.route("/")
def index():
    return "Hello world!"


# Route to handle registration form submission
@server.route("/register-user", methods=["POST"])
def register_user():

    data = request.json 

    # Get form data from request
    username = data.get("username")
    email = data.get("email")
    password = generateHashedPassword(data.get("password"), 12)

    # return 'Username: {}, Email: {}, Password: {}'.format(username, email, pasword)

    # Check if all fields are valid
    if not username or not email or not password:
        return jsonify({"message": "All Fields are required."}), 400


    # Insert to Database Command Decorator 
    @db_insert_decorator(error_message="An error occurred while inserting data into the database", success_message="Row inserted successfully",)
    def insert_user_to_db(usernameToBeAdded, emailToBeAdded, passwordToBeAdded):
        user_values = (usernameToBeAdded, emailToBeAdded, passwordToBeAdded)
        return databaseCommands.insert_user_command, user_values

    # Insert into 'Users' table
    if insert_user_to_db(username, email, password):
        return 'Row Added Successfully'
    else:
        return 'An error occurred while inserting data into the database'
    