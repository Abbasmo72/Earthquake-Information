<div align="center">

## Quake Monitor

<img src="https://vancouver.citynews.ca/wp-content/blogs.dir/sites/9/2024/10/30/Oregon-Earthquake-Pacific-Oct-30-1024x576.jpg" alt="Image Description" width="50%">

</div>
<hr>

[Click to see the descriptions in Persian language](PersianQuakeMonitor.md)
<hr>

## Overview of the Code
The code is designed to track global earthquake activity above a magnitude of 4.0 over the past 24 hours, leveraging data from the US Geological Survey (USGS) Earthquake API. It includes three main components:

1. Data Retrieval: The fetch_earthquake_data() function builds a URL to fetch earthquake data in JSON format from the USGS API, filtering based on a minimum magnitude of 4.0 and a 24-hour timeframe. This ensures the data is recent and only includes significant seismic events.
2. Data Processing: After receiving the JSON data, each earthquake entry is processed to extract essential details such as location, country, city (if available), geographic coordinates, magnitude, and the exact time of occurrence. The data is stored in a dictionary that groups earthquakes by country, making it easier to organize and display by location.
3. Displaying Data: The display_earthquake_data() function sorts the countries alphabetically and prints the earthquake information for each country. For each entry, it shows the affected cities, coordinates, magnitude, and exact time, creating a clear and organized summary of seismic events worldwide.

This program provides a concise and structured view of recent global earthquake activity, grouped by country and city, enabling users to track significant seismic events in a reader-friendly format.

## How the Code Works (Step-by-Step Breakdown)
1. Importing Libraries:
   - requests: Used to send HTTP requests to the API.
   - datetime and timedelta: Used for working with dates and times, and calculating the start and end times.
   - defaultdict: A type of dictionary from the collections module that automatically creates a default value (a list in this case) for missing keys.
```python
import requests
from datetime import datetime, timedelta
from collections import defaultdict
```
2. Defining the format_time function:
  This function formats the utc_time input (which is in milliseconds) into a readable format:
   - The time is first converted into seconds (by dividing by 1000).
   - Then, using datetime.utcfromtimestamp(), it is converted to a UTC date-time object.
   - Finally, the time is formatted to YYYY-MM-DD HH:MM:SS UTC.
```python
def format_time(utc_time):
    return datetime.utcfromtimestamp(utc_time / 1000).strftime('%Y-%m-%d %H:%M:%S UTC')
```
3. Defining the fetch_earthquake_data function:
   - Start and End Time: The end_time is set to the current UTC time, and the start_time is calculated as 24 hours before the end_time using timedelta.
   - URL Construction: The URL for the API request is built, including parameters such as the data format (geojson), start and end times, and a minimum magnitude of 4 for the earthquakes.
   - Request and Response: The data is fetched from the USGS Earthquake API using requests.get(url), and the response is converted to JSON.
   - Return Data: The earthquake features are returned from the API response.
```python
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
```
4. Defining the display_earthquake_data function:
- Fetching Data: The earthquake data is fetched using the fetch_earthquake_data function.
- Creating country_dict: A defaultdict is created to store earthquake data categorized by country and city.
- Processing Each Earthquake: For each earthquake in the data, the following information is extracted:
   - props: Contains earthquake properties like location, magnitude, and time.
   - coords: Contains the geographical coordinates (latitude and longitude).
   - place: The location of the earthquake.
   - magnitude: The magnitude of the earthquake.
   - time: The time of the earthquake, which is formatted using the format_time function.
```python
def display_earthquake_data():
    earthquake_data = fetch_earthquake_data()
    country_dict = defaultdict(list)
    
    for quake in earthquake_data:
        props = quake['properties']
        coords = quake['geometry']['coordinates']
        place = props['place']
        magnitude = props['mag']
        time = format_time(props['time'])
```
5. Categorizing Earthquakes by Country:
   - Location Parsing: The location (place) is split into city and country parts. If the location includes a comma, it is assumed to be in the format "City, Country". If not, the country      is set as "Unknown".
   - Storing Data: The earthquake data is added to country_dict, with the country as the key and a list of earthquake details (city, coordinates, magnitude, and time) as the value.
```python
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
```
6. Displaying the Data:
   - Sorting and Displaying: The countries are sorted alphabetically, and the earthquake details are printed for each country.
   - For each country, the list of earthquakes is displayed with information such as city, coordinates, magnitude, and time.
   - A separator line is printed between countries for better readability.
```python
    for country in sorted(country_dict.keys()):
        print(f"Country: {country}")
        for quake in country_dict[country]:
            print(f"  City: {quake['city']}")
            print(f"    Coordinates: ({quake['latitude']}, {quake['longitude']})")
            print(f"    Magnitude: {quake['magnitude']}")
            print(f"    Time: {quake['time']}")
        print("\n" + "-"*50 + "\n")
```
7. Running the Code:
   - This line calls the display_earthquake_data function to execute the program and display the earthquake data.
```python
display_earthquake_data()
```

### Summary
This code fetches earthquake data from the USGS API for earthquakes with a magnitude of 4 or higher that occurred in the last 24 hours. It categorizes the data by country and city and displays details such as location, magnitude, coordinates, and time for each earthquake, sorted alphabetically by country.

# Python Code
```python
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
```


