import cv2 as cv
import mediapipe as mp

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

video = cv.VideoCapture(0)

while True:
    isTrue, frame = video.read()
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(rgb)

    finger_count = 0  # Variable to store the count of fingers

    if results.multi_hand_landmarks:
        for hlms in results.multi_hand_landmarks:
            # Draw landmarks using mediapipe
            mpDraw.draw_landmarks(frame, hlms, mpHands.HAND_CONNECTIONS)

            # Check for each finger based on landmark positions
            if hlms.landmark[4].y < hlms.landmark[2].y and hlms.landmark[4].x > hlms.landmark[2].x:  # Thumb
                finger_count += 1
            if hlms.landmark[8].y < hlms.landmark[6].y:  # Index finger
                finger_count += 1
            if hlms.landmark[12].y < hlms.landmark[10].y:  # Middle finger
                finger_count += 1
            if hlms.landmark[16].y < hlms.landmark[14].y:  # Ring finger
                finger_count += 1
            if hlms.landmark[20].y < hlms.landmark[18].y:  # Little finger
                finger_count += 1

    # Display the finger count on the frame
    cv.putText(frame, f"Finger Count: {finger_count}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv.imshow("Live", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()
