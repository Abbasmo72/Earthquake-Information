import folium
import requests
from datetime import datetime, timedelta

# دریافت داده‌های زلزله‌های جهان در ۲۴ ساعت گذشته از USGS
url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
params = {
    "format": "geojson",
    "starttime": (datetime.utcnow() - timedelta(days=1)).isoformat(),
    "endtime": datetime.utcnow().isoformat(),
    "minmagnitude": 2.5  # حداقل شدت زلزله برای نمایش
}
response = requests.get(url, params=params)
data = response.json()

# ایجاد نقشه تعاملی
world_map = folium.Map(location=[0, 0], zoom_start=2)

# افزودن نقاط زلزله به نقشه
for earthquake in data["features"]:
    coords = earthquake["geometry"]["coordinates"]
    place = earthquake["properties"]["place"]
    mag = earthquake["properties"]["mag"]
    lat, lon = coords[1], coords[0]
    
    # اضافه کردن هر نقطه زلزله به نقشه
    folium.CircleMarker(
        location=[lat, lon],
        radius=5,
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=0.6,
        tooltip=f"<strong>Location:</strong> {place}<br><strong>Magnitude:</strong> {mag}<br><strong>Coordinates:</strong> ({lat}, {lon})"
    ).add_to(world_map)

# ذخیره نقشه به فایل HTML
world_map.save("world_earthquakes_map.html")
print("نقشه زلزله‌ها در فایل world_earthquakes_map.html ذخیره شد.")
