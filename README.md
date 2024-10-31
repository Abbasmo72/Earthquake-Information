<div align="center">

## Earthquake information

<img alt="Gif" src="https://acropolis-wp-content-uploads.s3.us-west-1.amazonaws.com/2019/02/Hero-Earthquake-Proof-Buildings.gif" height="250px" width="600px">
</div>
<hr>

[Click to see the descriptions in Persian language](Persian.md)
<hr>

## Overview of the Code:
This script is designed to fetch earthquake data from the USGS (United States Geological Survey) using a GeoJSON feed, parse the JSON response, and print relevant information such as the number of events and locations where earthquakes have been felt.

[Seismo Watch](SeismoWatch.py)

## Finding Information:
The code retrieves information from the United States Geological Survey (USGS) website, specifically from the following URL:

<a href="http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson" target="_blank">View Earthquake Data</a>

This URL provides a GeoJSON feed that contains data about recent earthquakes. The specific information passed to the code includes:
1. Metadata: This includes the title of the data set and the count of recorded earthquake events.
2. Features: This section provides details about each earthquake, including:
   Place: The geographical location of the earthquake.<br>
  Magnitude: The strength of the earthquake, which is used to filter significant events (magnitude ≥ 4.0).<br>
  Felt Reports: The number of reports from people who felt the earthquake, if available.

The code processes this data to display the title, total number of recorded events, locations of all earthquakes, locations of significant earthquakes (magnitude ≥ 4.0), and details of earthquakes that were felt by people, along with the count of such reports.



## Libraries:
The code uses the following libraries:
1. json:
  This library is part of Python's standard library and is used to parse JSON (JavaScript Object Notation) data. No need to install this library, as it comes pre-installed with Python.
2. urllib.request:
  This is another standard library module that is used to handle opening and fetching URLs. This library is also included in Python by default, so no installation is needed.

## JSON: What is it and How Does it Work?
JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is commonly used for transmitting data in web applications between a server and a client.
In Python, the json library is used to decode JSON data into a Python dictionary, allowing the program to easily access and manipulate the data.
<hr>

## How the Code Works (Step-by-Step Breakdown):

1. Import Libraries:
```python
import json
import urllib.request
```
The json library is used for working with JSON data.
The urllib.request library is used for making HTTP requests to fetch data from a given URL.

2. Defining the printResults function:
```python
def printResults(data):
```
This function will process the JSON data received from the USGS server and print the desired information.

3. Parse the JSON Data:
```python
theJSON = json.loads(data)
```
The JSON data (in string format) is loaded into a Python dictionary using json.loads(). This allows easy access to the data.

4. Extracting the Title from Metadata:
```python
if 'title' in theJSON['metadata']:
    print(theJSON['metadata']['title'])
```
This checks if the 'title' exists in the metadata and prints it. The title typically gives information about the data source.

5. Counting and Printing Total Events:
```python
count = theJSON['metadata']['count']
print(count, 'events recorded')
```
The script fetches the total count of recorded earthquake events and prints it.

6. Printing All Event Locations:
```python
for i in theJSON['features']:
    print(i['properties']['place'])
```
This loop iterates over all earthquake events (features) and prints the location (place) where each earthquake occurred.

7. Filtering and Printing Significant Events (Magnitude >= 4.0):
```python
for i in theJSON['features']:
    if i['properties']['mag'] >= 4.0:
        print(i['properties']['place'])
```
This loop prints locations of earthquakes with a magnitude greater than or equal to 4.0. These events are more significant because of their higher magnitude.

8. Printing Earthquakes that Were Felt by People:
```python
print('\n Events that were felt:')
for i in theJSON['features']:
    feltReports = i['properties']['felt']
    if feltReports is not None:
        if feltReports > 0:
            print(i['properties']['place'], feltReports, 'times')
```
The code filters the events where people reported feeling the earthquake. If an event was felt, it prints the location and the number of times it was reported.

9. Main Function:
```python
def main():
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))
    if(webUrl.getcode()) == 200:
        data = webUrl.read()
        printResults(data)
    else:
        print('Received an error from the server, cannot print results', webUrl.getcode())
```
The main() function makes an HTTP request to the USGS API to retrieve the latest earthquake data (summary of events with a magnitude of 2.5+ for the past day).
If the request is successful (200 status code), the response data is passed to the printResults() function for processing. If not, it prints an error message.

10. Running the Script:
```python
if __name__ == "__main__":
    main()
```
This block ensures that the main() function is called when the script is executed.

## Python Code
```python

import json
import urllib.request 

def printResults(data):
   
    theJSON = json.loads(data)
    
    if 'title' in theJSON['metadata']:
        print(theJSON['metadata']['title'])
    
    count = theJSON['metadata']['count']
    print(count, 'events recorded')
    
    for i in theJSON['features']:
        print(i['properties']['place'])
    print('---------------------')

    for i in theJSON['features']:
        if i ['properties']['mag'] >= 4.0:
            print(i['properties']['place'])
    print('---------------------')

    print('\n Events that were felt:')
    for i in theJSON['features']:
        feltReports = i['properties']['felt']
        if feltReports != None:
            if feltReports > 0:
                print(i['properties']['place'], feltReports, 'times')
def main():
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib.request.urlopen(urlData)
    print ("result code: " + str(webUrl.getcode()))
    if(webUrl.getcode()) == 200:
        data = webUrl.read()
        printResults(data)
    else:
        print('Received an error from the server, cannot print results', webUrl.getcode())
if __name__ == "__main__":
    main()

```

## Conclusion:
This script retrieves real-time earthquake data from the USGS and processes it to display key information about recent earthquakes, such as:
Title of the dataset
Total number of events
Locations of all recorded events
Locations of events with a magnitude of 4.0 or greater
Locations and counts of events that were felt by people.

<hr>

## License

MIT

