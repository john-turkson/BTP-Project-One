import bcrypt

def generateHashedPassword(password_str, rounds):
    
    # Generate a salt
    salt = bcrypt.gensalt(rounds)

    # Hash the password with the generated salt
    hashed_password = bcrypt.hashpw(password_str.encode('utf-8'), salt)

    return hashed_password.decode('utf-8')


# Verify Password
def verifyPassword(passwordToCheck, hashed_password):
    
    # Check if the plain password matches the hashed password
    return bcrypt.checkpw(passwordToCheck, hashed_password)

