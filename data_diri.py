import tkinter as tk
from tkinter import messagebox
import os

# FUNGSI MENAMBAHKAN DATA SISWA
def save_data(): 
    nama = entry_nama.get()
    nim = entry_nim.get()
    prodi = entry_prodi.get()

    # memastikan file di folder yang sama
    script_dir = os.path.dirname(os.path.abspath(__file__))
    biodata_path = os.path.join(script_dir, "biodata.txt")

    with open(biodata_path, "a") as f:   # io untuk menambahkan ke biodata.path
        f.write(f"{nama} | {nim} | {prodi}\n")   # ← MASUK BLOK WITH

    display_file()

def display_file():
    text_display.delete("1.0", tk.END)
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        biodata_path = os.path.join(script_dir, "biodata.txt")
        with open(biodata_path, "r") as f: #io untuk nemapilkan data ke ui
            text_display.insert(tk.END, f.read())
    except FileNotFoundError:
        text_display.insert(tk.END, "File belum tersedia.")


# WINDOW UTAMA

root = tk.Tk()
root.title("Input Biodata Mahasiswa")
root.configure(bg="#FAF3E1")

main_frame = tk.Frame(root, bg="#FAF3E1")
main_frame.pack(padx=20, pady=20)

label_style = {"fg": "black", "bg": "#FAF3E1"}
entry_style = {"bg": "#ffffff", "fg": "black"}

tk.Label(main_frame, text="Nama", **label_style).grid(row=0, column=0, sticky="w", pady=5)
entry_nama = tk.Entry(main_frame, width=30, **entry_style)
entry_nama.grid(row=0, column=1, pady=5, padx=10)

tk.Label(main_frame, text="NIM", **label_style).grid(row=1, column=0, sticky="w", pady=5)
entry_nim = tk.Entry(main_frame, width=30, **entry_style)
entry_nim.grid(row=1, column=1, pady=5, padx=10)

tk.Label(main_frame, text="Prodi", **label_style).grid(row=2, column=0, sticky="w", pady=5)
entry_prodi = tk.Entry(main_frame, width=30, **entry_style)
entry_prodi.grid(row=2, column=1, pady=5, padx=10)
#button untuk mengirim data ke biodata.txt memanggil fungsi save_data
btn_save = tk.Button(
    main_frame,
    text="Simpan",
    bg="#7289da",
    fg="white",
    padx=10,
    pady=5,
    command=save_data
)
btn_save.grid(row=3, column=0, columnspan=2, pady=15)
#tampilan output program
text_display = tk.Text(
    root,
    width=60,
    height=12,
    bg="white",
    fg="black",
    padx=10,
    pady=10,
    highlightbackground="#99aab5"
)
text_display.pack(padx=20, pady=10)

root.mainloop()
