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

برای مشاهده فایل <b>[English README.md](TremorTracker/EnglishTremorTracker.md)</b> و <b>[Persian README.md](TremorTracker/PersianTremorTracker.md)</b> و کد کامل <b>[Python Code](TremorTracker/TremorTracker.py)</b>.
<hr>

### 2. مانیتور زلزله:
این برنامه داده‌های زلزله‌های بالای ۴ ریشتر در ۲۴ ساعت گذشته را از سراسر دنیا با استفاده از API سازمان زمین‌شناسی آمریکا دریافت می‌کند. تابع fetch_earthquake_data() یک URL برای درخواست داده‌ها در قالب JSON می‌سازد که شامل فیلترهایی برای محدوده زمان و شدت زلزله است. تابع format_time() زمان زلزله را از فرمت UTC به یک تاریخ و زمان قابل خواندن تبدیل می‌کند. هر ورودی زلزله پردازش شده و اطلاعاتی مانند مکان، شهر، کشور، مختصات، شدت و زمان دقیق آن استخراج می‌شود. داده‌ها در یک دیکشنری ذخیره می‌شوند و زلزله‌ها براساس کشور و سپس شهر گروه‌بندی می‌شوند. تابع display_earthquake_data() کشورها را به ترتیب حروف الفبا مرتب کرده و اطلاعات هر کشور را به صورت خوانا چاپ می‌کند. برای هر کشور، شهرهای تحت تأثیر، مختصات جغرافیایی، شدت و زمان هر زلزله نمایش داده می‌شود. این برنامه به کاربران امکان می‌دهد فعالیت‌های لرزه‌ای اخیر را در سراسر دنیا مشاهده کنند، به صورت مرتب شده براساس کشور و شهر.

برای مشاهده فایل <b>[English README.md](QuakeMonitor/EnglishQuakeMonitor.md)</b> و <b>[Persian README.md](QuakeMonitor/PersianQuakeMonitor.md)</b> و کد کامل <b>[Python Code](QuakeMonitor/QuakeMonitorPersian.py)</b>.
<hr>

### 3. زمین لرزه های کشور ایران:
این کد با هدف استخراج و نمایش اطلاعات زلزله‌های یک ماه گذشته در ایران نوشته شده است و از API مرکز زمین‌شناسی ایالات متحده (USGS) برای دریافت داده‌ها استفاده می‌کند. ابتدا تاریخ امروز به همراه تاریخ ۳۰ روز قبل محاسبه می‌شود تا بازه زمانی یک ماه اخیر تنظیم گردد. سپس مختصات جغرافیایی ایران به‌عنوان محدوده جغرافیایی درخواست تنظیم شده و داده‌ها بر اساس این مختصات و بازه زمانی فیلتر می‌شوند.
کد با ارسال درخواست به API، اطلاعات زلزله‌ها را به‌صورت JSON دریافت می‌کند. اگر درخواست موفقیت‌آمیز باشد، برنامه وارد مرحله پردازش داده‌ها می‌شود. در این مرحله، برای هر زلزله ویژگی‌هایی شامل بزرگی زلزله، محل وقوع، زمان دقیق (تاریخ و ساعت) و مختصات جغرافیایی (عرض و طول) استخراج می‌گردد.
سپس برنامه با تجزیه مکان زلزله تلاش می‌کند تا نام استان یا شهری را که زلزله در آن رخ داده است استخراج کند. اگر مکان دارای نام دقیق شهر یا استان باشد، آن را به همراه اطلاعات کامل دیگری که جمع‌آوری شده در خروجی نمایش می‌دهد. اگر مکان دقیق مشخص نباشد، کد مکان کلی‌تر را نمایش می‌دهد. همچنین در صورت بروز خطا در هنگام دریافت داده‌ها، پیام خطا به کاربر نشان داده می‌شود تا از وضعیت ناموفق درخواست مطلع شود.

برای مشاهده فایل <b>[English README.md](IranSeismoFinder/EnglishIranSeismoFinder.md)</b> و <b>[Persian README.md](IranSeismoFinder/PersianIranSeismoFinder.md)</b> و کد کامل <b>[Python Code](IranSeismoFinder/IranSeismoFinderPersian.py)</b>.
<hr>





## مجوز


MIT

