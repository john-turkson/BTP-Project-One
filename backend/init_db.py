from database import db_create_table_decorator, databaseModels

# Create Tables based on models from 'models.py'

# Use db_command_decorator to create 'Users' Table
@db_create_table_decorator(error_message='Error Creating \'Users\' Table!', success_message='\'Users\' table created successfully!')
def create_users_table(command):
    pass

# Use db_command_decorator to create 'Musics' Table
@db_create_table_decorator(error_message='Error Creating \'Musics\' Table!', success_message='\'Musics\' table created successfully!')
def create_musics_table(command):
    pass

# Use db_command_decorator to create 'Playlists' Table
@db_create_table_decorator(error_message='Error Creating \'Playlists\' Table!', success_message='\'Playlists\' table created successfully!')
def create_playlists_table(command):
    pass

# Use db_command_decorator to create 'Association' Table
@db_create_table_decorator(error_message='Error Creating \'Association\' Table!', success_message='\'Association\' table created successfully!')
def create_association_table(command):
    pass

# Create db Tables
create_users_table(databaseModels['usersTable'])
create_musics_table(databaseModels['musicTable'])
create_playlists_table(databaseModels['playlistsTable'])
create_association_table(databaseModels['associationTable'])



