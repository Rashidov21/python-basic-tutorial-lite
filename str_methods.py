# .upper() - Matndagi barcha harflarni katta harflarga o‘zgartiradi
# print("salom".upper())

# .lower() - Matndagi barcha harflarni kichkina harflarga o‘zgartiradi

# print('SALOM'.lower())

# .capitalize() - Matnning faqat birinchi harfini katta harfga o‘zgartiradi, qolganlarini kichik qiladi 
# print('salom'.capitalize())

# .title() - Matndagi har bir so‘zning birinchi harfini katta harfga o‘zgartiradi

# print('salom dunyo'.title())

# .strip() - Matn boshidagi va oxiridagi bo‘sh joylarni olib tashlaydi

# print('salom dunyo         '.strip())    

# .lstrip() - Matn boshidagi (chapdagi) bo‘sh joylarni olib tashlaydi

# print('salom dunyo         '.lstrip())

# .rstrip() - Matn oxiridagi (o‘ngdagi) bo‘sh joylarni olib tashlaydi

# print('salom dunyo         '.rstrip())

# .replace() - Matnda berilgan so‘z yoki belgilarni boshqa so‘z yoki belgilar bilan almashtiradi

# print("salom dunyo".replace("dunyo","python-basic"))

# .split() - Matnni berilgan ajratuvchi bo‘yicha bo‘laklarga ajratib, ro‘yxatga aylantiradi

# print("salom,dunyo,python,js,php,java pytho".split(","))

# .join() - Ro‘yxatdagi elementlarni birlashtirib, bitta matnga aylantiradi

# name =  ['hello', 'world', 'python']

# print(name)

# print(" ".join(name))

# print("".join(name))

# .find() - Matnda berilgan qatorning boshlanish indeksini topadi, topilmasa -1 qaytaradi

# print("salom dunyo".find("dunyo"))

# .count() - Matnda berilgan qator nechta marta uchrashini hisoblaydi

# fruits = ['banana', 'apple', 'banana', 'apple', 'kiwi'] 
# fruit_count = {}
# # print(fruits.count())
# for i in fruits:
#      if i in fruit_count:
#          fruit_count[i] += 1
#      else:
#          fruit_count[i] = 1
# print(fruit_count)
# print(len(fruits))

# .startswith() - Matn berilgan boshlang‘ich qator bilan boshlanishini tekshiradi


# .endswith() - Matn berilgan tugash qator bilan tugashini tekshiradi

# print('pythhon'.endswith('py')) # Boolean  False

# .index() - Matnda berilgan qatorning boshlanish indeksini topadi, topilmasa xato beradi
# print("salom dunyo".index("dunyo"))

# .rindex() - Matnda berilgan qator oxirgi marta qayerda boshlanishini topadi, topilmasa xato beradi

# print("salom dunyo".rindex("dunyo"))

# .format() - Matn ichida joy ajratib, unga qiymatlar joylashtiradi

# print('{0} Husanboy {1} {2}'.format('salom', 'dunyo', 'python'))
# print('{0} Husanboy {2} {1}'.format('salom', 'dunyo', 'python'))

# .center() - Matnni berilgan uzunlikda markazlashtiradi va bo‘sh joylar bilan to‘ldiradi

# print("Salom MuhammadYusuf aka".center(40,'@')) # 40 ta belgi bo‘yicha matnni markazlashtirish

# .isalpha() - Matn faqat harflardan iborat bo‘lsa True, aks holda False qaytaradi
# print('salom'.isalpha()) # True

# .isdigit() - Matn faqat raqamlardan iborat bo‘lsa True, aks holda False qaytaradi

# print('hello123'.isdigit()) # False
# print('12.3'.isdigit()) # False

# .isalnum() - Matn faqat harflar va raqamlardan iborat bo‘lsa True, aks holda False qaytaradi
# print('salom123'.isalnum())

# .isnumeric() - Matn faqat raqam belgilaridan iborat bo‘lsa True, aks holda False qaytaradi

# print('123'.isnumeric()) # True

# .isdecimal() - Matn faqat o‘nlik raqamlardan iborat bo‘lsa True, aks holda False qaytaradi

# print('12.3'.isdecimal()) # True

# .islower() - Matn faqat kichik harflardan iborat bo‘lsa True, aks holda False qaytaradi
# print('salom'.islower())
# print('Salom'.islower())

# .isupper() - Matn faqat katta harflardan iborat bo‘lsa True, aks holda False qaytaradi


# .isspace() - Matn faqat bo‘sh joylardan iborat bo‘lsa True, aks holda False qaytaradi

# print(' '.isspace()) # True

# .istitle() - Matn har bir so‘zining birinchi harfi katta, qolganlari kichik bo‘lsa True qaytaradi

# print('Salom Muhammadyusuf Aka'.istitle())

# .swapcase() - Matndagi katta harflarni kichik, kichik harflarni katta harflarga o‘zgartiradi

# print('salom muhammadyusuf aka'.swapcase())