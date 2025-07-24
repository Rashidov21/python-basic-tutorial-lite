import time
# Exception - xatoliklar uchun ota obyekt

# print(1 / 0) # ZeroDivisionError: division by zero

# n = 10
# try:
#     res = n / 0  # This will raise a ZeroDivisionError  
# except ZeroDivisionError:
#     print("Can't be divided by zero!")
# print(2*2)
# print(2*10)

# x = 2
# try:
#     # xatolik bolishi mumkin bolgan kod 
#     x / 1
# except:
#     # xatolik bolsa ishlashi kerak bolgan kod 
#     print("Xatolik bor - ", x)
# else:
#     # xatolik bolmasa ishlaydigan kod 
#     print("Xatolik yoq  - ", x)
# finally:
#     # xatolik bolsa bolmasa ishlaydigan kod 
#     print("xatolikga tekshirildi")

# with open("data.json", "r") as file:
#     print(file.read()) # FileNotFoundError
# try:    
#     with open("data.json", "r") as file:
#         print(file.read())
# except FileNotFoundError as err:
#     print("Fayl topilmadi uni hosil qilaman!")
#     print(err)
#     time.sleep(2)
#     with open("data.json", "w+") as file:
#         print("Fayl hosil qilingi!")

# import requests

# try:
#     page = requests.get("https://pyblog.uz")
#     print(page.status_code)
# except Exception as er:
#     time.sleep(5)
#     page = requests.get("https://pyblog.uz")
#     print(page.status_code)