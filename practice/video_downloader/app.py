# pip install pytube instaloader
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pytubefix import YouTube
import instaloader

DEFAULT_FOLDER = os.path.join(os.path.expanduser("~"), "Videos")

class VideoDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Yuklab olish")
        self.root.geometry("400x250")

        self.url_var = tk.StringVar()
        self.folder_path = DEFAULT_FOLDER

        tk.Label(root, text="Video URL (YouTube / Instagram):",
                 font=("Arial",16)).pack(pady=5)
        self.url_entry = tk.Entry(root, textvariable=self.url_var, width=50)
        self.url_entry.pack(pady=5)

        tk.Button(root, text="Joy Tanlash", command=self.select_folder).pack(pady=5)
        tk.Button(root, text="Yuklab olish", command=self.download_video).pack(pady=5)

        self.status_label = tk.Label(root, text="", fg="green")
        self.status_label.pack(pady=10)

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.status_label.config(text=f"Tanlangan papka: {self.folder_path}")

    def download_video(self):
        url = self.url_var.get()
        if not url or not self.folder_path:
            messagebox.showwarning("Ogohlantirish", "Iltimos, URL va papkani tanlang!")
            return

        try:
            if "youtube.com" in url or "youtu.be" in url:
                yt = YouTube(url)
                stream = yt.streams.get_highest_resolution()
                stream.download(output_path=self.folder_path)
                self.status_label.config(text="YouTube video yuklandi!")

            elif "instagram.com" in url:
                loader = instaloader.Instaloader(dirname_pattern=self.folder_path)
                shortcode = url.split("/")[-2]
                loader.download_post(instaloader.Post.from_shortcode(loader.context, shortcode), target="")
                self.status_label.config(text="Instagram video yuklandi!")

            else:
                self.status_label.config(text="Noto‘g‘ri URL!", fg="red")

        except Exception as e:
            messagebox.showerror("Xatolik", f"Xatolik yuz berdi:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoDownloaderApp(root)
    root.mainloop()
