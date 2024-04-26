import tkinter as tk
import BiblotekaClass as BC

root = tk.Tk()
app = BC.LibraryManagementGUI(root, BC.path)
root.mainloop()


import tkinter as tk
from tkinter import messagebox
import openpyxl
from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook

wb = Workbook()
ws = wb.active
wb.save('sample.xlsx')
path = "biblioteka.xlsx"

class LibraryManagementGUI:
    def __init__(self, master, filename):
        self.master = master
        master.title("Библиотечен мениджър")

        # Window size and centering
        window_width = 500
        window_height = 300
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        center_x = int((screen_width / 2) - (window_width / 2))
        center_y = int((screen_height / 2) - (window_height / 2))
        master.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        self.filename = filename
        self.book_loans = []
        self.load_loans()

        # Font configuration
        label_font = ('Arial', 12)
        entry_font = ('Arial', 12)
        button_font = ('Arial', 12)

        # Layout
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

        self.loan_period_entry = tk.Entry(master, font=entry_font)
        self.loan_period_entry.grid(row=4, column=1, sticky="ew")

        self.add_button = tk.Button(master, text="Добавяне на книгата", command=self.add_loan, font=button_font)
        self.add_button.grid(row=10, column=0, sticky="ew")
        self.view_button = tk.Button(master, text="Инвентар", command=self.view_loans, font=button_font)
        self.view_button.grid(row=10, column=1, columnspan=2, sticky="ew")

        # Grid configuration
        master.grid_columnconfigure(1, weight=1)

    def load_loans(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    kniga_ime, kniga_avtor, loan_period = line.strip().split(',')
                    self.book_loans.append({
                        "Име на книгата: ": kniga_ime,
                        "Автор": kniga_avtor,
                        "Период": loan_period
                    })
        except FileNotFoundError:
            pass

    def save_loans(self):
        with open(self.filename, 'w') as file:
            for loan in self.book_loans:
                file.write(f"{loan['Име на книгата: ']},{loan['Автор']},{loan['Период']}\n")

    def add_loan(self):
        kniga_ime = self.kniga_ime_entry.get()
        kniga_avtor = self.kniga_avtor_entry.get()
        loan_period = self.loan_period_entry.get()

    def view_loans(self):
        loans = "\n".join(
            [f"Book: {loan['kniga_ime']}, Автор: {loan['kniga_avtor']}, Дата на вписване: {loan['loan_period']} days"
             for loan in self.book_loans])
        messagebox.showinfo("All Book Loans", loans)
