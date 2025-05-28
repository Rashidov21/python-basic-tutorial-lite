"""Bu bizni Pythondagi birinchi kodimiz"""
# Interpretator - kodni tog'ri yozilganiga tekshiruvchi dastur
# Kompilyator - kodni mashina kodiga tarjima qiladi

# print("hello world")

# Komentlar - qisqa , lo'nda, mantiqan to'gri va ingliz tilida bo'lishi kerak

# Dastur
# 1. Ma'lumot qabul qilish 
# 2.Uni qayta ishlash
# 3.Saqlash 
# 4.Natijani qaytarish 

# O'zgaruvchi 
# Malumot turlari 

# O'zgaruvchi - kompyuter xotirasidagi RAM ma'lum bir katakchaga olib boruvchi manzil 
# def main():
#     pass 

# print(main)  # <function main at 0x0000025194F704A0>
# main  = 0x0000025194F704A0

# x = 10

# print(x)

# z = 3

# print(10+10)

# O'zgaruvchini nomlashda :
# 1.ingliz tilida 
# 2.mantiqan to'gri nom
# 3.birinchi belgisi raqam yoki belgilar bolishi mumkin emas faqat _ mumkin

# Mumkin:
#     name 
#     NAME 
#     n1
#     _name 
    
# Mumkin emas:
#     1name
#     %name
#     n 

# Case'lar - register
# Camel case > userAge , userProfilePictureUrl 
# Snake case > user_age,user_profile_picture_url

# cd documents 
# cd Documents
# NAME = "john"
# name = "david"
# print(NAME,name)


# PI = 3.14
# PI = 3.50
# print(PI) 

# x = 10
# x = 15
# print(x)

# import keyword
# print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# if , elif , else

# if - agar 
# elif - aks holda yoki  
# else - aks holda

# name = input("Ismingizni kiriting: ")
# if name:
#     print(f"Xush kelibsiz {name}")
#     # f - string format "" {o'zgaruvchi}
# else:
#     print("Iltimos ismingizni kiriting")



# and - va 
# if age and age > 18:
#     print("Xush kelibsiz")
    
# or - yoki

# if age or age > 18:
#     print("Xush kelibsiz")
    
# elif age == 18:
#     print("Xush kelibsiz")
    
# else:
#     print("Sizning yoshingiz 18 dan kichik")

# match case - 
# age = int(input())

# match age: # ozgaruvchi 
#     case 18:
#         print("Xush kelibsiz")
#     case _ if age > 18:
#         print(f"Xush kelibsiz sizning yoshingiz 18 dan katta")
#     case _ if age == 18:
#         print("Xush kelibsiz sizning yoshingiz 18")
#     case _:
#         print("Sizning yoshingiz 18 dan kichik")

# 🧩 3-mashq: Oy nomiga qarab faslni aniqlash

# 🔹 Foydalanuvchi oy nomini kiritadi (mart, dekabr, avgust va h.k.). Siz faslni aniqlang: bahor, yoz, kuz, yoki qish.

# input: oy nomi
# output: fasl nomi

# 2. Foydalanovchini parolini uzunligini tekshiring agar 6 bekgidan dan katta bolsa "Parol muvaffaqiyatli saqlandi" aks holda "Iltimos parol 6 dan katta bolishi shart" xabar chiqsin

# input: parol
# output: "Parol muvaffaqiyatli saqlandi" aks holda "Iltimos parol 6 dan katta bolishi shart"

# len() - uzunligini aniqlash
# in - mavjudligini tekshiradi 
# not in - mavjud emasligini tekshiradi

# Uyga vazifa 

# Telefon raqamini tekshiring (90,91)
# agar 93 50 94 operator - bolsa Ucel 
# 77 lik 88 Uzmobile  
# 91 90 Beeline  

