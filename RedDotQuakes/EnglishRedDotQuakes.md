<div align="center">

## Red Dot Quakes

<img src="https://preview.redd.it/hi-data-scientist-getting-into-earthquakes-apr-2022-2023-v0-v7vma0wrt5ta1.png?auto=webp&s=eb551b31278c792052c59897ccbe9f95e49acbd5" alt="Image Description" width="40%">

</div>
<hr>

[Click to see the descriptions in Persian language](PersianRedDotQuakes.md)
<hr>

## Overview of the Code
This Python code fetches worldwide earthquake data from the past 24 hours, using the US Geological Survey (USGS) API, and visualizes it on an interactive map with folium. Here’s an overview of each section:

1. <b>Import Libraries:</b>
   - The code imports folium for map visualization, requests for making HTTP requests to the API, and datetime for working with date and time values.
2. <b>Fetch Earthquake Data:</b>
   - It defines a URL for the USGS earthquake API endpoint.
   - Parameters for the API request include the start and end times for the past 24 hours, formatted as ISO strings, and a minimum magnitude of 2.5.
   - An HTTP GET request is sent to fetch data, and the JSON response is stored in data.
3. <b>Create Interactive Map:</b>
   - A folium.Map object named world_map is created, centered on the global coordinates [0, 0] with a zoom level that shows the whole world.
4. <b>Add Earthquake Data to the Map:</b>
   - The code iterates through each earthquake in the fetched data.
   - For each earthquake, it retrieves the coordinates, place name, and magnitude.
   - A folium.CircleMarker is added to the map for each earthquake, using red markers with a tooltip that shows the location, magnitude, and coordinates.
5. <b>Save the Map:</b>
   - Finally, the map is saved to an HTML file named "world_earthquakes_map.html".
   - The code prints a confirmation message once the map is saved.
  
The result is an HTML file with an interactive map that displays recent earthquakes with details on location and magnitude when each marker is hovered over.
<hr>

### Sample Map

[Click Sampel Map](sampleMap.JPG)
<hr>

## How the Code Works (Step-by-Step Breakdown) code
1. Import Required Libraries:
   - folium: Used to create interactive maps. It helps in placing markers and customizing maps.
   - requests: Used to send HTTP requests to external APIs (in this case, the USGS earthquake data API).
   - datetime and timedelta: These modules are used to handle time and dates, specifically to get data from the past 24 hours.
```python
import folium
import requests
from datetime import datetime, timedelta
```
2. Fetch Earthquake Data:
   - url: This is the endpoint URL for the USGS Earthquake API, which provides earthquake data in GeoJSON format.
   - params: A dictionary that defines the parameters for the API request:
        - format: Specifies the format of the response (GeoJSON in this case).
        - starttime: The starting time for the query (24 hours before the current time).
        - endtime: The ending time for the query (the current time).
        - minmagnitude: Specifies the minimum earthquake magnitude to display (in this case, 2.5 or higher).
   - requests.get(): Sends the HTTP GET request to the API with the specified parameters.
   - response.json(): Parses the JSON response from the API into a Python dictionary.
```python
url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
params = {
    "format": "geojson",
    "starttime": (datetime.utcnow() - timedelta(days=1)).isoformat(),
    "endtime": datetime.utcnow().isoformat(),
    "minmagnitude": 2.5  # Minimum earthquake magnitude to display
}
response = requests.get(url, params=params)
data = response.json()
```
3. Create the Map:
   - folium.Map(): Creates a new map centered at latitude 0 and longitude 0 (which is near the equator and prime meridian) with an initial zoom level of 2. This zoom level ensures that the whole world is visible on the map.
```python
world_map = folium.Map(location=[0, 0], zoom_start=2)
```
4. Add Earthquake Data to the Map:
   - for earthquake in data["features"]:: Loops through each earthquake feature in the features array from the GeoJSON data.
   - Extracting Information: For each earthquake:
        - coords: Retrieves the earthquake's geographic coordinates (longitude, latitude).
        - place: The location description of the earthquake.
        - mag: The magnitude of the earthquake.
        - lat, lon = coords[1], coords[0]: Assigns the latitude and longitude from the coords array (GeoJSON format stores coordinates as [longitude, latitude]).
   - folium.CircleMarker(): Adds a red circle marker on the map at the earthquake's location. The parameters:
        - location=[lat, lon]: Sets the position of the marker.
        - radius=5: Sets the size of the circle marker.
        - color="red": Sets the border color of the circle.
        - fill=True: Fills the circle with color.
        - fill_color="red": Sets the fill color to red.
        - fill_opacity=0.6: Sets the transparency of the fill color (0 is fully transparent, 1 is fully opaque).
        - tooltip=...: Displays a tooltip when hovering over the marker, showing the earthquake’s location, magnitude, and coordinates.
   - .add_to(world_map): Adds the marker to the map.
```python
for earthquake in data["features"]:
    coords = earthquake["geometry"]["coordinates"]
    place = earthquake["properties"]["place"]
    mag = earthquake["properties"]["mag"]
    lat, lon = coords[1], coords[0]
    
    # Add each earthquake point to the map
    folium.CircleMarker(
        location=[lat, lon],
        radius=5,
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=0.6,
        tooltip=f"<strong>Location:</strong> {place}<br><strong>Magnitude:</strong> {mag}<br><strong>Coordinates:</strong> ({lat}, {lon})"
    ).add_to(world_map)
```
5. Save the Map to an HTML File:
   - world_map.save("world_earthquakes_map.html"): Saves the generated map as an HTML file named "world_earthquakes_map.html". This file can be opened in any web browser to view the interactive map.
```python
world_map.save("world_earthquakes_map.html")
```
6. Print Confirmation:
   - print(): Prints a message confirming that the map has been saved successfully.

### Final Outcome:
   - The code creates an interactive map of the world with earthquake data from the past 24 hours, with each earthquake represented by a red circle marker on the map.
   - When you hover over each marker, a tooltip shows detailed information (location, magnitude, coordinates).
   - The map is saved as an HTML file that you can view in any web browser.

## Python Code
```python
import folium
import requests
from datetime import datetime, timedelta

# Fetch earthquake data worldwide for the past 24 hours from USGS
url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
params = {
    "format": "geojson",
    "starttime": (datetime.utcnow() - timedelta(days=1)).isoformat(),
    "endtime": datetime.utcnow().isoformat(),
    "minmagnitude": 2.5  # Minimum earthquake magnitude to display
}
response = requests.get(url, params=params)
data = response.json()

# Create an interactive map
world_map = folium.Map(location=[0, 0], zoom_start=2)

# Add earthquake points to the map
for earthquake in data["features"]:
    coords = earthquake["geometry"]["coordinates"]
    place = earthquake["properties"]["place"]
    mag = earthquake["properties"]["mag"]
    lat, lon = coords[1], coords[0]
    
    # Add each earthquake point to the map
    folium.CircleMarker(
        location=[lat, lon],
        radius=5,
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=0.6,
        tooltip=f"<strong>Location:</strong> {place}<br><strong>Magnitude:</strong> {mag}<br><strong>Coordinates:</strong> ({lat}, {lon})"
    ).add_to(world_map)

# Save the map to an HTML file
world_map.save("world_earthquakes_map.html")
print("Earthquake map saved to world_earthquakes_map.html")
```
