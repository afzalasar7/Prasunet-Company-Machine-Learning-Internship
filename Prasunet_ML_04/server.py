import streamlit as st #type: ignore
import cv2
import numpy as np
from keras.models import load_model #type: ignore
from live_video import capture_video

st.set_page_config(page_icon='✌️', page_title='Hand Gesture Classification', layout="wide")
st.markdown('<div style="text-align:center;font-size:50px;">HAND GESTURE CLASSIFICATION 🤚</div>', unsafe_allow_html=True)

# Load the model
try:
    model = load_model('models/model-10E-99A-98VA.keras')
    st.success('Model loaded successfully')
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

classes = ['ok', 'down', 'C', 'thumb', 'index', 'fist-side', 'fist', 'palm-side', 'palm', 'L']


def preprocess_image(image):
    try:
        file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise ValueError("Invalid image")
        img = cv2.convertScaleAbs(img, alpha=0.8, beta=0)
        img = cv2.resize(img, (200, 200))
        img = img / 255.0
        img = np.expand_dims(img, axis=(0, -1))
        return img
    except Exception as e:
        st.error(f"Error processing image: {e}")
        return None

def classify_image(image):
    try:
        image = preprocess_image(image)
        if image is not None:
            prediction = model.predict(image)
            predicted_class = classes[np.argmax(prediction)]
            confidence = np.max(prediction)
            return predicted_class, confidence, prediction
        else:
            return None, None, None
    except Exception as e:
        st.error(f"Error classifying image: {e}")
        return None, None, None

def main():
    st.sidebar.title('Options')
    app_mode = st.sidebar.selectbox('Choose the app mode',
                                    ['Image Input', 'Webcam Input'])

    if app_mode == 'Image Input':
        st.sidebar.write('Upload an image for classification:')
        uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])
        if uploaded_file is not None:
            st.image(uploaded_file, width = 450)
            if st.button('Classify Image'):
                predicted_class, confidence, prediction = classify_image(uploaded_file)
                if predicted_class is not None:
                    st.write("Prediction Probabilities:", prediction)
                    st.markdown(f'<h2>Predicted Class: {predicted_class}</h2>', unsafe_allow_html=True)
                    st.markdown(f'<h3>Confidence: {confidence:.2f}</h3>', unsafe_allow_html=True)
                else:
                    st.error("Failed to classify image. Please try another image.")

    elif app_mode == 'Webcam Input':
        st.sidebar.write('Click Start to begin webcam capture:')
        if st.button('Start'):
            st.write('To stop the live capture press Q on keyboard')
            capture_video()
            

if __name__ == '__main__':
    main()
