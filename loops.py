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

count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue # keyingi siklga o'tish
    if count == 7:
        break # siklni to'xtatish
    print(count)
