# log_aktivitas_ui.py
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def catat_log():
    waktu = datetime.now().strftime("%H:%M")
    teks = f"[{waktu}] Program dijalankan\n"

    with open("log.txt", "a") as f:
        f.write(teks)

    messagebox.showinfo("Sukses", f"Log dicatat:\n{teks}")

def tampilkan_log():
    text_log.delete("1.0", tk.END)
    try:
        with open("log.txt", "r") as f:
            text_log.insert(tk.END, f.read())
    except FileNotFoundError:
        text_log.insert(tk.END, "Belum ada log.")


# UI
root = tk.Tk()
root.title("Log Aktivitas")
root.geometry("400x350")

btn_catat = tk.Button(root, text="Catat Log", width=20, bg="#43b581", fg="white", command=catat_log)
btn_catat.pack(pady=10)

btn_tampil = tk.Button(root, text="Tampilkan Log", width=20, bg="#7289da", fg="white", command=tampilkan_log)
btn_tampil.pack(pady=10)

text_log = tk.Text(root, width=45, height=12)
text_log.pack(pady=10)

root.mainloop()
