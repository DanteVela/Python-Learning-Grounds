import phonenumbers
from phonenumbers import geocoder, carrier
# -------------------------------------------------------------------------------------------------------------------------------- 
# lookup_number function to get location and carrier information
# This function takes a phone number string and an optional default region code
def lookup_number(number_str, default_region="US"):
    # Parse the E.164 or national‐format number
    parsed = phonenumbers.parse(number_str, default_region)

    # Geographical location (city, state, etc.) or None if blank
    location = geocoder.description_for_number(parsed, "en") or None

    # Carrier name or None if not found
    phone_carrier = carrier.name_for_number(parsed, "en") or None

    return location, phone_carrier

def information_found(location, phone_carrier):
    if location and phone_carrier:
        print(f"Location: {location}")
        print(f"Carrier: {phone_carrier}")
    elif location and not phone_carrier:
        print(f"Location: {location}, carrier information not found.")
    elif phone_carrier and not location:
        print(f"Carrier: {phone_carrier}, location information not found.")
    else:
        print("Location and carrier information not found.")
# ---------------------------------------------------------------------------------------------------------------------------------
# Look up the location and carrier for a given phone number using the lookup_number function
location, phone_carrier = lookup_number("+14155552671")
information_found(location, phone_carrier)
# ---------------------------------------------------------------------------------------------------------------------------------