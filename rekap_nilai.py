# rekap_nilai_ui.py
import tkinter as tk
from tkinter import messagebox

def simpan_data():
    nama = entry_nama.get()
    tugas = entry_tugas.get()
    uts = entry_uts.get()
    uas = entry_uas.get()

    if not nama or not tugas or not uts or not uas:
        messagebox.showwarning("Peringatan", "Semua field harus diisi!")
        return

    try:
        tugas = int(tugas)
        uts = int(uts)
        uas = int(uas)
    except:
        messagebox.showerror("Error", "Nilai harus berupa angka!")
        return

    with open("nilai_mahasiswa.txt", "a") as f:
        f.write(f"{nama},{tugas},{uts},{uas}\n")

    messagebox.showinfo("Sukses", "Data berhasil disimpan.")

    entry_nama.delete(0, tk.END)
    entry_tugas.delete(0, tk.END)
    entry_uts.delete(0, tk.END)
    entry_uas.delete(0, tk.END)


def tampilkan_rekap():
    text_rekap.delete("1.0", tk.END)
    text_rekap.insert(tk.END, "=== REKAP NILAI MAHASISWA ===\n")
    text_rekap.insert(tk.END, "Nama\tTugas\tUTS\tUAS\tRata2\n")

    try:
        with open("nilai_mahasiswa.txt", "r") as f:
            for baris in f:
                nama, tugas, uts, uas = baris.strip().split(",")
                tugas = int(tugas)
                uts = int(uts)
                uas = int(uas)
                rata = (tugas + uts + uas) / 3

                text_rekap.insert(
                    tk.END, f"{nama}\t{tugas}\t{uts}\t{uas}\t{rata:.2f}\n"
                )
    except FileNotFoundError:
        text_rekap.insert(tk.END, "Belum ada data.")


# UI
root = tk.Tk()
root.title("Rekap Nilai Mahasiswa")
root.geometry("500x450")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Nama").grid(row=0, column=0)
entry_nama = tk.Entry(frame)
entry_nama.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Tugas").grid(row=1, column=0)
entry_tugas = tk.Entry(frame)
entry_tugas.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="UTS").grid(row=2, column=0)
entry_uts = tk.Entry(frame)
entry_uts.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="UAS").grid(row=3, column=0)
entry_uas = tk.Entry(frame)
entry_uas.grid(row=3, column=1, padx=10, pady=5)

btn_simpan = tk.Button(root, text="Simpan Data", width=20, bg="#43b581", fg="white", command=simpan_data)
btn_simpan.pack(pady=5)

btn_rekap = tk.Button(root, text="Tampilkan Rekap", width=20, bg="#7289da", fg="white", command=tampilkan_rekap)
btn_rekap.pack(pady=5)

text_rekap = tk.Text(root, width=60, height=15)
text_rekap.pack(pady=10)

root.mainloop()
