<div align="center">

## TremorTracker

<img alt="Gif" src="https://acropolis-wp-content-uploads.s3.us-west-1.amazonaws.com/2019/02/Hero-Earthquake-Proof-Buildings.gif" height="250px" width="600px">
</div>
<hr>

[Click to see the descriptions in Persian language](EnglishTremorTracker.md)
<hr>



## مروری بر کد:
این اسکریپت برای واکشی داده‌های زلزله از USGS (سازمان زمین‌شناسی ایالات متحده) با استفاده از فید GeoJSON، تجزیه پاسخ JSON و چاپ اطلاعات مرتبط مانند تعداد رویدادها و مکان‌هایی که زمین‌لرزه‌ها در آن‌ها احساس شده‌اند، طراحی شده است.

[دیدن کد پایتون](TremorTracker.py)

## یافتن اطلاعات:
این کد اطلاعات را از وب سایت سازمان زمین شناسی ایالات متحده (USGS) به طور خاص از آدرس اینترنتی زیر بازیابی می کند:

 برای دیدن سایت مرجع کلک کنید <a href="http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson" target="_blank">View Earthquake Data</a>

این URL یک فید GeoJSON ارائه می دهد که حاوی داده های مربوط به زلزله های اخیر است. اطلاعات خاص ارسال شده به کد شامل:
1. فراداده: این شامل عنوان مجموعه داده و تعداد رویدادهای زلزله ثبت شده است.
2. ویژگی ها: این بخش جزئیات مربوط به هر زمین لرزه از جمله:
   مکان: موقعیت جغرافیایی زلزله.<br>
  بزرگی: قدرت زمین لرزه که برای فیلتر کردن رویدادهای مهم استفاده می شود (قدرت ≥ 4.0).<br>
  گزارش‌های احساسی: تعداد گزارش‌های افرادی که زلزله را احساس کرده‌اند، در صورت وجود.

کد این داده‌ها را پردازش می‌کند تا عنوان، تعداد کل رویدادهای ثبت‌شده، مکان همه زمین‌لرزه‌ها، مکان‌های زمین‌لرزه‌های مهم (قدرت ≥ 4.0)، و جزئیات زمین‌لرزه‌هایی که توسط مردم احساس شده‌اند، همراه با شمارش چنین گزارش‌هایی را نمایش دهد.


## کتابخانه ها:
کد از کتابخانه های زیر استفاده می کند:
1. کتابخانه json :
  این کتابخانه بخشی از کتابخانه استاندارد پایتون است و برای تجزیه و تحلیل داده های JSON (جاوا اسکریپت Object Notation) استفاده می شود. نیازی به نصب این کتابخانه نیست، زیرا با پایتون از قبل نصب شده است.
2. کتابخانه urllib.request:
  این ماژول کتابخانه استاندارد دیگری است که برای مدیریت باز کردن و واکشی URL ها استفاده می شود. این کتابخانه نیز به صورت پیش فرض در پایتون گنجانده شده است، بنابراین نیازی به نصب نیست.

## چیست و چگونه کار می کند(json)؟
جیسون یک فرمت تبادل داده سبک وزن است که خواندن و نوشتن آن برای انسان آسان است و تجزیه و تولید آن برای ماشین ها آسان است. معمولاً برای انتقال داده ها در برنامه های وب بین سرور و مشتری استفاده می شود.
در پایتون، از کتابخانه json برای رمزگشایی داده‌های JSON در فرهنگ لغت پایتون استفاده می‌شود و به برنامه اجازه می‌دهد به راحتی به داده‌ها دسترسی پیدا کند و آن‌ها را دستکاری کند.
<hr>

## چگونه کد کار می کند (تجزیه گام به گام):
1. واردات کتابخانه ها:
```python
import json
import urllib.request
```
کتابخانه json برای کار با داده های JSON استفاده می شود.
کتابخانه urllib.request برای ایجاد درخواست های HTTP برای واکشی داده ها از یک URL خاص استفاده می شود.


2. تعریف تابع printResults:
```python
def printResults(data):
```
این تابع داده های JSON دریافتی از سرور USGS را پردازش کرده و اطلاعات مورد نظر را چاپ می کند.

3. Parse the JSON Data:
```python
theJSON = json.loads(data)
```
داده های JSON (در قالب رشته) با استفاده از json.loads() در فرهنگ لغت پایتون بارگذاری می شود. این امکان دسترسی آسان به داده ها را فراهم می کند.


4. استخراج عنوان از متادیتا:
```python
if 'title' in theJSON['metadata']:
    print(theJSON['metadata']['title'])
```
با این کار بررسی می‌شود که «عنوان» در فراداده وجود داشته باشد و آن را چاپ می‌کند. عنوان معمولاً اطلاعاتی در مورد منبع داده می دهد.


5. شمارش و چاپ کل رویدادها:
```python
count = theJSON['metadata']['count']
print(count, 'events recorded')
```
فیلمنامه تعداد کل رویدادهای زلزله ثبت شده را واکشی می کند و آن را چاپ می کند.


6. چاپ همه مکان های رویداد:
```python
for i in theJSON['features']:
    print(i['properties']['place'])
```
این حلقه روی تمام رویدادهای زلزله (ویژگی ها) تکرار می شود و مکان (مکان) جایی که هر زلزله رخ داده است را چاپ می کند.


7. فیلتر کردن و چاپ رویدادهای مهم (مقدار >= 4.0):
```python
for i in theJSON['features']:
    if i['properties']['mag'] >= 4.0:
        print(i['properties']['place'])
```
این حلقه مکان های زلزله هایی با بزرگی بیشتر یا مساوی 4.0 را چاپ می کند. این وقایع به دلیل بزرگی بالاتر از اهمیت بیشتری برخوردار هستند.


8. چاپ زمین لرزه هایی که توسط مردم احساس شد:
```python
print('\n Events that were felt:')
for i in theJSON['features']:
    feltReports = i['properties']['felt']
    if feltReports is not None:
        if feltReports > 0:
            print(i['properties']['place'], feltReports, 'times')
```
این کد رویدادهایی را که مردم گزارش کرده اند زلزله را احساس کرده اند فیلتر می کند. اگر رویدادی احساس شد، مکان و تعداد دفعات گزارش آن را چاپ می‌کند.


9. عملکرد اصلی:
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
تابع main() یک درخواست HTTP به USGS API برای بازیابی آخرین داده های زلزله (خلاصه رویدادها با بزرگی 2.5+ برای روز گذشته) می دهد.
اگر درخواست موفقیت آمیز باشد (200 کد وضعیت)، داده های پاسخ برای پردازش به تابع printResults() ارسال می شود. اگر نه، پیغام خطا چاپ می کند.


10. اجرای اسکریپ:
```python
if __name__ == "__main__":
    main()
```
این بلوک تضمین می کند که تابع main() هنگام اجرای اسکریپت فراخوانی می شود.

## کد پایتون
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

## نتیجه گیری:
این اسکریپت داده‌های زلزله در زمان واقعی را از USGS بازیابی می‌کند و آن‌ها را برای نمایش اطلاعات کلیدی درباره زلزله‌های اخیر پردازش می‌کند، مانند:
- عنوان مجموعه داده
- تعداد کل رویدادها
- مکان تمام رویدادهای ثبت شده
- مکان رویدادهایی با قدر 4.0 یا بیشتر
- مکان ها و تعداد رویدادهایی که توسط مردم احساس می شد.

<hr>
