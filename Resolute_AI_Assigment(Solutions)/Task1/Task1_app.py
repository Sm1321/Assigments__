import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load data
data = pd.read_excel(r"C:\Users\sm689\Desktop\2.Resolute_AI_assigment\Task1\train.xlsx")
X_test = pd.read_excel(r"C:\Users\sm689\Desktop\2.Resolute_AI_assigment\Task1\test.xlsx")


# Standardize data
scaler = StandardScaler()
X = data.drop(columns = ['target'],axis =1)
X_scaled = scaler.fit_transform(X)

# Fit KMeans model
kmeans = KMeans(n_clusters=2, init='k-means++')
kmeans.fit(X_scaled)

# Function to predict cluster for a new data point
def predict_cluster(data_point):
    scaled_data_point = scaler.transform(data_point.values.reshape(1, -1))
    return kmeans.predict(scaled_data_point)[0]

# Streamlit app
st.title('Task 1 Clustering Streamlit  ')

# Show data
st.subheader('Original Data')
st.write(data.head())

# Show test data
st.subheader('Test Data')
st.write(X_test.head())

# Select a data point from test data
selected_index = st.number_input('Select a row index from Test Data', min_value=0,
                                 max_value=len(X_test)-1, 
                                 value=0, 
                                 step=1)



selected_data_point = X_test.iloc[selected_index]

# Predict cluster for selected data point
predicted_cluster = predict_cluster(selected_data_point)

# Explain why
cluster_centers = kmeans.cluster_centers_
scaled_selected_data_point = scaler.transform(selected_data_point.values.reshape(1, -1))
distances = np.linalg.norm(cluster_centers - scaled_selected_data_point, axis=1)
closest_cluster = np.argmin(distances)

st.subheader('Prediction Results')
st.write(f'The selected data point belongs to cluster {predicted_cluster}')
st.write(f'It is closest to cluster {closest_cluster} with a distance of {distances[predicted_cluster]}')

# Show comparison
st.subheader('Comparison with Cluster Centers')
comparison = pd.DataFrame({
    'Feature': X.columns,
    'New Data Point': selected_data_point.values,
    'Cluster Center': cluster_centers[predicted_cluster]
})


st.write(comparison)
