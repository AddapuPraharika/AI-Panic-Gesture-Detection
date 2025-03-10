import geocoder
from twilio.rest import Client

# Twilio Credentials (Replace with yours)
ACCOUNT_SID = "-----------" # keep your account_sid
AUTH_TOKEN = "---------" # keep your auth_token
TWILIO_PHONE = "--------"  # keep your Twilio phone number
TO_PHONE = "----------"  # Your personal verified number

def get_live_location():
    """Fetches the user's live location using IP-based geolocation"""
    g = geocoder.ip("me")  # Gets current location based on IP
    if g.latlng:
        latitude, longitude = g.latlng
        google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
        return google_maps_link
    else:
        return "Location not found"

def send_sos_alert():
    """Sends an emergency SOS alert with location via Twilio"""
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    location_link = get_live_location()  # Get live GPS location

    sos_message = f"🚨 EMERGENCY ALERT! Help needed! 🚨\n📍 Location: {location_link}"

    message = client.messages.create(
        body=sos_message,
        from_=TWILIO_PHONE,
        to=TO_PHONE
    )
    
    print(f"🚀 SOS Alert Sent Successfully! Message ID: {message.sid}")

# Run the SOS alert function
send_sos_alert()
