import cv2
from deepface import DeepFace
from datetime import datetime
import os
import sqlite3

def get_registered_faces():
    conn = sqlite3.connect("faces.db")
    c = conn.cursor()
    c.execute("SELECT name, image_path FROM workers")
    data = c.fetchall()
    conn.close()
    return data  # [(name, path), ...]

def recognize_face():
    data = get_registered_faces()
    cap = cv2.VideoCapture(0)
    recognized = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Rasmini vaqtincha saqlaymiz
        temp_path = "temp.jpg"
        cv2.imwrite(temp_path, frame)

        for name, db_image in data:
            try:
                result = DeepFace.verify(img1_path=temp_path, img2_path=db_image, enforce_detection=False)

                if result['verified']:
                    print(f"✅ Aniqlangan foydalanuvchi: {name}")
                    save_attendance(name)
                    recognized = True
                    break
            except Exception as e:
                print(f"❌ Solishtirishda xatolik: {e}")

        os.remove(temp_path)
        cv2.imshow("Yuzni aniqlash", frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or recognized:
            break

    cap.release()
    cv2.destroyAllWindows()

def save_attendance(name):
    conn = sqlite3.connect("faces.db")
    c = conn.cursor()

    # Jadval yo'q bo‘lsa, yaratamiz
    c.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )
    ''')

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO attendance (name, time) VALUES (?, ?)", (name, now))
    conn.commit()
    conn.close()


recognize_face()