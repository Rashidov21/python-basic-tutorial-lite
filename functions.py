# function - nom berilgan bu kod bo'lagi uni dasturni istalgan joyida (o'zi elon qilingan qatordan so'ng) istalgan marta chaqirish mumkin

# def - funktsiyalar elon qilinadi 
# function - harakat  


# print() - bu funktsiya , u oziga berilgan narsalarni ekranga chiqaradi 
# def main():
#     pass 

# print(main) # <function main at 0x000002326EF4A340>
# print(main()) # None

# main - bu funksiyani nomi va shu nom ostida RAM da uni kodlari saqlanadi
# () - bu funksiyani ishga tushirish


# def plus(x,y):
#     return x + y 

# print(plus("lap","top")) # laptop
# print(plus(2,2)) # 4
# print(plus(True,False)) # 1
# print(plus([1,2],[4,5])) # [1, 2, 4, 5]
# print(plus({"a":2},{"b":3})) # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# def plus(x,y):
#     if type(x) == int or type(x) == float and type(y) == int or type(y) == float:
#         return x + y 
#     else:
#         return "Plus function work with only numbers..."
    

# print(plus("lap","top"))
# print(plus(2,2)) # 4
# print(plus(2,2.5)) # 4.5

# def test(a,b,c,d):
#     return [a,b,c,d]

# result = test(1,2,3,4)
# print(result) # [1, 2, 3, 4]

# print(test(1,2,3)) # TypeError: test() missing 1 required positional argument: 'd'

# positional arguments and not positiniol arguments 
# positional arguments
# def test(a,b,c,d):
#     return [a,b,c,d]

# #  not positiniol arguments 
# def test(a=None,b=None,c=None,d=None):
#     return [a,b,c,d]
# print(test()) # [None, None, None, None]

# def test(a=0,b=0,c=0,d=0):
#     return [a,b,c,d]
# print(test()) # [0, 0, 0, 0]

# def test(a=0,b=0,c=0,d=0):
#     return [a,b,c,d]
# print(test(5,6)) # [5, 6, 0, 0]

# task 1 
# user 2 ta son kiritadi va "+-*/" belgilarigan bittasini ham kiritadi siz funktsiya orqal 
# kiritilgan 2 son ustida kiritilgan amalni bajarib natijani qaytarishingiz kerak

# input 
# num1 = input("N1")
# num2 = input("N2")
# operator = input("+-*/ ?")

# a,b,*c = 1,2,3,4,5

# print(a,b,c) # 1 2 [3, 4, 5]

# *args - list arguments 
# **kwarg - dict - keyword arguments

# def create_new_person_data(full_name,age,gender,height,weight...):
#     return {"fname":full_name,"age":age,"gender":gender,....}

# def create_new_person_data(*args):
#     print(type(args)) # <class 'tuple'>
#     print(args) # ('John Doe', 23, 'male', 1.86, 75)
#     for a in args:
#         print(a)

# create_new_person_data("John Doe",23,"male",1.86,75)


# def create_new_person_data(*args,**kwargs):
#     print(type(args)) # <class 'tuple'>
#     print(args) # ('salom', 'qale')

#     print(type(kwargs)) # <class 'dict'>
#     print(kwargs) # {'a': 1, 'b': 2}

# create_new_person_data("salom","qale",a=1,b=2)



# lambda - anonim function 

# l = lambda a: a**2

# print(l(2)) #4
# print(l(10)) # 100

# print(lambda x,y:x+y) # <function <lambda> at 0x0000021EBF24D1C0>
# plus = lambda x,y:x+y
# print(plus(2,2)) # 4

# task : arr ichidagi 5 dan katta qiymatlarni alohida massivga yozing

# arr = [1,2,4,5,9,7,8,6,3,1,2,5,4]
# result = []
# for i in arr:
#     if i > 5:
#         result.append(i)
# print(result) # [9, 7, 8, 6]

# print([i for i in arr if i > 5]) # [9, 7, 8, 6]

# filter() - berilgan ketma-ketlikdan berilgan shart (function) boyicha elementlarni filterlaydi

# print(filter(lambda i: i>5,arr)) # <filter object at 0x0000024971EA5F00>
# print(list(filter(lambda i: i>5,arr))) # [9, 7, 8, 6]

# map - berilgan ketma-ketlikdagi har bir element uchun berilgan functionni qo'llaydi
# print(list(map(lambda i:i**2,[1,2,3]))) # [1, 4, 9]

# zip - berilgan ketma-ketliklardan har biridan teng miqdorda element olib yangi ketma-ketlik tuple qaytaradi 

# print(list(zip("abc",[1,2,3,4,5]))) # [('a', 1), ('b', 2), ('c', 3)]
# print(list(zip("abc",[1],(-1,-2,-3)))) # [('a', 1, -1), ('b', 2, -2), ('c', 3, -3)]

# arr = [1,2,4,5,9,7,8,6,3,1,2,5,4]
# arr.sort()
# print(arr) # [1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9]
# arr = [1,2,4,5,9,7,8,6,3,1,2,5,4]
# arr.sort(reverse=True)
# print(arr) # [9, 8, 7, 6, 5, 5, 4, 4, 3, 2, 2, 1, 1]

# arr.sort(key= lambda x: x > 5)
# print(arr) # [5, 5, 4, 4, 3, 2, 2, 1, 1, 9, 8, 7, 6]
# arr.sort(key= lambda x: x < 5)
# print(arr) # [5, 5, 9, 8, 7, 6, 4, 4, 3, 2, 2, 1, 1]

data = list(zip("ecbd",[2,1,3,4,]))
print(data) # [('e', 2), ('c', 1), ('b', 3), ('d', 4)]

data.sort(key=lambda i:i[1])
print(data) # [('c', 1), ('e', 2), ('b', 3), ('d', 4)]
data.sort(key=lambda i:i[0])
print(data) # [('b', 3), ('c', 1), ('d', 4), ('e', 2)]

arr = [
    {"age":23,"weight":58},
    {"age":18,"weight":68},
    {"age":14,"weight":75},
    {"age":19,"weight":98},
    {"age":29,"weight":82},
]
arr.sort(key=lambda item: item["age"]) # age boyicha saralash
print(arr)
arr.sort(key=lambda item: item["weight"]) # weight boyicha saralash
print(arr)