import streamlit as st
import pandas as pd

# Load predictions
predictions = pd.read_csv(r"C:\Users\sm689\Desktop\2.Resolute_AI_assigment\Task2\all_models_predictions.csv")

st.title('Model Predictions')

# Display predictions for each model
for column in predictions.columns:
    st.header(f'Predictions for {column}')
    st.write(predictions[column])
