import calendar 
import datetime
import time 
# tilni o'zbekcha qilish 
import locale
locale.setlocale(locale.LC_ALL,"UZ_uz")

# cal = calendar.LocaleTextCalendar(0)
# print(cal.formatmonth(2025,6))

# html_cal = calendar.LocaleHTMLCalendar(0)
# print(html_cal.formatyear(2026))
# with open("calendar.html", "w+") as file:
#     file.write(html_cal.formatyear(2026))

# sana va vaqt bilan ishlash 
td = datetime.datetime.today()
print(td) # 2025-06-30 10:51:16.233444
print(td.year)
print(td.month)
print(td.day)
print(td.hour)
print(td.minute)
print(td.second)

my_birthday = datetime.date(1995,10,30)
today_date = datetime.date(2025,6,30)
time_dif = today_date - my_birthday
print(time_dif) # 10836 days, 0:00:00
print(time_dif.days ) # yillar bilan oylarni toping
print(time_dif.days // 30)
print((time_dif.days // 30) // 12)

print(datetime.datetime.now()) # 2025-06-30 11:19:07.971625

for i in range(5):
    print(i)
    time.sleep(1)

while True:
    _ = datetime.datetime.now()
    print(f"{_.hour}:{_.minute}:{_.second}")
    time.sleep(1)