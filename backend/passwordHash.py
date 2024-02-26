import bcrypt

storedPassword = b'password'

# Salting the password
salt = bcrypt.gensalt()

# Hash the password
hashedPassword = bcrypt.hashpw(storedPassword, salt);


# Print Salt
print("Salt :")
print(salt)
 
# printing the hashed
print("Hashed")
print(hashedPassword)

enteredPassword = b'password'

# Check if the entered password is equal to the hashed stored password
if (hashedPassword != bcrypt.hashpw(enteredPassword, hashedPassword)):
    print('False')
else:
    print('True')