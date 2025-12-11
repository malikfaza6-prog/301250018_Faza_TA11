# menu.py
import tkinter as tk
import os
import subprocess

# -----------------------------
# Fungsi membuka program lain
# -----------------------------

def buka_biodata():
    subprocess.Popen(["python", "data_diri.py"])

def buka_rekap_nilai():
    subprocess.Popen(["python", "rekap_nilai.py"])

def jalankan_log():
    subprocess.Popen(["python", "log_aktivitas.py"])


# -----------------------------
# UI MENU UTAMA
# -----------------------------
root = tk.Tk()
root.title("Menu Program")
root.geometry("350x300")
root.configure(bg="#E8EEF1")

frame = tk.Frame(root, bg="#E8EEF1")
frame.pack(pady=40)

label = tk.Label(frame, text="MENU UTAMA PROGRAM", font=("Arial", 14, "bold"), bg="#E8EEF1")
label.pack(pady=10)

# Tombol Biodata
btn_biodata = tk.Button(
    frame,
    text="Input Biodata Mahasiswa",
    width=25,
    height=2,
    bg="#7289da",
    fg="white",
    command=buka_biodata
)
btn_biodata.pack(pady=10)

# Tombol Rekap Nilai
btn_nilai = tk.Button(
    frame,
    text="Rekap Nilai Mahasiswa",
    width=25,
    height=2,
    bg="#43b581",
    fg="white",
    command=buka_rekap_nilai
)
btn_nilai.pack(pady=10)

# Tombol Log Aktivitas
btn_log = tk.Button(
    frame,
    text="Catat Log Aktivitas",
    width=25,
    height=2,
    bg="#faa61a",
    fg="white",
    command=jalankan_log
)
btn_log.pack(pady=10)

root.mainloop()
