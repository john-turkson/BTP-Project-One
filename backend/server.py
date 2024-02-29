from flask import Flask, request, jsonify
from passwordHash import generateHashedPassword, verifyPassword
from database import db_insert_decorator, databaseModels


# Create's an application that is nammed after the name of the file
server = Flask(__name__)

@server.route("/")
def index():
    return "Hello world!"


# Route to handle registration form submission
@server.route("/register-user", methods=["POST"])
def register_user():

    # Get form data from request
    username = request.form.get("username")
    email = request.form.get("email")
    pasword = request.form.get("password")

    # return 'Username: {}, Email: {}, Password: {}'.format(username, email, pasword)

    password = generateHashedPassword(request.form.get("password"), 12)

    # Check if all fields are valid
    if not username or not email or not password:
        return jsonify({"message": "All Fields are required."}), 400

    # SQL command to insert user into 'Users' table
    insert_user_command = """
    INSERT INTO Users (username, email, password)
    VALUES (%s, %s, %s)
    """

    # Insert to Database Command Decorator 
    @db_insert_decorator(error_message="An error occurred while inserting data into the database", success_message="Row inserted successfully",)
    def insert_user_to_db(usernameToBeAdded, emailToBeAdded, passwordToBeAdded):
        user_values = (usernameToBeAdded, emailToBeAdded, passwordToBeAdded)
        return insert_user_command, user_values

    # Insert into 'Users' table
    if insert_user_to_db(username, email, password):
        return 'Row Added Successfully'
    else:
        return 'An error occurred while inserting data into the database'
    