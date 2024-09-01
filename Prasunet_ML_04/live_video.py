import cv2
import numpy as np
from keras.models import load_model # type: ignore

classes = ['ok', 'down', 'C', 'thumb', 'index', 'fist-side', 'fist', 'palm-side', 'palm', 'L']

def preprocess_image(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (200,200))
    img = img / 255.0
    img = np.expand_dims(img, axis=(0,-1))
    return img


def capture_video():
    # Open the video capture
    cap = cv2.VideoCapture(0)  # 0 corresponds to the first webcam connected
    model = load_model('models/model-10E-99A-98VA.keras')
    if model is None: return

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        image = preprocess_image(frame)
        predicts = classes[np.argmax(model.predict(image))]
        cv2.putText(frame, predicts, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

        cv2.imshow('Video Capture', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
