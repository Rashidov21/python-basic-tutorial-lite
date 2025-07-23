
# OOP – bu dasturlash uslubi. Unda ma'lumotlar va funksiyalar bir joyda, ya'ni ob'ektlarda saqlanadi.

# Bu uslubda biz haqiqiy hayotdagi narsalarni (mashina, odam, hayvon) dasturda model qilishimiz mumkin.
# Class yaratamiz
# class Student:
#     def __init__(self, name, age):
#         self.name = name        # bu attribute
#         self.age = age      # bu ham attribute

#     def say_hi(self):      # bu method
#         print(f"Salom, mening ismim {self.name}, yoshim {self.age} da.")

# Object yaratamiz
# student_1 = Student("Ali", 20)
# student_2 = Student("Vali", 21)
# student_3 = Student("G'ani", 16)

# # Method chaqiramiz
# student_1.say_hi()
# student_2.say_hi()
# student_3.say_hi()

# class Calculator:
#     def __init__(self,number1,number2,action):
#         self.number1 = number1
#         self.number2 = number2
#         self.action = action
    
#     def plus(self):
#         return self.number1 + self.number2
    
#     def check(self):
#         if self.action == "+":
#             print(self.plus())

# calc = Calculator(2,2,"+")
# calc.check() # 4

# # Meros olish 
# class Animal:
#     def __init__(self,name):
#         self.name = name 

# class Dog(Animal):
    
#     def says(self):
#         print(f"{self.name} wow wow !")
        
# class Cat(Animal):
    
#     def says(self):
#         print(f"{self.name} meow meow !")
# dog = Dog("Rex")
# cat = Cat("Matroskin")
# dog.says() # Rex wow wow !
# cat.says() # Matroskin meow meow !

# Meros olishni ishlatib 
# Person > Teacher
# Man,Woman > Boy 


class BankAccount:
    def __init__(self, balance,test):
        self.__balance = balance  # private attribute
        self.test = test

    def view_balance(self):
        return self.__balance

    def get_cash(self, summa):
        if summa <= self.__balance:
            self.__balance -= summa
            print(f"{summa} so'm yechildi. Qolgan balans: {self.__balance}")
        else:
            print("Xatolik: Mablag' yetarli emas.")
    
    @staticmethod 
    def plus(x,y):
        print(x+y)

account = BankAccount(1000,True)
print(account.plus(2,5))
# account = BankAccount(1000,"None")
# # Bu xatolik: tashqaridan to'g'ridan-to'g'ri kira olmaymiz
# # print(account.__balance) # AttributeError

# print(account.view_balance())   # 1000
# account.get_cash(300)           # 300 so'm yechildi...
# print(account.view_balance())   # 700

# print(account.test)
# account.test = "Hello world"
# print(account.test)

class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    @classmethod
    def tugilgan_yili_boyicha(cls, ism, yil):
        from datetime import date
        hozirgi_yil = date.today().year
        yosh = hozirgi_yil - yil
        return cls(ism, yosh)  # yangi Talaba obyektini yaratadi

    def info(self):
        print(f"{self.ism}, {self.yosh} yoshda")

# Obyektni boshqa usul bilan yaratish
talaba1 = Talaba.tugilgan_yili_boyicha("Ali", 2005)
talaba1.info()