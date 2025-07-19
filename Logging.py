# This script demonstrates the importance of not logging sensitive information such as credit card numbers.
# It shows how to properly handle sensitive data in logs by using a sanitization function.
# ----------------------------------------------------------------------------------------------------------------------------------
# Import necessary libraries
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename='app.log')
# ----------------------------------------------------------------------------------------------------------------------------------
# Improperly logging sensitive information:
# This function logs payment details including sensitive information like credit card numbers.
# It is not secure as it exposes sensitive data in the logs.
def old_process(user_id, credit_card_number, amount):
    logging.info(f"Processing payment "
                 f"for user {user_id} "
                 f"with credit card"
                 f" {credit_card_number} "
                 f"for amount {amount}")

    # TODO: Code to process the payment
    print("Payment processed.")
# ----------------------------------------------------------------------------------------------------------------------------------
# Replace with asterisks
def sanitize(info):
    return "**** **** **** ****"

# Optimized process function to use Sanitize:
# This function logs payment details while ensuring sensitive information is not exposed.
# It uses the Sanitize function to mask credit card numbers before logging.
def process(user_id, credit_card_number, amount):
    sanitized_card = sanitize(credit_card_number)
    logging.info(f"Processing payment "
                 f"for user {user_id} "
                 f"with credit "
                 f"card {sanitized_card} "
                 f"for amount {amount}")
    
    # TODO: Code to process the payment
    print("Payment processed.")

# Example usage
old_process('user123', '4111 1111 1111 1111', 100.0)
process('user123', '4111 1111 1111 1111', 100.0)