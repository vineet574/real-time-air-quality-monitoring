import streamlit as st
import matplotlib.pyplot as plt
from fetch_data import fetch_air_quality_data
import pandas as pd

def display_air_quality(data, days):
    st.title("Real-Time Air Quality Monitoring")
    st.subheader("Current Air Quality Index (AQI)")
    aqi = data['data']['aqi']
    st.write(f"AQI: {aqi}")
    
    if aqi <= 50:
        st.success("Air Quality: Good")
    elif aqi <= 100:
        st.info("Air Quality: Moderate")
    elif aqi <= 150:
        st.warning("Air Quality: Unhealthy for Sensitive Groups")
    elif aqi <= 200:
        st.warning("Air Quality: Unhealthy")
    else:
        st.error("Air Quality: Very Unhealthy")

    st.write("Dominant Pollutant:", data['data']['dominentpol'])
    st.write("Location:", data['data']['city']['name'])

    if 'history' in data['data']:
        history = data['data']['history'][:days]
        dates = [entry['date'] for entry in history]
        aqi_values = [entry['aqi'] for entry in history]

        fig, ax = plt.subplots()
        ax.plot(dates, aqi_values, marker='o', linestyle='-')
        ax.set_xlabel("Date")
        ax.set_ylabel("AQI")
        ax.set_title(f"AQI Trend Over Last {days} Days")
        ax.grid(True)
        st.pyplot(fig)

        
        st.download_button(
            label="Download AQI Data as CSV",
            data=pd.DataFrame(history).to_csv(index=False),
            file_name="aqi_data.csv",
            mime="text/csv",
        )

def main():
    st.sidebar.header("Real-Time Air Quality Monitoring")
    st.sidebar.write("Enter coordinates to get AQI for a specific location.")
    latitude = st.sidebar.number_input("Latitude", value=28.6139, format="%.6f")
    longitude = st.sidebar.number_input("Longitude", value=77.2090, format="%.6f")

    days = st.sidebar.slider("Select Number of Days for Historical AQI", min_value=1, max_value=7, value=3)
    city_coords = {"lat": latitude, "lon": longitude}
    data = fetch_air_quality_data(city_coords)
    if data and data['status'] == 'ok':
        display_air_quality(data, days)
    else:
        st.error("Failed to fetch air quality data. Please check the coordinates.")

if __name__ == "__main__":
    main()
