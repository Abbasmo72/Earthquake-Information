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
