import streamlit as st
import pandas as pd
import datetime


st.title('NBA Game Predictions')
st.write("Please not that these are only suggestions, and predictions further from the current date will be less accurate.")
#d = st.date_input('Select a Date')
#st.write('Showing Games from ', d)
#df = pd.read_csv('nbaGamePredictions.csv')
#st.write(df[df['GAME_DATE']==d])


# Select a Date
#min_date = datetime.date(2022, 10, 12)
#max_date = datetime.date(2024, 4, 14)
#d = st.date_input('Select a Date', min_value=min_date, max_value=max_date)

min_date = datetime.date(2022, 10, 12)
max_date = datetime.date(2024, 4, 25)
current_date = datetime.date(2024, 4, 23)

# Create the date input widget with the minimum and maximum values
d = st.date_input('Select a Date', min_value=min_date, max_value=max_date, value=current_date)


# Read the DataFrame
df = pd.read_csv('nbaGamePredHistory.csv')
df['Game Date'] = pd.to_datetime(df['Game Date']).dt.date
# Convert 'GAME_DATE' column to datetime
pred_df = pd.read_csv('nbaGamePredictions.csv')
pred_df['Game Date'] = pd.to_datetime(pred_df['Game Date']).dt.date



# Check if 'd' is before the current date
if d < current_date:
    st.write('Showing Games from', d)

    filtered_df = df[df['Game Date'] == d]
    if filtered_df.shape[0] > 0:
        st.write(filtered_df)
    else:
        st.write("There are no NBA Games on this date.")
elif d == current_date:
    st.write('Showing Games from', d)
    st.write("Today's Predictions")
    filtered_df = pred_df[pred_df['Game Date'] == d]
    if filtered_df.shape[0] > 0:
        st.write(filtered_df)
    else:
        st.write("There are no NBA Games on this date.")
else:
    st.write("Showing Predictions for", d)
    filtered_df = pred_df[pred_df['Game Date'] == d]
    if filtered_df.shape[0] > 0:
        st.write(filtered_df)
    else:
        st.write("There are no NBA Games on this date.")


# Filter DataFrame based on selected date
#filtered_df = df[df['Game Date'] == d]

# Show filtered DataFrame
#st.write(filtered_df)
