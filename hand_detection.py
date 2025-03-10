import cv2
import mediapipe as mp  

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils  # For drawing hand landmarks

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break  

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert frame to RGB
    results = hands.process(frame_rgb)  # Detect hands

    if results.multi_hand_landmarks:  # If hands are detected
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)  # Draw hand landmarks

    cv2.imshow("Hand Detection", frame)  # Show the video with hand tracking

    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  

cap.release()
cv2.destroyAllWindows()
