# for , while 
# for - sanoqli takrorlanish 
# while - cheksiz takrorlanish 

# for index,elem in enumerate("salom"):
#     print(f"{elem} in index = {index}")
    
# for i in range(3):
#     x = int(input("X = "))
#     print(x**2)

# for i in range(5):print(i)

# for i in range(10):
#     if i % 2 == 0:
#         print("Juft")
#     else:
#         print("Toq")
# else:
#     print("sikl tugadi")

# continue, break

# count = 0
# while count < 10:
#     count += 1
#     if count % 2 == 0:
#         continue # keyingi siklga o'tish
#     if count == 7:
#         break # siklni to'xtatish
#     print(count)

# task 3 
# n soni berilgan (30 > n > 0) 0 dan n gacha bo'lgan sonlarni orasida probellar bilan chiqaring agar son toq bo'lsa bitta probel bilan uni keyingi son orasini belgilaysiz agar juft bo'lsa 2 ta probel bilan. misol : 0  1 2  3 4  5

# task 4 
# 1 dan  500 gacha sanab barcha 7 sonlarini alohida massivga yozing;
# Masalan nums = [7,17,27……]

# task 8 
# 9 qavatli uyda 3-ta podyezd bor har bir qavatda 6 tadan kvartira bor. Foydalanuvchi kvartira raqamini kiritsa siz topishingiz kerak;
# (kvartiralar raqamlari 1-chi qavatdan 1-podyezdan boshlanadi : 1-kv , 1-podyezd 1-etaj)
# Kvartira qaysi qavatda ekanini
# Kvartira qaysi podyezdda ekanini
# etaj = 9
# podyezd = 3
# kvartiralar = (9 * 6) * 3 # 162
# print(range(1,163,kvartiralar // podyezd))
# print(list(range(1,163,kvartiralar // podyezd)))

# user = 23
# if user > 1 and user <= 54:
#     print("birinchi podyezd")
#     print("etaj = ", (user // 6) + 1)
# if user > 54 and user <= 108:
#     print("ikkinchi podyezd")
# if user > 109 and user <= 162:
#     print("uchinchi podyezd")
    
def main(x,y):
    