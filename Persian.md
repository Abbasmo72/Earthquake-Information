<div align="center">

## اطلاعات زلزله

<img alt="Gif" src="https://acropolis-wp-content-uploads.s3.us-west-1.amazonaws.com/2019/02/Hero-Earthquake-Proof-Buildings.gif" height="250px" width="600px">
</div>
<hr>

[Click to see the descriptions in English language](README.md)

نکته :<b>هر بخش دارای یک فایل README به زبان انگلیسی و فارسی در فایل مربوطه می باشد. با کلیک بر روی پیوندهای هر بخش، می توانید اطلاعات عمیق بیشتری در مورد کد و عملکرد آن کسب کنید.<b/>
<hr>

### 1. ردیاب زلزله:
این کد پایتون به منظور دریافت و نمایش اطلاعات زلزله‌های اخیر از API مرکز زمین‌شناسی ایالات متحده (USGS) طراحی شده است. با استفاده از کتابخانه urllib.request، داده‌های زلزله به فرمت JSON از URL مشخص شده دریافت می‌شود. تابع printResults برای پردازش این داده‌ها نوشته شده و ابتدا عنوان و تعداد رویدادهای زلزله را چاپ می‌کند. سپس، مکان تمام زلزله‌ها را لیست می‌کند و مکان‌هایی که زلزله‌های با شدت ۴ یا بیشتر ثبت شده‌اند را جداگانه نمایش می‌دهد. در انتها، تعداد دفعاتی که زلزله‌ها در هر منطقه حس شده‌اند را بررسی و چاپ می‌کند. در تابع main، پس از برقراری اتصال به URL، در صورت موفقیت‌آمیز بودن درخواست، داده‌ها به تابع printResults ارسال می‌شوند تا پردازش شوند. اگر در دریافت داده‌ها خطایی رخ دهد، یک پیام خطا به کاربر نمایش داده می‌شود.
برای مشاهده فایل <b>[English README.md](TremorTracker/EnglishTremorTracker.md)</b> و <b>[Persian README.md](TremorTracker/PersianTremorTracker.md)</b> در مورد کد کامل بازی <b>[Python Code](TremorTracker/TremorTracker.py)</b>.
<hr>



## مجوز


MIT

