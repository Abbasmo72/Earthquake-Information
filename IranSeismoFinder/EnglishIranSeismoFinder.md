<div align="center">

## Iran Seismo Finder

<img src="https://images.khabaronline.ir/images/2016/3/16-3-25-1345132028858.jpg" alt="Image Description" width="40%">

</div>
<hr>

[Click to see the descriptions in Persian language](PersianIranSeismoFinder.md)
<hr>

## Overview of the Code
1. Date Range Calculation:
   - The script calculates the date range for the past month by determining today’s date and subtracting 30 days to define the start of the period. This ensures the query retrieves       earthquake data from the last 30 days.
2. Geographical Filtering:
   - The code specifies the geographical boundaries of Iran using its latitude and longitude coordinates. This ensures that only earthquakes within Iran’s borders are included in the data retrieval.
3. API Request Setup:
   - It sends a request to the USGS Earthquake API with the calculated date range and geographical parameters. The query fetches earthquake data in GeoJSON format, which includes detailed information about each event.
4. Data Extraction:
   - After receiving the response from the API, the script processes the JSON data. It extracts key details such as the earthquake’s magnitude, location, time of occurrence, and geographical coordinates (latitude and longitude).
5. Location Parsing:
   - The script attempts to extract the specific province or city from the location string for each earthquake. This is done by splitting the location into parts and extracting the relevant region (province or city) within Iran.
6. Output Information:
   - The extracted information for each earthquake, including magnitude, location, exact time, and coordinates, is displayed to the user in a readable format. If the location string does not provide enough details, the full location is displayed instead.
7. Error Handling:
   - In the case of an unsuccessful API request or any issues in retrieving the data, the script will output an error message to inform the user that something went wrong.
8. User-Friendly Output:
   - The code ensures that the information is presented clearly, providing users with earthquake details including both general and specific location data, as well as time and magnitude.
  
## How the Code Works (Step-by-Step Breakdown):
1. Importing the Required Library:
   - The requests library is imported to send HTTP requests to the USGS Earthquake API and handle the response. This library makes it easier to interact with APIs by providing simple methods for making requests and handling responses.
```python
import requests
```
2. Defining the Function:
   - This function get_iran_earthquakes is where all the logic for fetching, processing, and displaying earthquake data is contained. It's defined so it can be called whenever needed to get earthquake data.
```python
def get_iran_earthquakes():
```
3. Calculating the Date Range:
   - This section calculates the date range for the past 30 days. The start_date is computed by subtracting 30 days from the current date using datetime.timedelta. The end_date is set as today's date. These dates are formatted into the required string format (YYYY-MM-DD).
```python
start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
end_date = datetime.datetime.now().strftime('%Y-%m-%d')
```
4. Setting Geographical Parameters for Iran:
- The params dictionary contains the parameters to be sent in the request to the USGS Earthquake API. These include:
   - format: Specifies that the response should be in GeoJSON format.
   - starttime and endtime: Set the date range for the past 30 days.
   - minlatitude, maxlatitude, minlongitude, and maxlongitude: These parameters define the geographical bounds of Iran, ensuring only earthquakes within this region are returned.
```python
params = {
    'format': 'geojson',
    'starttime': start_date,
    'endtime': end_date,
    'minlatitude': 24.396308,
    'maxlatitude': 39.148174,
    'minlongitude': 44.396216,
    'maxlongitude': 63.246158
}
```
5. Sending the API Request:
   - The requests.get method sends an HTTP GET request to the USGS Earthquake API using the specified URL and parameters. The response from the API is stored in the response object.
```python
response = requests.get(url, params=params)
```
6.  Checking the Response Status:
   - This checks if the request was successful by evaluating the status code. A status code of 200 indicates that the request was successful and data is available.
```python
if response.status_code == 200:
```
7. Processing the JSON Data:
   - If the request was successful, the response content is parsed into a JSON object using response.json(). The earthquakes list is extracted from the features key in the JSON response, which contains the data for each earthquake.
```python
data = response.json()
earthquakes = data['features']
```
8. Extracting Earthquake Details:
- This loop iterates through each earthquake in the earthquakes list. For each earthquake, it extracts:
   - magnitude: The magnitude of the earthquake from the properties section.
   - location: The string describing the location of the earthquake from the properties section.
```python
for quake in earthquakes:
    magnitude = quake['properties']['mag']
    location = quake['properties']['place']
```
9. Parsing the Location:
    - The code tries to parse the location string to extract the province or city. The location string is split by commas, and if there are multiple parts, it takes the second-to-last part as the province or city. This part is stripped of any leading or trailing whitespace. If there’s no city/province information, it simply prints the full location string.
```python
parts = location.split(',')
if len(parts) > 1:
    city_province = parts[-2].strip()
    print(f'Magnitude: {magnitude}, Location: {city_province}, Full Location: {location}')
else:
    print(f'Magnitude: {magnitude}, Location: {location}')
```
10. Error Handling:
    - If the request to the API fails (i.e., the status code is not 200), this line ensures an error message is printed indicating that data could not be fetched.
```python
else:
    print('Error fetching data')
```
11. Calling the Function:
    - This line calls the get_iran_earthquakes function, executing the code within it to fetch and display earthquake data for the past month in Iran.
```python
get_iran_earthquakes()
```

Each section of the code is responsible for a specific task, from calculating the date range to displaying the earthquake information. The code retrieves earthquake data from an API, processes it, and presents it in a readable format for the user.

## Python Code:
```python
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
```
