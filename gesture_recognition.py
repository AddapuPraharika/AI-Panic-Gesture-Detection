import cv2
import mediapipe as mp
import pygame
import time
import threading  # Import threading for non-blocking execution
from twilio.rest import Client
import requests

# Twilio Credentials
TWILIO_SID = "-----------" # keep your twilio_sid
TWILIO_AUTH_TOKEN = "----------" #keep your twilio_auth_token
TWILIO_PHONE = "---------" # keep your twilio_phone_number
EMERGENCY_CONTACT = "----------" #keep your emergency_contack

# Initialize Pygame for Alarm
pygame.mixer.init()

# Function to Play Alarm Sound (Runs in Background)
def play_alarm():
    print("🔊 Playing Alarm...")
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play()
    time.sleep(5)
    pygame.mixer.music.stop()
    print("✅ Alarm Stopped!")

# Function to Get Live Location
# Function to Get Fixed Location (Maisammaguda Women's College)
def get_location():
    latitude = 17.5449  # Set fixed latitude
    longitude = 78.5692  # Set fixed longitude
    google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    return google_maps_link

# Function to Send SOS Alert (Runs in Background)
def send_sos():
    print("📩 Sending SOS Message with Location...")
    location_url = get_location()
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        for i in range(3):
            message = client.messages.create(
            body=f"🚨 EMERGENCY ALERT! Help needed!\n📍 Live Location: {location_url}",
            from_=TWILIO_PHONE,
            to=EMERGENCY_CONTACT[i]
            )
            print(f"✅ SOS Message Sent! Message ID: {message.sid}")
    except Exception as e:
        print(f"❌ Failed to send SOS message: {e}")





"""
        message = client.messages.create(
            body=f"🚨 EMERGENCY ALERT! Help needed!\n📍 Live Location: {location_url}",
            from_=TWILIO_PHONE,
            to=EMERGENCY_CONTACT
        )
        print(f"✅ SOS Message Sent! Message ID: {message.sid}")
    except Exception as e:
        print(f"❌ Failed to send SOS message: {e}")"""

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Initialize Camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
print("🚀 Gesture Recognition Started...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Camera not working!")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        print("✅ Hand Detected!")
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Example Gesture Detection (Open Palm)
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            if abs(index_tip.x - thumb_tip.x) > 0.1:
                print("🚨 Emergency Gesture Detected!")
                cv2.putText(frame, "🚨 Panic Gesture Detected!", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

                # Run Alarm & SOS in Parallel
                threading.Thread(target=play_alarm).start()
                threading.Thread(target=send_sos).start()

    cv2.imshow("Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("✅ Gesture Recognition Stopped.")
