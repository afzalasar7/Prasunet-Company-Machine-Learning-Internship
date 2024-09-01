import streamlit as st
import cv2
import numpy as np
from joblib import load

st.set_page_config(page_icon='🐈', page_title='Dog and Cat Classification', layout='wide')

st.markdown('<div style="text-align:center;font-size:50px;">Dog vs Cat Classification 🐕 or 🐈</div>', unsafe_allow_html=True)

try:
   model = load('models/dogcat_model.pkl')
except Exception as e:
   st.error(f"Error loading model: {e}")
   st.stop()

class_labels = {1: 'Cat', 2: 'Dog'}

def preprocess_image(image):
   try:
       file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
       
       img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
       if img is None:
           raise ValueError("Invalid image")
       
       img = cv2.resize(img, (50, 50))
       img = img / 255.0
       img = img.reshape((1, -1))
       return img
   except Exception as e:
       st.error(f"Error processing image: {e}")
       return None

def main():
   uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png', '.webp'])

   if uploaded_file is not None:
       st.image(uploaded_file, width = 500)
       
       if st.button('Classify Image'):
           image = preprocess_image(uploaded_file)
           if image is not None:
               prediction = model.predict(image)
               predicted_class = class_labels[int(prediction)]
               st.markdown(f'<div style="font-size:50px;;">Prediction: {predicted_class}</div>', unsafe_allow_html=True)

if __name__ == '__main__':
   main()
