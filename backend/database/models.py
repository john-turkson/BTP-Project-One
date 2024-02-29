# Databse/models.py

# Database Models

databaseModels = {
    
    # Query to create 'Users' Table
    "usersTable": """ 
                CREATE TABLE Users (
                    user_id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    password VARCHAR(128) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
}


