import requests

def fetch_air_quality_data(city):
    # Replace 'YOUR_API_TOKEN' with the actual token from WAQI
    api_token = "7f3ea4f852e884a59ba5ff0eba73e19db9456ddd"
    url = f"https://api.waqi.info/feed/geo:{city['lat']};{city['lon']}/?token={api_token}"
    response = requests.get(url)
    
    # Print response details for debugging
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data.")
        return None

city_coords = {"lat": 28.6139, "lon": 77.2090}  # Coordinates for New Delhi
data = fetch_air_quality_data(city_coords)
print("Fetched Data:", data)
