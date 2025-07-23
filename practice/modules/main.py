import datetime
import json
import time 
import os 
import random # bu hammasini import qilish
from random import randint # bu faqat kerakli narsani import qilish

from bs4 import BeautifulSoup
from PIL import Image

# import data 
# import db 
from data import show_data
from db import create_db



show_data()
create_db()

print(random.randint(23,50))