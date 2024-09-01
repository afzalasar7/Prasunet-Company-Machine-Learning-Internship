import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from sklearn.preprocessing import MinMaxScaler

# Set page configuration
st.set_page_config(page_icon='🛒', page_title='Mall Customer Segmentation', layout="wide")

# Page title with emojis
st.markdown('<div style="text-align:center;font-size:50px;">MALL CUSTOMER SEGMENTATION 🛍️</div>', unsafe_allow_html=True)

def load_model():
    try:
        model = joblib.load('models/customer_clustering.pkl')
        return model
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

def plot_clusters(data_scaled, labels, new_data_scaled=None, new_label=None):
    cluster_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    
    plt.figure(figsize=(10, 5))
    for i, color in enumerate(cluster_colors):
        cluster_points = data_scaled[labels == i]
        if len(cluster_points) >= 3:  # ConvexHull requires at least 3 points
            hull = ConvexHull(cluster_points)
            plt.fill(cluster_points[hull.vertices, 0], cluster_points[hull.vertices, 1], color, alpha=0.3)
        plt.scatter(data_scaled[labels == i, 0], data_scaled[labels == i, 1], c=color, label=f'Cluster {i}', s=10)
    
    if new_data_scaled is not None and new_label is not None:
        plt.scatter(new_data_scaled[0, 0], new_data_scaled[0, 1], color='black', marker='x', s=100, label='New Data Point')

    plt.legend()
    plt.xlabel('Annual Income')
    plt.ylabel('Spending Score')
    st.pyplot(plt)

def main():
    model = load_model()
    if model is None:
        return

    # Load and preprocess the dataset
    dataset = pd.read_csv('data/Mall_Customers.csv').loc[:, ['Annual Income (k$)', 'Spending Score (1-100)']]
    ms = MinMaxScaler()
    data_scaled = ms.fit_transform(dataset)
    labels = model.predict(data_scaled)

    # User input for new data point
    col1, col2 = st.columns(2)

    with col1:
        annual_income = st.number_input('Enter the annual income in the scale of 1000$', value=0.0)
    with col2:
        spending_score = st.number_input('Enter the spending score (1 - 100)', value=0)



    # Check if submit button is clicked
    if st.button('Submit'):
        col1, col2 = st.columns(2)

        with col1:
            # Plot original clustered dataset
            st.markdown('<h3>Original Clusters 🌟</h3>', unsafe_allow_html=True)
            plot_clusters(data_scaled, labels)

        with col2:
            # Predict and plot new data point
            new_data = pd.DataFrame({'Annual Income (k$)': [annual_income], 'Spending Score (1-100)': [spending_score]})
            new_data_scaled = ms.transform(new_data)
            new_label = model.predict(new_data_scaled)[0]

            st.markdown('<h3>New Data Point Prediction 🎯</h3>', unsafe_allow_html=True)
            plot_clusters(data_scaled, labels, new_data_scaled, new_label)

            # Display the cluster of the new data point
            st.markdown(f'<div style="font-size:35px;">The new data point belongs to cluster: {new_label}</div>', unsafe_allow_html=True)
    else:
        # Default plot on initial load
        st.image('images/clustering-2.png', width=750)

if __name__ == '__main__':
    main()
