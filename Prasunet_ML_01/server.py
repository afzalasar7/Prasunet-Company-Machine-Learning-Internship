import warnings
warnings.filterwarnings('ignore')

import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import RobustScaler

st.set_page_config(page_icon="🏡", page_title="House Prices Prediction", layout='wide')

st.markdown('<h1 style="text-align:center;">HOUSE PRICES PREDICTION 🏡</h1>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center;">based on Square Footing, Number of Bedrooms and Number of Bathrooms🔍</div>', unsafe_allow_html=True)
st.write('---')


def load_model(file_path):
    try:
        model = joblib.load(file_path)
        return model
    except (OSError, IOError) as e:
        st.error(f"Error loading model file {file_path}: {e}")
        return None
    except joblib.externals.loky.process_executor._RemoteTraceback as e:
        st.error(f"Error unpickling model file {file_path}: {e}")
        return None

def model_predictions(dataset, features):
    l2_model = load_model('models/Linear_Regression_l2Regularizer_model.pkl')
    lr_model = load_model('models/Linear_Regression_model.pkl')
    
    if l2_model is None or lr_model is None:
        return None, None

    rs = RobustScaler()
    rs.fit(dataset.loc[:,['SquareFeet', 'Bedrooms', 'Bathrooms']])

    input_data = rs.transform(features)
    
    l2_prediction = l2_model.predict(input_data)
    lr_prediction = lr_model.predict(input_data)
    
    return l2_prediction, lr_prediction

def process_uploaded_file(dataset, uploaded_file):
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success('File successfully uploaded and loaded into DataFrame.')

            l2_predictions = []
            lr_predictions = []
            
            df = df.loc[:, ['SquareFeet', 'Bedrooms', 'Bathrooms']]
            df = df.ffill()
            rs = RobustScaler()
            rs.fit(dataset.loc[:,['SquareFeet', 'Bedrooms', 'Bathrooms']])

            df = rs.transform(df)

            l2_model = load_model('models/Linear_Regression_l2Regularizer_model.pkl')
            lr_model = load_model('models/Linear_Regression_model.pkl')
            
            if l2_model is None or lr_model is None:
                return None, None
            
            l2_predictions.append(l2_model.predict(df))
            lr_predictions.append(lr_model.predict(df))

            st.write(l2_predictions)
            st.write(lr_predictions)

        except Exception as e:
            st.error(f"Error processing uploaded file: {e}")


def main():
    global dataset
    dataset = pd.read_csv('./data/housing_price_dataset.csv') 

    col1, col2, col3 = st.columns(3)

    with col1:
        square_footing = st.number_input("Square Footing of the house")

    with col2:
        bathrooms = st.number_input("Total Number of Bedrooms in the house")

    with col3:
        bedrooms = st.number_input("Total Number of Bathrooms in the house")
    
    features = [square_footing, bathrooms, bedrooms]
    
    
    submit_button = st.button('Predict Individual 🚀')

    if submit_button:
        l2_prediction, lr_prediction = model_predictions(dataset, [features])
        if l2_prediction is not None and lr_prediction is not None:
            st.write(f'🔮 L2 Regularized Linear Regression Prediction: ${l2_prediction[0]:,.2f}')
            st.write(f'🔮 Linear Regression Prediction: ${lr_prediction[0]:,.2f}')

    st.write('---')

    uploaded_file = st.file_uploader('Upload a CSV file for batch prediction:', type=['csv'])

    if st.button('Predict from File 📁') and uploaded_file is not None:
        print(process_uploaded_file(dataset, uploaded_file))

main()
