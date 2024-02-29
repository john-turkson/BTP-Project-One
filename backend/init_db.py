from database import db_create_table_decorator, databaseModels

# Create Tables based on models from 'models.py'

# Use db_command_decorator to create 'Users' Table
@db_create_table_decorator(error_message='Error Creating \'Users\' Table!', success_message='\'Users\' table created successfully!')
def create_users_table(command):
    pass

# Create 'Users' Table
create_users_table(databaseModels['usersTable'])



