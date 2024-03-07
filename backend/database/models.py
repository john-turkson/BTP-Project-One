# Databse/models.py

# Database Models

databaseModels = {

    # Query to create 'Users' Table
    "usersTable": """ 
                CREATE TABLE IF NOT EXISTS Users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password VARCHAR(128) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """,

    # Query to create 'Musics' Table
    "musicTable": """
                CREATE TABLE IF NOT EXISTS Musics (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(100) NOT NULL,
                    artist VARCHAR(100) NOT NULL,
                    image BYTEA,
                    mp3_file BYTEA,
                    user_id INTEGER REFERENCES users(id) NOT NULL
                );
                """,

    # Query to create 'Playlists' Table
    "playlistsTable": """
                CREATE TABLE IF NOT EXISTS Playlists (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    image BYTEA,
                    user_id INTEGER REFERENCES users(id) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """,

    "associationTable": """
                CREATE TABLE IF NOT EXISTS Association (
                    playlist_id INTEGER REFERENCES playlists(id),
                    music_id INTEGER REFERENCES musics(id),
                    PRIMARY KEY (playlist_id, music_id)
                );
                """
                
}

# Database Commands

databaseCommands = {

    # SQL command to insert user into 'Users' table
    "insert_user_command": """
    INSERT INTO Users (username, password)
    VALUES (%s, %s)
    """

}
