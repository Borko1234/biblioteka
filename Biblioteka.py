import tkinter as tk
from tkinter import messagebox
import sqlite3


def create_database_and_table():
    cnt = sqlite3.connect("inventar.db")
    cursor = cnt.cursor()
    cursor.execute(
        """CREATE TABLE available (
        title TEXT,
        date TEXT,
        inventar_num INTEGER,
        signatura INTEGER,
        bg_avtor TEXT,
        chujd_avtor TEXT,
        nalichen_broi INTEGER
        )"""
    )
    cnt.commit()


def run_app():
    root = tk.Tk()
    filename = "library_loans.txt"
    app = LibraryManagementGUI(root, filename)
    root.mainloop()


class LibraryManagementGUI:
    def __init__(self, master):
        self.master = master
        master.title("Инвентарна книга")

        window_width = 500
        window_height = 300
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        center_x = int((screen_width / 2) - (window_width / 2))
        center_y = int((screen_height / 2) - (window_height / 2))
        master.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        label_font = ("Arial", 12)
        entry_font = ("Arial", 12)
        button_font = ("Arial", 12)

        self.label1 = tk.Label(master, text="Име на книгата:", font=label_font)
        self.label1.grid(row=0, column=0, sticky="w")

        self.kniga_ime_entry = tk.Entry(master, font=entry_font)
        self.kniga_ime_entry.grid(row=0, column=1, sticky="ew")

        self.label2 = tk.Label(master, text="Автор: ", font=label_font)
        self.label2.grid(row=2, column=0, sticky="w")

        self.kniga_avtor_entry = tk.Entry(master, font=entry_font)
        self.kniga_avtor_entry.grid(row=2, column=1, sticky="ew")

        self.label3 = tk.Label(master, text="Дата на вписване:", font=label_font)
        self.label3.grid(row=4, column=0, sticky="w")

        self.data_vpisvane_entry = tk.Entry(master, font=entry_font)
        self.data_vpisvane_entry.grid(row=4, column=1, sticky="ew")

        self.label8 = tk.Label(master, text="Инвентарен номер", font=label_font)
        self.label8.grid(row=6, column=0, sticky="w")

        self.inventar_num_entry = tk.Entry(master, font=entry_font)
        self.inventar_num_entry.grid(row=6, column=1, sticky="ew")

        self.label4 = tk.Label(master, text="Сигнатура", font=label_font)
        self.label4.grid(row=8, column=0, sticky="w")

        self.signatura_entry = tk.Entry(master, font=entry_font)
        self.signatura_entry.grid(row=8, column=1, sticky="ew")

        self.label5 = tk.Label(master, text="БГ автор", font=label_font)
        self.label5.grid(row=10, column=0, sticky="w")

        self.bg_avtor_entry = tk.Entry(master, font=entry_font)
        self.bg_avtor_entry.grid(row=10, column=1, sticky="ew")

        self.label6 = tk.Label(master, text="Чужд автор", font=label_font)
        self.label6.grid(row=12, column=0, sticky="w")

        self.chujd_avtor_entry = tk.Entry(master, font=entry_font)
        self.chujd_avtor_entry.grid(row=12, column=1, sticky="ew")

        self.label7 = tk.Label(master, text="Наличен брой", font=label_font)
        self.label7.grid(row=14, column=0, sticky="w")

        self.nalichen_broi_entry = tk.Entry(master, font=entry_font)
        self.nalichen_broi_entry.grid(row=14, column=1, sticky="ew")

        self.add_button = tk.Button(
            master, text="Добавяне на книгата", command=self.add_loan, font=button_font
        )
        self.add_button.grid(row=16, column=0, sticky="ew")

        self.view_button = tk.Button(
            master, text="Инвентар", command=self.view_loans, font=button_font
        )
        self.view_button.grid(row=16, column=1, columnspan=2, sticky="ew")

        master.grid_columnconfigure(1, weight=1)
