import tkinter as tk
from tkinter import messagebox



class LibraryManagementGUI:
    def __init__(self, master, filename):
        self.master = master
        master.title("")

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

        self.add_button = tk.Button(master, text="Добавяне на книгата", command=self.add_loan, font=button_font)
        self.add_button.grid(row=16, column=0, sticky="ew")
        self.view_button = tk.Button(master, text="Инвентар", command=self.view_loans, font=button_font)
        self.view_button.grid(row=16, column=1, columnspan=2, sticky="ew")

        # Grid configuration
        master.grid_columnconfigure(1, weight=1)

    def load_loans(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    # Splitting the line by commas
                    parts = line.strip().split(',')
                    # Checking if the line has the expected number of parts
                    if len(parts) == 8:
                        kniga_ime, kniga_avtor, data_vpisvane,inventaren_num, signatura, bg_avtor, chujd_avtor, nalichen_broi = parts
                        self.book_loans.append({
                            "Име на книгата: ": kniga_ime,
                            "Автор на книгата": kniga_avtor,
                            "Дата на вписване: ": data_vpisvane,
                            "Инвентарен номер":inventaren_num,
                            "Сигнатура": signatura,
                            "БГ автор": bg_avtor,
                            "Чужд автор": chujd_avtor,
                            "Наличен брой:": nalichen_broi

                        })
                    else:
                        # If the line doesn't have the expected format, skip it or handle the error as per your requirement
                        print(f"Invalid line: {line}")
        except FileNotFoundError:
            pass

    def save_loans(self):
        with open(self.filename, 'w') as file:
            for loan in self.book_loans:
                # Check if all keys exist before accessing them
                if all(key in loan for key in
                       ['Име на книгата: ', 'Автор на книгата', 'Дата на вписване: ', "Инвентарен номер",'Сигнатура', 'БГ автор', 'Чужд автор','Наличен брой']):
                    file.write(
                        f"{loan['Име на книгата: ']},{loan['Автор на книгата']},{loan['Дата на вписване: ']},{load['Инвентарен номер']}"
                        f",{loan['Сигнатура']},{loan['БГ автор']},{loan['Чужд автор']},{loan['Наличен брой']}\n")

    def add_loan(self):
        kniga_ime = self.kniga_ime_entry.get()
        kniga_avtor = self.kniga_avtor_entry.get()
        data_vpisvane = self.data_vpisvane_entry.get()
        inventaren_num=self.data_vpisvane_entry.get()
        signatura = self.signatura_entry.get()
        bg_avtor=self.bg_avtor_entry.get()
        chujd_avtor=self.chujd_avtor_entry.get()
        nalichen_broi=self.nalichen_broi_entry.get()

        self.book_loans.append({
            "Име на книгата: ": kniga_ime,
            "Автор на книгата: ": kniga_avtor,
            "Дата на вписване: ": data_vpisvane,
            "Инвентарен номер": inventaren_num,
            "Сигнатура": signatura,
            "БГ автор": bg_avtor,
            "Чужд автор": chujd_avtor,
            "Наличен брой": nalichen_broi
        })
        self.save_loans()

        messagebox.showinfo("Успешно", "Книгата е добавена успешно!")

    def view_loans(self):
        loans = "\n".join(
            [
                f"Book: {loan['Име на книгата: ']}, Автор: {loan.get('Автор на книгата', '')}, Дата на вписване: {loan['Дата на вписване: ']},Инвентарен номер{loan['Инвентарен номер']}"
                f", Сигнатура: {loan['Сигнатура']}, БГ автор {loan['БГ автор']}, Чужд автор {loan['Чужд автор']},Наличен брой:{loan['Наличен брой']}"
                for loan in self.book_loans if
                all(key in loan for key in ['Име на книгата: ', 'Дата на вписване: ', 'Сигнатура'])
            ])
        messagebox.showinfo("All Book Loans", loans)


# Run the application
root = tk.Tk()
filename = "library_loans.txt"
app = LibraryManagementGUI(root, filename)
root.mainloop()
