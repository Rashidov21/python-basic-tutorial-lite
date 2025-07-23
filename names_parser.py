
# import requests
# from bs4 import BeautifulSoup

# url = "https://ismlar.com/uz/category/Arabcha,%20o%E2%80%98zbekcha"
# # ?page=2

# for i in range(1,94):
#     page = requests.get(url+f"?page={i}")
#     soup = BeautifulSoup(page.text, "html.parser")
#     names = soup.find_all("li", class_="p-4 rounded-2xl space-y-4 bg-cyan-100")
#     data = []
#     for name_block in names:
#         name = name_block.find("a").text.strip()
#         desc  = name_block.find("p").text.strip()
#         data.append(name)
#         data.append(desc)
#     with open("names.txt", "a+", encoding="utf-8") as file:
#         file.write(f"id={i}, name={data[0]}, description={data[1]} \n")



# open() fayllarni ochish 
# f = open("test.txt","r")
# print(f) # FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

# f = open("test.txt", "+w")
# # print(dir(f))
# # 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines'
# f.write("Hello world")
# f.close()
# rf = open("test.txt", "r")
# print(rf.read()) # Hello world
# rf.close() 

# with open("example.txt", "w", encoding="utf-8") as file:
#     file.write("Salom, dunyo!")

# with open("example.txt", "a", encoding="utf-8") as file:
#     file.write("\nYana bir qatordan matn.")

# with open("example.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)
# line_lenght = []
# with open("test.txt", "r", encoding="utf-8") as file:
#     for index,line in enumerate(file.readlines()):
#         line_lenght.append((index,len(line),line))
#     line_lenght.sort(key=lambda x:x[1])
#     print(line_lenght[-1][2])


# with open("test.txt", "r") as file:
#     f = file.readlines()
#     f.sort(key=lambda x:len(x),reverse=True)
#     print(f[0])

# with open("nums.txt","w+") as file:
#     for i in range(15):
#         file.write(f"{i}\n")
# summa = []
# with open("nums.txt", "r") as file:
#     for line in file.readlines():
#         summa.append(int(line))
# print(sum(summa)) #105