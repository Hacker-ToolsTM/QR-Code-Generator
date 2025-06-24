import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode
from io import BytesIO

def generate_qr():
    url = entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    try:
        qr = qrcode.make(url)
        bio = BytesIO()
        qr.save(bio, format='PNG')
        bio.seek(0)

        img = Image.open(bio)
        img = img.resize((200, 200))
        qr_img = ImageTk.PhotoImage(img)

        qr_label.config(image=qr_img)
        qr_label.image = qr_img
        status_label.config(text="✅ Your QR code is ready!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("300x400")
root.configure(bg="#f0faff")

tk.Label(root, text="Enter a URL:", bg="#f0faff").pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Generate QR Code", command=generate_qr).pack(pady=10)

qr_label = tk.Label(root, bg="#f0faff")
qr_label.pack(pady=10)

status_label = tk.Label(root, text="", bg="#f0faff")
status_label.pack()

root.mainloop()
