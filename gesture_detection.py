import cv2
import mediapipe as mp
import pygame
import time
from twilio.rest import Client

# Twilio Credentials
TWILIO_SID = "--------" #keep you twilio_sid
TWILIO_AUTH_TOKEN = "----------" #keep your twilio_auth_token
TWILIO_PHONE = "---------" #keep your twilio_phone
EMERGENCY_CONTACT = "---------" #keep your emergency_contack

# Initialize Pygame for Alarm
pygame.mixer.init()

# Function to Play Alarm Sound
def play_alarm():
    pygame.mixer.music.load("alarm.mp3")  # Ensure the file exists in the same folder
    pygame.mixer.music.play()
    print("🔊 Alarm Triggered!")
    time.sleep(5)
    pygame.mixer.music.stop()

# Function to Send SOS Alert
def send_sos():
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="🚨 EMERGENCY ALERT! Help needed!",
        from_=TWILIO_PHONE,
        to=EMERGENCY_CONTACT
    )
    print(f"📩 SOS Message Sent! Message ID: {message.sid}")

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

            if abs(index_tip.x - thumb_tip.x) > 0.1:  # Adjust threshold
                print("🚨 Emergency Gesture Detected!")
                cv2.putText(frame, "🚨 Panic Gesture Detected!", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                
                # Play Alarm & Send SOS
                play_alarm()
                send_sos()

    cv2.imshow("Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("✅ Gesture Recognition Stopped.")
