import time
import requests
from twilio.rest import Client
import geocoder

# Twilio credentials (Replace with your actual credentials)
TWILIO_SID = "-----------"  #keep your twilio_sid0f27b
TWILIO_AUTH_TOKEN = "-----------" #keep your twilio_auth_token
TWILIO_PHONE_NUMBER = "-----------" #keep your twilio_phone_number
EMERGENCY_CONTACT = "-----------" # keep your emergency_contack

# Function to get live location


# Function to Get Exact GPS Location
# Function to Get Fixed Location (Maisammaguda Women's College)
def get_location():
    latitude = 546082  # Set fixed latitude
    longitude = 23.5370  # Set fixed longitude
    google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    return google_maps_link



# Function to send SOS alert with live location
def send_sos_alert():
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    
    try:
        while True:
            location = get_live_location()
            message_body = f"🚨 SOS Alert! Emergency detected! Live Location: {location}"
            
            message = client.messages.create(
                body=message_body,
                from_=TWILIO_PHONE_NUMBER,
                to=EMERGENCY_CONTACT
            )
            
            print(f"✅ SOS Alert Sent! Message ID: {message.sid}")
            time.sleep(10)  # Wait for 10 seconds before sending next update
    
    except KeyboardInterrupt:
        print("❌ SOS Tracking Stopped by User")

# Run the function
send_sos_alert()