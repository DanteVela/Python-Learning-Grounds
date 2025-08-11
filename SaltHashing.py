# Salted Hashing:
import bcrypt

# Generate a salt and hash the password
password = "mypassword123"
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password.encode(), salt)

# Verify the password
if bcrypt.checkpw(password.encode(), hashed_password):
    print("Password matches!")
else:
    print("Invalid password.")