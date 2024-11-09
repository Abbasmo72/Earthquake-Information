<div align="center">

## لرزش نقطه قرمز

<img src="https://preview.redd.it/hi-data-scientist-getting-into-earthquakes-apr-2022-2023-v0-v7vma0wrt5ta1.png?auto=webp&s=eb551b31278c792052c59897ccbe9f95e49acbd5" alt="Image Description" width="40%">

</div>
<hr>

[Click to see the descriptions in English language](EnglishRedDotQuakes.md)
<hr>

## مروری بر کد
این کد پایتون داده‌های زلزله‌های سراسر جهان در ۲۴ ساعت گذشته را از طریق API سازمان زمین‌شناسی ایالات متحده (USGS) دریافت کرده و آن‌ها را بر روی یک نقشه تعاملی با استفاده از کتابخانه folium نمایش می‌دهد. در اینجا توضیح هر بخش از کد آورده شده است:
1. وارد کردن کتابخانه‌ها:
   - کتابخانه‌های folium برای نمایش نقشه، requests برای ارسال درخواست HTTP به API و datetime برای کار با تاریخ و زمان وارد شده‌اند.
2. دریافت داده‌های زلزله:
   - ابتدا URL برای نقطه انتهایی API زلزله‌های USGS تعریف می‌شود.
   - پارامترهای درخواست شامل زمان شروع و پایان برای ۲۴ ساعت گذشته به فرمت ISO و حداقل بزرگی زلزله ۲.۵ تنظیم می‌شود.
   - درخواست GET به API ارسال می‌شود و پاسخ JSON در متغیر data ذخیره می‌شود.
3. ایجاد نقشه تعاملی:
   - یک شی folium.Map به نام world_map ایجاد می‌شود که مرکز آن بر روی مختصات جهانی [0, 0] قرار دارد و سطح زوم آن به اندازه‌ای است که نقشه جهانی نمایش داده شود.
4. افزودن داده‌های زلزله به نقشه:
   - کد به ازای هر زلزله در داده‌های دریافت شده، مختصات، مکان و بزرگی آن را استخراج می‌کند.
   - برای هر زلزله، یک folium.CircleMarker به نقشه اضافه می‌شود که از نشانگرهای قرمز با ابزار نمایش (tooltip) استفاده می‌کند که اطلاعات مکان، بزرگی و مختصات زلزله را نمایش می‌دهد.
5. ذخیره نقشه:
   - در نهایت، نقشه به یک فایل HTML به نام "world_earthquakes_map.html" ذخیره می‌شود.
   - کد پیامی را چاپ می‌کند که نشان می‌دهد نقشه با موفقیت ذخیره شده است.

نتیجه نهایی یک فایل HTML است که نقشه تعاملی نمایش‌دهنده زلزله‌های اخیر با جزئیات مکان و بزرگی هر زلزله است که با قرار گرفتن روی هر نشانگر نمایش داده می‌شود.
<hr>

### نمونه نقشه زلزله ها
[کلیک کنید](sampleMap.JPG)

<hr>

## چگونه کد کار می کند (تجزیه گام به گام)
1. وارد کردن کتابخانه‌های مورد نیاز:
   - کتابخانه folium: برای ایجاد نقشه‌های تعاملی استفاده می‌شود. این کتابخانه به شما امکان اضافه کردن نشانگرها و سفارشی کردن نقشه‌ها را می‌دهد.
   - کتابخانه requests: برای ارسال درخواست‌های HTTP به APIهای خارجی (در اینجا API داده‌های زلزله USGS) استفاده می‌شود.
   - کتابخانه datetime و timedelta: برای کار با تاریخ و زمان به کار می‌روند، به ویژه برای دریافت داده‌های ۲۴ ساعت گذشته.
```python
import folium
import requests
from datetime import datetime, timedelta
```
2. دریافت داده‌های زلزله:
   - دریافت داده‌ه url: این آدرس برای API زلزله‌های USGS است که داده‌ها را به صورت GeoJSON فراهم می‌کند.
   - یک دیکشنری params:  که پارامترهای درخواست را مشخص می‌کند.
```python
url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
params = {
    "format": "geojson",
    "starttime": (datetime.utcnow() - timedelta(days=1)).isoformat(),
    "endtime": datetime.utcnow().isoformat(),
    "minmagnitude": 2.5  # حداقل بزرگی زلزله برای نمایش
}
response = requests.get(url, params=params)
data = response.json()
```
3. ایجاد نقشه:
   - این خط folium.Map(): یک نقشه جدید ایجاد می‌کند که مرکز آن در مختصات [0, 0] (نزدیک به خط استوا و نصف‌النهار اصلی) است و سطح زوم آن ۲ است که باعث می‌شود نقشه به گونه‌ای نمایش داده شود که تمام دنیا قابل مشاهده باشد.
```python
world_map = folium.Map(location=[0, 0], zoom_start=2)
```
4. افزودن داده‌های زلزله به نقشه:
```python
for earthquake in data["features"]:
    coords = earthquake["geometry"]["coordinates"]
    place = earthquake["properties"]["place"]
    mag = earthquake["properties"]["mag"]
    lat, lon = coords[1], coords[0]
    
    # افزودن هر نقطه زلزله به نقشه
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
5. ذخیره نقشه به یک فایل HTML:
   - ایجاد فایل world_map.save("world_earthquakes_map.html"): نقشه ساخته شده را به یک فایل HTML به نام "world_earthquakes_map.html" ذخیره می‌کند. این فایل را می‌توان در هر مرورگری باز کرده و نقشه تعاملی را مشاهده کرد.
```python
world_map.save("world_earthquakes_map.html")
```
6. چاپ پیام تایید:
```python
print("Earthquake map saved to world_earthquakes_map.html")
```
### نتیجه نهایی:
  - این کد یک نقشه تعاملی از جهان ایجاد می‌کند که داده‌های زلزله‌های ۲۴ ساعت گذشته را نمایش می‌دهد. هر زلزله با یک نشانگر دایره‌ای قرمز روی نقشه نمایش داده می‌شود.
  - با قرار گرفتن موس روی هر نشانگر، اطلاعات مربوط به مکان، بزرگی و مختصات زلزله نمایش داده می‌شود.
  - نقشه به صورت یک فایل HTML ذخیره می‌شود که می‌توان آن را در هر مرورگری باز کرد.

## کد پایتون
```python
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
```
