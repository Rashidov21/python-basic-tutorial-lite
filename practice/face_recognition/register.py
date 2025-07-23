import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import shutil
import os
import sqlite3

def register_from_file():
    # Foydalanuvchi ismini so‘rash
    name = simpledialog.askstring("Ro'yxatdan o'tkazish", "Foydalanuvchi ismini kiriting:")
    if not name:
        return
    # Rasm faylini tanlash
    filepath = filedialog.askopenfilename(
        title="Rasmni tanlang",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        )
    if filepath:
        # Saqlash yo‘li
        os.makedirs("images", exist_ok=True)
        save_path = os.path.join("images", f"{name}.jpg")
        try:
                shutil.copyfile(filepath, save_path)

                # DB ga yozish
                conn = sqlite3.connect("faces.db")
                c = conn.cursor()
                c.execute("INSERT INTO workers (name, image_path) VALUES (?, ?)", (name, save_path))
                conn.commit()
                conn.close()
                messagebox.showinfo("Muvaffaqiyatli", f"{name} ro'yxatdan o'tkazildi!")
        except Exception as e:
                messagebox.showerror("Xatolik", f"Faylni saqlashda yoki DBga yozishda xatolik: {e}")
    else:
        messagebox.showwarning("Xatolik", "Rasm tanlanmadi.")

# GUI oynasi
window = tk.Tk()
window.title("Foydalanuvchini qo‘shish")
window.geometry("300x150")

btn = tk.Button(window, text="Rasm orqali qo‘shish", command=register_from_file)
btn.pack(pady=40)

window.mainloop()
