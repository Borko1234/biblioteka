"""
import tkinter as tk
import random
random_number = round(random.uniform(1, 17), 2)
print(f"The random number is: {random_number}")
print('Let\'s play a game')
guess = input("Guess the number: ")
if float(guess) == random_number:
    print('You won this time!')
else:
    print('C:/Windows/System32')"""

"""
import tkinter as tk
from tkinter import messagebox
import random

# Function to compare the guessed number with the random number
def check_guess():
    try:
        guessed_number = float(entry.get())  # Get the guessed number from the entry widget
        if guessed_number == random_number:

            messagebox.showinfo("WOW!","You won this time!")
        else:

            messagebox.showwarning('Didn\'t guesst right nigga',"Delete C:/Windows/System32")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Generate a random number between 1 and 100
random_number = round(random.uniform(1, 10), 2)

# Create the main window
root = tk.Tk()
root.title("Lets play a game")
root.geometry("500x250")
# Create a label and an entry widget for number input
label = tk.Label(root, text="Guess the number")
label2 = tk.Label(root, text=f"The random number is {random_number}")
label.pack(padx=20, pady=5)
label2.pack(padx=22, pady=5)#tova e kude da pokaje random chisloto

entry = tk.Entry(root)
entry.pack(padx=20, pady=5)

# Create a button to check the guessed number against the random number
check_button = tk.Button(root, text="Check Guess", command=check_guess)
check_button.pack(padx=20, pady=10)
# Run the application
root.mainloop()
"""
# Simple Library Management System

# Updated Library Management System with console interaction and file storage

class LibraryManagement:
    def __init__(self, filename):
        self.filename = filename
        self.book_loans = []
        self.load_loans()

    def load_loans(self):
        # Load book loans from the file
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
            # File doesn't exist yet, will be created on save
            pass

    def save_loans(self):
        # Save book loans to the file
        with open(self.filename, 'w') as file:
            for loan in self.book_loans:
                file.write(f"{loan['book_name']},{loan['borrower_name']},{loan['loan_period']}\n")

    def add_loan(self, book_name, borrower_name, loan_period):
        # Add a new loan record
        self.book_loans.append({
            "book_name": book_name,
            "borrower_name": borrower_name,
            "loan_period": loan_period
        })
        self.save_loans()

    def remove_loan(self, book_name):
        # Remove a loan record by book name
        self.book_loans = [loan for loan in self.book_loans if loan['book_name'] != book_name]
        self.save_loans()

    def view_loans(self):
        # Print all loan records
        for loan in self.book_loans:
            print(f"Book: {loan['book_name']}, Borrowed By: {loan['borrower_name']}, Loan Period: {loan['loan_period']} days")

    def console_interface(self):
        while True:
            print("\nLibrary Management System")
            print("1. Add a book loan")
            print("2. Remove a book loan")
            print("3. View all book loans")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                book_name = input("Enter book name: ")
                borrower_name = input("Enter borrower's name: ")
                loan_period = input("Enter loan period (days): ")
                self.add_loan(book_name, borrower_name, loan_period)
            elif choice == "2":
                book_name = input("Enter book name to remove: ")
                self.remove_loan(book_name)
            elif choice == "3":
                self.view_loans()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

# Example usage - to be run in a Python environment
filename = "library_loans.txt"
library = LibraryManagement(filename)
library.console_interface()












