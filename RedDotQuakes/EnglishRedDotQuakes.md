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
