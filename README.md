<div align="center">

## Earthquake information

<img alt="Gif" src="https://acropolis-wp-content-uploads.s3.us-west-1.amazonaws.com/2019/02/Hero-Earthquake-Proof-Buildings.gif" height="250px" width="600px">
</div>
<hr>

[Click to see the descriptions in Persian language](Persian.md)

<b>Notice:</b> <b>Each section has a README file in English and Farsi in its respective file. By clicking on the links of each section, you can learn more in-depth information about the code and its function.
<hr>

### 1. Tremor Tracker:
This Python code is designed to retrieve and display recent earthquake information from the United States Geological Survey (USGS) API. It uses the urllib.request library to fetch earthquake data in JSON format from a specified URL. The printResults function processes this data, first printing the title and the number of recorded earthquake events. Then, it lists the locations of all earthquakes and separately displays those with a magnitude of 4.0 or greater. Finally, it checks and prints the number of times the earthquakes were felt in each location. In the main function, after establishing a connection to the URL, the code sends the retrieved data to the printResults function for processing if the request is successful. If there is an error in retrieving the data, an error message is displayed to the user.

To view the file <b>[English README.md](TremorTracker/EnglishTremorTracker.md)</b> and <b>[Persian README.md](TremorTracker/PersianTremorTracker.md)</b> And the complete code <b>[Python Code](TremorTracker/TremorTracker.py)</b>.
<hr>

### 2. Quake Monitor:
This program retrieves earthquake data above a magnitude of 4.0 from the past 24 hours worldwide using the USGS Earthquake API. The fetch_earthquake_data() function constructs a URL to request data in JSON format, filtering by time range and earthquake magnitude. The format_time() function converts the earthquake time from UTC to a readable date and time. Each earthquake entry is processed to extract details such as location, city, country, coordinates, magnitude, and exact time. The data is stored in a dictionary, grouping earthquakes by country and then by city. The display_earthquake_data() function sorts countries alphabetically and prints each country’s information in a readable format. For each country, affected cities, geographic coordinates, magnitude, and time of each earthquake are displayed. This allows users to view recent seismic activity worldwide, organized by country and city.

To view the file <b>[English README.md](QuakeMonitor/EnglishQuakeMonitor.md)</b> and <b>[Persian README.md](QuakeMonitor/PersianQuakeMonitor.md)</b> And the complete code <b>[Python Code](QuakeMonitor/QuakeMonitorEnglish.py)</b>.
<hr>

### 3. Iran Seismo Finder: 
This code is designed to retrieve and display earthquake information from the past month in Iran using the United States Geological Survey (USGS) API. It first calculates the date range by determining today’s date and the date 30 days prior, setting up a one-month time frame. It also specifies the geographical coordinates of Iran to filter data for this specific region.
The code then sends a request to the API, which returns earthquake data in JSON format. If the request is successful, the program proceeds to process the data. For each earthquake, details such as magnitude, location, exact time (date and hour), and geographical coordinates (latitude and longitude) are extracted.
The program also attempts to parse the earthquake’s location to identify the specific province or city within Iran where the earthquake occurred. If the location string includes a precise city or province, it displays this along with other collected information. If a specific location isn’t available, the code displays a more general location name. In case of any issues in retrieving the data, an error message is printed to inform the user of the unsuccessful request.

To view the file <b>[English README.md](IranSeismoFinder/EnglishIranSeismoFinder.md)</b> and <b>[Persian README.md](IranSeismoFinder/PersianIranSeismoFinder.md)</b> And the complete code <b>[Python Code](IranSeismoFinder/IranSeismoFinderEnglish.py)</b>.
<hr>

### 4. Red Dot Quakes:
This Python script visualizes recent global earthquake data on an interactive map. It uses the USGS API to fetch data on earthquakes that occurred in the past 24 hours, displaying only those with a magnitude above 2.5 to ensure relevance. The data includes each earthquake’s location, magnitude, and geographic coordinates. Using the folium library, the script creates an interactive world map centered at (0, 0) with a wide view. Each earthquake is marked as a red dot on the map, representing the epicenter location. Hovering over a marker shows a tooltip with details about the earthquake, including location name, magnitude, and latitude/longitude. The completed map is saved as an HTML file for easy viewing in a web browser, allowing users to explore recent global seismic activity interactively.

To view the file <b>[English README.md](RedDotQuakes/EnglishRedDotQuakes.md)</b> and <b>[Persian README.md](RedDotQuakes/PersianRedDotQuakes.md)</b> And the complete code <b>[Python Code](RedDotQuakes/RedDotQuakesEnglish.py)</b>.
<hr>


## License

MIT

