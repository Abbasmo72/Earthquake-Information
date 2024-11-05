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
To view the file <b>[English README.md](TremorTracker/EnglishTremorTracker.md)</b> and <b>[Persian README.md](TremorTracker/PersianTremorTracker.md)</b> In the case of the full code of the game <b>[Python Code](TremorTracker/TremorTracker.py)</b>.
<hr>


## License

MIT

