import requests
from datetime import datetime, timedelta

def get_iran_earthquakes():
    # آدرس API مربوط به زلزله‌ها
    url = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
    
    # محاسبه تاریخ پایان (امروز) و تاریخ شروع (یک ماه قبل)
    end_date = datetime.utcnow()  # تاریخ امروز به‌صورت UTC
    start_date = end_date - timedelta(days=30)  # تاریخ 30 روز قبل
    
    # تنظیم پارامترهای درخواست به API
    params = {
        'format': 'geojson',
        'starttime': start_date.strftime('%Y-%m-%d'),  # تاریخ شروع (30 روز قبل)
        'endtime': end_date.strftime('%Y-%m-%d'),      # تاریخ پایان (امروز)
        'minlatitude': 24.396308,     # حداقل عرض جغرافیایی برای ایران
        'maxlatitude': 39.148174,     # حداکثر عرض جغرافیایی برای ایران
        'minlongitude': 44.396216,    # حداقل طول جغرافیایی برای ایران
        'maxlongitude': 63.246158     # حداکثر طول جغرافیایی برای ایران
    }
    
    # ارسال درخواست به API
    response = requests.get(url, params=params)
    
    # بررسی موفقیت درخواست
    if response.status_code == 200:
        # استخراج داده‌ها به‌صورت JSON
        data = response.json()
        earthquakes = data['features']
        
        # پردازش هر زلزله در لیست زلزله‌ها
        for quake in earthquakes:
            magnitude = quake['properties']['mag']  # بزرگی زلزله
            location = quake['properties']['place']  # مکان زلزله
            # تبدیل زمان وقوع زلزله از میلی‌ثانیه به فرمت خوانا
            quake_time = datetime.utcfromtimestamp(quake['properties']['time'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
            # دریافت مختصات جغرافیایی (طول و عرض)
            coordinates = quake['geometry']['coordinates']
            longitude = coordinates[0]  # طول جغرافیایی
            latitude = coordinates[1]   # عرض جغرافیایی
            
            # تلاش برای استخراج نام استان یا شهر از رشته مکان
            if 'Iran' in location:
                # منطق ساده برای استخراج شهر/استان
                parts = location.split(',')
                if len(parts) > 1:
                    city_province = parts[-2].strip()  # گرفتن قسمت قبل از "Iran"
                    print(f'بزرگی: {magnitude}, مکان: {city_province}, مکان کامل: {location}, تاریخ: {quake_time}, عرض جغرافیایی: {latitude}, طول جغرافیایی: {longitude}')
                else:
                    print(f'بزرگی: {magnitude}, مکان: {location}, تاریخ: {quake_time}, عرض جغرافیایی: {latitude}, طول جغرافیایی: {longitude}')
    else:
        print('خطا در دریافت داده‌ها')

# فراخوانی تابع
get_iran_earthquakes()
