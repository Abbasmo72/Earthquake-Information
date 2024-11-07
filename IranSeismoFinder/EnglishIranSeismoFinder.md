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
