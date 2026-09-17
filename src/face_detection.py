import cv2
import time


def run_face_detection():
    # Step 1: Load Haar Cascade Model
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)

    if face_cascade.empty():
        print("Error: Failed to load Haar Cascade XML model file.")
        return

    # Step 2: Initialize Webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to access webcam.")
        return

    prev_time = 0

    print("Face Detection System running.")
    print("Press 'q' in the video window to exit.")

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to capture frame from webcam.")
            break

        # Step 3: Resize and Preprocess Frame
        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        # Step 4: Multi-Scale Face Detection
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Step 5: Draw Bounding Rectangles
        for (x, y, w, h) in faces:
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "Face Detected",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        # Step 6: Calculate FPS
        curr_time = time.time()

        if prev_time != 0:
            fps = 1 / (curr_time - prev_time)
        else:
            fps = 0

        prev_time = curr_time

        # Step 7: Display FPS and Number of Faces
        cv2.putText(
            frame,
            f"FPS: {int(fps)} | Faces Detected: {len(faces)}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 0, 0),
            2
        )

        # Step 8: Display Video
        cv2.imshow(
            "Vityarthi Real-Time Face Detection",
            frame
        )

        # Step 9: Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Step 10: Release Resources
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_face_detection()
