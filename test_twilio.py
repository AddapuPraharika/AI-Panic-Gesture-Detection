from twilio.rest import Client

# Replace with your Twilio credentials
ACCOUNT_SID = "-----------" # keep your account_sid
AUTH_TOKEN = "------------" # keep your auth_token
TWILIO_PHONE = "-----------" # keep your twilio_phone
RECEIVER_PHONE = "----------" # keep your receiver_phone

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    body="🚨 Test SOS Alert! 🚨",
    from_=TWILIO_PHONE,
    to=RECEIVER_PHONE
)

print("✅ SOS Message Sent! Message ID:", message.sid)
