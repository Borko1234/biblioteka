import tkinter as tk
from tkinter import messagebox

class LibraryManagementGUI:
    def __init__(self, master, filename):
        self.master = master
        master.title("Library Management System")

        # Window size and centering
        window_width = 400
        window_height = 200
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
        self.label1 = tk.Label(master, text="Book Name:", font=label_font)
        self.label1.grid(row=0, column=0, sticky="w")

        self.book_name_entry = tk.Entry(master, font=entry_font)
        self.book_name_entry.grid(row=0, column=1, sticky="ew")

        self.label2 = tk.Label(master, text="Borrower's Name:", font=label_font)
        self.label2.grid(row=1, column=0, sticky="w")

        self.borrower_name_entry = tk.Entry(master, font=entry_font)
        self.borrower_name_entry.grid(row=1, column=1, sticky="ew")

        self.label3 = tk.Label(master, text="Loan Period (days):", font=label_font)
        self.label3.grid(row=2, column=0, sticky="w")

        self.loan_period_entry = tk.Entry(master, font=entry_font)
        self.loan_period_entry.grid(row=2, column=1, sticky="ew")

        self.add_button = tk.Button(master, text="Add Loan", command=self.add_loan, font=button_font)
        self.add_button.grid(row=3, column=0, sticky="ew")

        self.remove_button = tk.Button(master, text="Remove Loan", command=self.remove_loan, font=button_font)
        self.remove_button.grid(row=3, column=1, sticky="ew")

        self.view_button = tk.Button(master, text="View All Loans", command=self.view_loans, font=button_font)
        self.view_button.grid(row=4, column=0, columnspan=2, sticky="ew")

        # Grid configuration
        master.grid_columnconfigure(1, weight=1)

    def load_loans(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    book_name, borrower_name, loan_period = line.strip().split(',')
                    self.book_loans.append({
                        "book_name": book_name,
                        "borrower_name": borrower_name,
                        "loan_period": loan_period
                    })
        except FileNotFoundError:
            pass

    def save_loans(self):
        with open(self.filename, 'w') as file:
            for loan in self.book_loans:
                file.write(f"{loan['book_name']},{loan['borrower_name']},{loan['loan_period']}\n")

    def add_loan(self):
        book_name = self.book_name_entry.get()
        borrower_name = self.borrower_name_entry.get()
        loan_period = self.loan_period_entry.get()

        self.book_loans.append({
            "book_name": book_name,
            "borrower_name": borrower_name,
            "loan_period": loan_period
        })
        self.save_loans()

        messagebox.showinfo("Success", "Book loan added successfully")

    def remove_loan(self):
        book_name = self.book_name_entry.get()
        self.book_loans = [loan for loan in self.book_loans if loan['book_name'] != book_name]
        self.save_loans()

        messagebox.showinfo("Success", "Book loan removed successfully")

    def view_loans(self):
        loans = "\n".join([f"Book: {loan['book_name']}, Borrowed By: {loan['borrower_name']}, Loan Period: {loan['loan_period']} days" for loan in self.book_loans])
        messagebox.showinfo("All Book Loans", loans)

# Run the application
root = tk.Tk()
filename = "library_loans.txt"
app = LibraryManagementGUI(root, filename)
root.mainloop()
