import requests
from datetime import datetime, timedelta
from collections import defaultdict

# Function to format the time
def format_time(utc_time):
    return datetime.utcfromtimestamp(utc_time / 1000).strftime('%Y-%m-%d %H:%M:%S UTC')

# Fetch earthquake data from the API
def fetch_earthquake_data():
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=1)
    url = (
        f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"
        f"&starttime={start_time.isoformat()}&endtime={end_time.isoformat()}"
        f"&minmagnitude=4"
    )
    response = requests.get(url)
    data = response.json()
    return data['features']

# Process and display the data
def display_earthquake_data():
    earthquake_data = fetch_earthquake_data()
    country_dict = defaultdict(list)
    
    for quake in earthquake_data:
        props = quake['properties']
        coords = quake['geometry']['coordinates']
        place = props['place']
        magnitude = props['mag']
        time = format_time(props['time'])

        # Extract country and city from the location string
        if ", " in place:
            city, country = place.split(", ")[-2:]
        else:
            city, country = place, "Unknown"

        country_dict[country].append({
            'city': city,
            'latitude': coords[1],
            'longitude': coords[0],
            'magnitude': magnitude,
            'time': time
        })

    # Display the data in alphabetical order by country
    for country in sorted(country_dict.keys()):
        print(f"Country: {country}")
        for quake in country_dict[country]:
            print(f"  City: {quake['city']}")
            print(f"    Coordinates: ({quake['latitude']}, {quake['longitude']})")
            print(f"    Magnitude: {quake['magnitude']}")
            print(f"    Time: {quake['time']}")
        print("\n" + "-"*50 + "\n")

# Run the code
display_earthquake_data()
