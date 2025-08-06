# import os
# import time
# import telepot
# from pytubefix import YouTube
# import instaloader

# DOWNLOAD_FOLDER = os.path.join(os.path.expanduser("~"), "Videos")
# TOKEN = "7626812897:AAHSgw_7DO9JJpxYvlWQW8UHyKx0BH1np_U"

import os
import time
import telepot
from pytubefix import YouTube
import instaloader
from config import TOKEN

bot = telepot.Bot(TOKEN)

TEMP_DIR = "temp_download"
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

def handle(msg):
    if 'text' not in msg:
        return

    chat_id = msg['chat']['id']
    text = msg['text'].strip()

    if text == "/start":
        bot.sendMessage(chat_id, "Instagram yoki Youtube video uchun link yuboring")
        bot.sendMessage(chat_id, "Киньте ссылку на Ютуб или Инстаграм видео")
        return

    if not text.startswith("http"):
        bot.sendMessage(chat_id, "Iltimos to'g'ri link yuboring !")
        bot.sendMessage(chat_id, "Пожалуйста киньте правильную ссылку !")
        return

    try:
        bot.sendMessage(chat_id, "Yuklanmoqda ... | Загружается...")

        if "youtube.com" in text or "youtu.be" in text:
            yt = YouTube(text)
            stream = yt.streams.get_highest_resolution()
            file_path = stream.download(output_path=TEMP_DIR)

        elif "instagram.com" in text:
            loader = instaloader.Instaloader(dirname_pattern=TEMP_DIR, save_metadata=False, download_comments=False)
            shortcode = text.split("/")[-2]
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
            loader.download_post(post, target="insta_temp")
            folder_path = os.path.join(TEMP_DIR, "insta_temp")
            files = [f for f in os.listdir(folder_path) if f.endswith((".mp4", ".jpg"))]
            if files:
                file_path = os.path.join(folder_path, files[0])
            else:
                bot.sendMessage(chat_id, "Hech qanday video topilmadi.")
                bot.sendMessage(chat_id, "Не нашлось никакое видео.")
                return

        else:
            bot.sendMessage(chat_id, "Men faqat Youtube yoki Instagram link qabul qilaman.")
            bot.sendMessage(chat_id, "Может принимать только Ютуб или Инстаграм ссылку.")
            return

        with open(file_path, 'rb') as f:
            bot.sendVideo(chat_id, f)
            bot.sendMessage(chat_id,"Bot Geeks Andijan o'quvchilari tomonidan tayyorlangan !")
            bot.sendMessage(chat_id,"Dasturlashni mukammal o'rganmoqchi bo'lsangiz, @geeks_support ga yozing !")

        # Faylni o‘chirish
        if os.path.exists(file_path):
            os.remove(file_path)
        if "insta_temp" in file_path:
            import shutil
            shutil.rmtree(os.path.join(TEMP_DIR, "insta_temp"), ignore_errors=True)

    except Exception as e:
        bot.sendMessage(chat_id, f"Xatolik yuz berdi:\n{e}")
        bot.sendMessage(chat_id, f"Произошла ошибка:\n{e}")

bot.message_loop(handle)

print("Бот запустился.")
while True:
    time.sleep(10)