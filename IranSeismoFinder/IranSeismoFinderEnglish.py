import requests
from datetime import datetime, timedelta

def get_iran_earthquakes():
    # URL for the USGS Earthquake API
    url = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
    
    # Calculate the start and end dates for the last 30 days
    end_date = datetime.utcnow()  # Today's date in UTC
    start_date = end_date - timedelta(days=30)  # Date 30 days ago
    
    # Parameters for the API request
    params = {
        'format': 'geojson',
        'starttime': start_date.strftime('%Y-%m-%d'),  # Start date (30 days ago)
        'endtime': end_date.strftime('%Y-%m-%d'),      # End date (today)
        'minlatitude': 24.396308,     # Minimum latitude for Iran
        'maxlatitude': 39.148174,     # Maximum latitude for Iran
        'minlongitude': 44.396216,     # Minimum longitude for Iran
        'maxlongitude': 63.246158      # Maximum longitude for Iran
    }
    
    # Make a request to the API
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        earthquakes = data['features']
        
        for quake in earthquakes:
            magnitude = quake['properties']['mag']
            location = quake['properties']['place']
            quake_time = datetime.utcfromtimestamp(quake['properties']['time'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
            coordinates = quake['geometry']['coordinates']
            longitude = coordinates[0]
            latitude = coordinates[1]
            
            # Attempt to extract province and city from the location string
            if 'Iran' in location:
                # Basic parsing logic to extract the city/province
                parts = location.split(',')
                if len(parts) > 1:
                    city_province = parts[-2].strip()  # Get the second last part
                    print(f'Magnitude: {magnitude}, Location: {city_province}, Full Location: {location}, Date: {quake_time}, Latitude: {latitude}, Longitude: {longitude}')
                else:
                    print(f'Magnitude: {magnitude}, Location: {location}, Date: {quake_time}, Latitude: {latitude}, Longitude: {longitude}')
    else:
        print('Error fetching data')

# Call the function
get_iran_earthquakes()
