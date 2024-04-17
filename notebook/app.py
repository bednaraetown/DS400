import streamlit as st
import pandas as pd

st.title('NBA Game Predictions')

#d = st.date_input('Select a Date')
#st.write('Showing Games from ', d)
#df = pd.read_csv('nbaGamePredictions.csv')
#st.write(df[df['GAME_DATE']==d])


# Select a Date
d = st.date_input('Select a Date')

# Show selected date
st.write('Showing Games from', d)

# Read the DataFrame
df = pd.read_csv('nbaGamePredHistory.csv')

# Convert 'GAME_DATE' column to datetime
df['Game Date'] = pd.to_datetime(df['Game Date']).dt.date

# Filter DataFrame based on selected date
filtered_df = df[df['Game Date'] == d]

# Show filtered DataFrame
st.write(filtered_df)
