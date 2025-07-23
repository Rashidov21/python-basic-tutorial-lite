import tkinter
import requests
from bs4 import BeautifulSoup
root = tkinter.Tk()
root.title("Currency app")
root.geometry("350x250")

url = "https://nbu.uz/jismoniy-shaxslar-valyutalar-kursi"
try:
    page =  requests.get(url)
except Exception as e:
    print("No connection !")
parser = BeautifulSoup(page.text,"html.parser")
currencies = parser.find_all("div", class_="currency_03_currency-item")
# nomi = currencies[0].find("div", class_="currency_03_currency-item-curerncies-wrapper")
# print(parser.find_all("div", class_="currency_03_currency-item-curerncies")[5])

data = []
for cur in currencies[:3]:
    currency = cur.find("div", class_="currency_03_currency-item-curerncies")
    buy_sale = cur.find_all("div", class_="currency_03_currency-item-price")
    lbl_currency = tkinter.Label(text=currency.text,font=("Arial",16))
    lbl_buysale = tkinter.Label(text=f"Sotib olish = {buy_sale[0].text}\nSotish = {buy_sale[1].text}",font=("Arial",12))
    lbl_currency.pack()
    lbl_buysale.pack()
root.mainloop()