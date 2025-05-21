# pip install requests 
# pip install beautifulsoup4
# pip install wget
import requests
import wget
from bs4 import BeautifulSoup

url = "https://qalampir.uz/"
HEADERS  = {
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
}
page = requests.get(url, headers=HEADERS)
print(page.status_code) # agar 200 bolsa demak sahifa yuklanyapti
# print(page.text) 
soup = BeautifulSoup(page.text, "html.parser")
all_images = soup.find_all("img")

count = 0
for img in all_images:
    src = img.get("src")  
    if src and src.startswith("http"):
        file_path = f"img_{count}.png"
        try:
            wget.download(src, file_path)
            print(f"\nИзображение сохранено как {file_path}")
            count += 1
        except Exception as download_error:
            print(f"\nОшибка при загрузке {src}: {download_error}")
        