# Generate a Password with secrets and string libraries in Python
# -------------------------------------------------------------------------------------------------------------------------------
# This script generates a random password using the secrets and string libraries in Python.
# It creates a password that includes letters, digits, and punctuation characters.
# Note: The function is executed immediately upon definition.
# -------------------------------------------------------------------------------------------------------------------------------
# Importing necessary libraries
import secrets
import string

# This function generates a random password of a specified length.
def generate_password(length=12):
    alphabet = (string.ascii_letters + string.digits + string.punctuation)

    return ''.join(secrets.choice(alphabet) for _ in range(length))

# Immediately Invoked Function Expression (IIFE)
password = generate_password()

# Print the generated password
print(f"Your new Generated Password: {password}")