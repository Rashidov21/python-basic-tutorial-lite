# bool,str,int,float,complex,list,tuple,range,dict,set,frozenset
# bool - True, False 

# str - 'text',"text","""text"""
# print("don't") 
# print("""don't "wory" """)
# num = "1"
# print(1 + num) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(num * 5) # 11111

# int , float, complex

# n = 3
# print(type(n)) # <class 'int'>
# n = 1.2
# print(type(n)) # <class 'float'>
# n = 2 + 2j
# print(n) # (2+2j)
# print(type(n)) # <class 'complex'>

# None - qiymat mavjud emas 

# count = None 

# Data type -> Primitiv . Referens 
# Primitiv - oddiy sodda malumot turlari 
# Referens - murakkab ma'lumot turlari 

# list - ro'yhatlar -> Array, massivlarni dinamik ko'rinishi 
# list - tartiblangan elementlar ketma-ketligi 

# l = [1,2,3]
# l = list("abc")
# print(l) # ['a', 'b', 'c']
# print(l[0])
# print(l[-1])
# Ketma-ketlik  > "abc" > [1,2,3] > (0,2,3) = ularga murojaat index (joylashuv) orqali boladi 
# To'plam > {'key':1}, set, frozenset

# tuple - kortej - o'zgarmas elementlar to'plami
# t = (1,2,3)
# print(t[2]) # 3

# dict - lug'at - elementlariga indeks orqali emas balki kalit o'rali murojaat qilinadigan to'plam
# d = {"key1":1,"key2":2}
# print(d) # {'key1': 1, 'key2': 2}
# d = dict(a=1,b=2)
# print(d) # {'a': 1, 'b': 2}

# range - diapazon - oraliq - sonlar oraligi, ketma-ketlik
# print(range(5)) # range(0, 5) > 0,1,2,3,4
# print(range(1,6)) # range(1, 6) > 1,2,3,4,5
# print(range(1,11,2)) # range(1, 11, 2) > [1, 3, 5, 7, 9 ]
# # print(list(range(1,11,2))) [1, 3, 5, 7, 9 ]
# print(sum(range(1,6))) # 15

# set - unikal elementlar to'plami
# s1 = set("abcc")
# print(s1)
# s2 = {'a','b','c','c'}
# print(s2)

# frozenset - o'zgarmas unikal elementlar to'plami
# fs1 = frozenset("abcc")
# print(fs1)