<div align="center">

## مانیتور زلزله

<img src="https://vancouver.citynews.ca/wp-content/blogs.dir/sites/9/2024/10/30/Oregon-Earthquake-Pacific-Oct-30-1024x576.jpg" alt="Image Description" width="50%">

</div>
<hr>

[Click to see the descriptions in Engilish language](EnglishQuakeMonitor.md)
<hr>


## مروری بر کد:
این کد برای ردیابی فعالیت زمین لرزه های جهانی بالاتر از بزرگی 4.0 در 24 ساعت گذشته طراحی شده است و از داده های سازمان زمین شناسی ایالات متحده (USGS) زلزله API استفاده می کند. شامل سه جزء اصلی است:

1. بازیابی داده: تابع fetch_earthquake_data() یک URL برای واکشی داده‌های زلزله در قالب JSON از USGS API ایجاد می‌کند و براساس حداقل بزرگی 4.0 و بازه زمانی 24 ساعته فیلتر می‌شود. این تضمین می‌کند که داده‌ها جدید هستند و فقط رویدادهای لرزه‌ای مهم را شامل می‌شوند.
2. پردازش داده ها: پس از دریافت داده های JSON، هر ورودی زلزله برای استخراج جزئیات ضروری مانند مکان، کشور، شهر (در صورت وجود)، مختصات جغرافیایی، بزرگی و زمان دقیق وقوع پردازش می شود. داده ها در فرهنگ لغتی ذخیره می شوند که زمین لرزه ها را بر اساس کشور گروه بندی می کند و سازماندهی و نمایش بر اساس مکان را آسان تر می کند.
3. نمایش داده ها: تابع display_earthquake_data() کشورها را بر اساس حروف الفبا مرتب می کند و اطلاعات زلزله را برای هر کشور چاپ می کند. برای هر ورودی، شهرهای آسیب‌دیده، مختصات، بزرگی و زمان دقیق را نشان می‌دهد و خلاصه‌ای واضح و سازمان‌یافته از رویدادهای لرزه‌ای در سراسر جهان ایجاد می‌کند.

این برنامه یک نمای مختصر و ساختاریافته از فعالیت‌های زلزله‌های اخیر جهانی را ارائه می‌کند که بر اساس کشور و شهر گروه‌بندی شده است و کاربران را قادر می‌سازد رویدادهای لرزه‌ای مهم را در قالبی خواننده پسند ردیابی کنند.

## چگونه کد کار می کند (تجزیه گام به گام):
1. وارد کردن کتابخانه‌ها:
   - کتابخانه requests: برای ارسال درخواست HTTP به API استفاده می‌شود.
   - کتابخانه datetime و timedelta: برای کار با تاریخ و زمان و محاسبه زمان‌های شروع و پایان استفاده می‌شوند.
   - کتابخانه defaultdict: یک نوع دیکشنری از کتابخانه collections که در صورت دسترسی به کلیدهای غیرموجود، به طور خودکار مقداری اولیه برای آن‌ها تولید می‌کند (در اینجا به لیست).
```python
import requests
from datetime import datetime, timedelta
from collections import defaultdict
```
2. تعریف تابع format_time:
- این تابع ورودی زمان utc_time را که به میلی‌ثانیه است، به زمان مناسب تبدیل می‌کند:
   - زمان ابتدا به ثانیه تبدیل می‌شود (با تقسیم بر 1000).
   - سپس با استفاده از datetime.utcfromtimestamp() به تاریخ و ساعت تبدیل می‌شود.
   - در نهایت، زمان به فرمت YYYY-MM-DD HH:MM:SS UTC تبدیل می‌شود.
```python
def format_time(utc_time):
    return datetime.utcfromtimestamp(utc_time / 1000).strftime('%Y-%m-%d %H:%M:%S UTC')
```
3. تعریف تابع fetch_earthquake_data:
   - زمان شروع و پایان: ابتدا زمان پایان به صورت زمان فعلی UTC (end_time) تعیین می‌شود، سپس زمان شروع (start_time) با استفاده از timedelta به مدت ۲۴ ساعت قبل از زمان فعلی تنظیم می‌شود.
   - ساخت URL: URL برای درخواست داده‌ها به API ساخته می‌شود که شامل پارامترهایی همچون فرمت geojson, زمان شروع و پایان، و حداقل شدت زلزله ۴ ریشتر است.
   - دریافت پاسخ: با استفاده از requests.get(url) داده‌ها از API دریافت شده و به فرمت JSON تبدیل می‌شوند.
   - بازگشت داده‌ها: داده‌ها به صورت ویژگی‌های زلزله‌ها (features) برگردانده می‌شوند.
```python
def fetch_earthquake_data():
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=1)
    url = (
        f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"
        f"&starttime={start_time.isoformat()}&endtime={end_time.isoformat()}"
        f"&minmagnitude=4"
    )
    response = requests.get(url)
    data = response.json()
    return data['features']
```
4. تعریف تابع display_earthquake_data:
   - دریافت داده‌ها: ابتدا داده‌های زلزله‌ها از تابع fetch_earthquake_data گرفته می‌شود.
   - ایجاد دیکشنری country_dict: این دیکشنری برای ذخیره اطلاعات زلزله‌ها به تفکیک کشورها و شهرها استفاده می‌شود.
  
```python
def display_earthquake_data():
    earthquake_data = fetch_earthquake_data()
    country_dict = defaultdict(list)
    
    for quake in earthquake_data:
        props = quake['properties']
        coords = quake['geometry']['coordinates']
        place = props['place']
        magnitude = props['mag']
        time = format_time(props['time'])
```
5. تقسیم‌بندی داده‌ها به کشورهای مختلف:
   - مکان (place) به قسمت‌های مختلف تقسیم می‌شود. اگر نام کشور و شهر با ویرگول جدا شده باشند، این اطلاعات استخراج شده و به دیکشنری country_dict افزوده می‌شود.
   - برای هر کشور، اطلاعاتی مانند نام شهر، مختصات جغرافیایی (طول و عرض جغرافیایی)، شدت زلزله، و زمان وقوع ذخیره می‌شود.
 ```python
        if ", " in place:
            city, country = place.split(", ")[-2:]
        else:
            city, country = place, "Unknown"
        
        country_dict[country].append({
            'city': city,
            'latitude': coords[1],
            'longitude': coords[0],
            'magnitude': magnitude,
            'time': time
        })
```
6. نمایش داده‌ها:
   - داده‌ها به ترتیب حروف الفبا بر اساس نام کشورها چاپ می‌شوند.
   - برای هر کشور، اطلاعات هر زلزله شامل نام شهر، مختصات جغرافیایی، شدت و زمان وقوع به صورت خوانا نمایش داده می‌شود.
   - در انتهای هر کشور، یک خط جداکننده برای خوانایی بیشتر چاپ می‌شود.
  
```python
    for country in sorted(country_dict.keys()):
        print(f"Country: {country}")
        for quake in country_dict[country]:
            print(f"  City: {quake['city']}")
            print(f"    Coordinates: ({quake['latitude']}, {quake['longitude']})")
            print(f"    Magnitude: {quake['magnitude']}")
            print(f"    Time: {quake['time']}")
        print("\n" + "-"*50 + "\n")
```
7. اجرای کد:
   - این خط کد تابع display_earthquake_data را اجرا می‌کند که در نهایت داده‌های مربوط به زلزله‌ها را نمایش می‌دهد.
```python
display_earthquake_data()
```

### نتیجه:
این کد اطلاعات زلزله‌های با شدت بالای ۴ ریشتر در ۲۴ ساعت گذشته را به تفکیک کشورها نمایش می‌دهد، شامل جزئیات مکان، شدت، زمان و مختصات جغرافیایی هر زلزله.

## کد پایتون:
```python
import requests
from datetime import datetime, timedelta
from collections import defaultdict

# تابعی برای فرمت کردن زمان
def format_time(utc_time):
    return datetime.utcfromtimestamp(utc_time / 1000).strftime('%Y-%m-%d %H:%M:%S UTC')

# درخواست داده‌های زلزله از API
def fetch_earthquake_data():
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=1)
    url = (
        f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"
        f"&starttime={start_time.isoformat()}&endtime={end_time.isoformat()}"
        f"&minmagnitude=4"
    )
    response = requests.get(url)
    data = response.json()
    return data['features']

# پردازش و نمایش اطلاعات
def display_earthquake_data():
    earthquake_data = fetch_earthquake_data()
    country_dict = defaultdict(list)
    
    for quake in earthquake_data:
        props = quake['properties']
        coords = quake['geometry']['coordinates']
        place = props['place']
        magnitude = props['mag']
        time = format_time(props['time'])

        # استخراج نام کشور و شهر از توضیحات مکانی
        if ", " in place:
            city, country = place.split(", ")[-2:]
        else:
            city, country = place, "Unknown"

        country_dict[country].append({
            'city': city,
            'latitude': coords[1],
            'longitude': coords[0],
            'magnitude': magnitude,
            'time': time
        })

    # نمایش اطلاعات به ترتیب حروف الفبا
    for country in sorted(country_dict.keys()):
        print(f"Country: {country}")
        for quake in country_dict[country]:
            print(f"  City: {quake['city']}")
            print(f"    Coordinates: ({quake['latitude']}, {quake['longitude']})")
            print(f"    Magnitude: {quake['magnitude']}")
            print(f"    Time: {quake['time']}")
        print("\n" + "-"*50 + "\n")

# اجرای کد
display_earthquake_data()
```


