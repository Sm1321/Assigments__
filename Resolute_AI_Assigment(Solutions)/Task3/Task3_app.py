import pandas as pd
import numpy as np
import streamlit as st



# Function to process data
def process_data():
    # Load raw data
    df = pd.read_excel(r"C:\Users\sm689\Desktop\2.Resolute_AI_assigment\Task3\rawdata.xlsx")

    # Convert 'date' and 'time' columns to string if they are not already
    df['date'] = df['date'].astype(str)
    df['time'] = df['time'].astype(str)

    # Combine 'date' and 'time' columns to create a 'timestamp' column
    df['timestamp'] = pd.to_datetime(df['date'] + ' ' + df['time'])

    # Sort by timestamp
    df = df.sort_values(by='timestamp')

    # Calculate duration between consecutive events
    df['duration'] = df['timestamp'].diff().dt.total_seconds().fillna(0)

    # Extract date from timestamp
    df['date'] = df['timestamp'].dt.date

    # Normalize location names to lowercase
    df['location'] = df['location'].str.lower()

    #df.columns
    # Calculate the total duration for each "inside" and "outside" on a datewise basis
    filtered_df = df[df['position'].isin(['inside', 'outside'])]
    group_duration = filtered_df.groupby(['date', 'location'])['duration'].sum()
    inside_outside_duration = group_duration.unstack(fill_value=0)


    # Count the number of "picking" and "placing" activities for each date
    filtered_activity_df = df[df['activity'].isin(['picking', 'placed'])]
    group_activity_count = filtered_activity_df.groupby(['date', 'activity']).size()
    picking_placing_count = group_activity_count.unstack(fill_value=0)

    return inside_outside_duration, picking_placing_count


# Call the Function Process the data
inside_outside_duration, picking_placing_count = process_data()

# Streamlit app
st.title("Task 3: Use rawdata as input and derive(Using Streamlit)")

st.header("1.Datewise Total Duration for Inside and Outside")
st.dataframe(inside_outside_duration)

st.header("2.Datewise Number of Picking and Placing Activities")
st.dataframe(picking_placing_count)







