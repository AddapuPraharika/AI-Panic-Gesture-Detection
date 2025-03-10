import cv2  

# Open the webcam
cap = cv2.VideoCapture(0)  

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Save as 'output.avi'

while True:
    ret, frame = cap.read()  # Read a frame
    if not ret:
        break  

    out.write(frame)  # Save the frame to the file
    cv2.imshow("Recording Video", frame)  # Show the video

    # Press 'q' to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  

cap.release()  # Release the webcam
out.release()  # Stop saving the video
cv2.destroyAllWindows()  # Close the window
