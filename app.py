import streamlit as st
import matplotlib.pyplot as plt
from fetch_data import fetch_air_quality_data

def display_air_quality(data):
    st.title("Real-Time Air Quality Monitoring")
    st.subheader("Current Air Quality Index (AQI)")
    
    # Display the AQI and status
    aqi = data['data']['aqi']
    st.write(f"AQI: {aqi}")
    
    # Determine air quality level
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

    # Additional information
    st.write("Dominant Pollutant:", data['data']['dominentpol'])
    st.write("Location:", data['data']['city']['name'])

    # **New Feature: Historical AQI Trend**
    if 'history' in data['data']:
        history = data['data']['history']
        dates = [entry['date'] for entry in history]
        aqi_values = [entry['aqi'] for entry in history]

        # Plot AQI trend
        fig, ax = plt.subplots()
        ax.plot(dates, aqi_values, marker='o', linestyle='-')
        ax.set_xlabel("Date")
        ax.set_ylabel("AQI")
        ax.set_title("AQI Trend Over Last 7 Days")
        ax.grid(True)
        st.pyplot(fig)

def main():
    st.sidebar.header("Real-Time Air Quality Monitoring")
    st.sidebar.write("Enter coordinates to get AQI for a specific location.")

    # Input fields for latitude and longitude
    latitude = st.sidebar.number_input("Latitude", value=28.6139, format="%.6f")
    longitude = st.sidebar.number_input("Longitude", value=77.2090, format="%.6f")

    # Fetch and display data for the entered coordinates
    city_coords = {"lat": latitude, "lon": longitude}
    data = fetch_air_quality_data(city_coords)
    if data and data['status'] == 'ok':
        display_air_quality(data)
    else:
        st.error("Failed to fetch air quality data. Please check the coordinates.")

if __name__ == "__main__":
    main()
