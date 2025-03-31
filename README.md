# Real-Time Air Quality Monitoring

This project displays real-time air quality information using data from the WAQI API. The dashboard is built with Streamlit and allows users to monitor AQI in any location by entering latitude and longitude.

## Features
- Real-time AQI updates
- Location switcher for custom coordinates
- Color-coded AQI health warnings

## How to Run
1. Install dependencies:
   ```bash
   pip install requests streamlit
streamlit run app.py
API
This project uses the World Air Quality Index (WAQI) API. You need to register for a free API token at https://aqicn.org/api/.
New Feature Added:
📊 AQI Trend Chart – Displays the AQI trend over the last 7 days for better insights into air quality variations.


 AQI Trend Chart 📈

Fetches historical AQI data (last 7 days).

Uses Matplotlib to plot AQI trends.

Helps users understand air pollution patterns.

✅ Better UI & Information 🎨

Clearly shows dominant pollutants.

Displays location details.

✅ Enhanced Error Handling 🚨

Shows an error if AQI data fetching fails.
