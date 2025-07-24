import requests
import time
from bs4 import BeautifulSoup
from db import write_to_db


url = "https://asaxiy.uz/product/knigi/page="
HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
for i in range(1,400):
    page = requests.get(url=url+str(i), headers=HEADERS)
    soup = BeautifulSoup(page.text, "html.parser")
    product_cards = soup.find_all("div",class_="product__item d-flex flex-column justify-content-between product-installment-item")

    for card in product_cards:
        title = card.find("p",class_="title__link").text.strip()
        price = card.find("span", class_="product__item-price").text.strip()
        link = "https://asaxiy.uz" + card.find_all("a")[1]["href"]
        write_to_db(title,price,url)
        print("page = ", i)
    time.sleep(1)