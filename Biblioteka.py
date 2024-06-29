import tkinter as tk
from tkinter import ttk
import sqlite3

cnt = sqlite3.connect("inventar.db")


def create_database_and_table():
    cursor = cnt.cursor()
    available = """
    CREATE TABLE IF NOT EXISTS available (
    Име TEXT,
    Автор TEXT,
    Дата на вписване TEXT,
    Инвентар TEXT,
    Сигнатура TEXT,
    Бг автор TEXT,
    Чужд автор TEXT,
    Наличен брой INT)
    """
    taken = """
    CREATE TABLE IF NOT EXISTS available (
    Име TEXT,
    Автор TEXT,
    Дата на вписване TEXT,
    Инвентар TEXT,
    Сигнатура TEXT,
    Бг автор TEXT,
    Чужд автор TEXT,
    Взет брой INT)
    """
    cursor.execute(available)
    cursor.execute(taken)
    cnt.commit()


def run_app():
    root = tk.Tk()
    LibraryManagementGUI(root)
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

        font = ("Arial", 12)

        self.label1 = tk.Label(master, text="Име на книгата:", font=font)
        self.label1.grid(row=0, column=0, sticky="w")
        self.ime = tk.StringVar()
        self.kniga_ime_entry = tk.Entry(master, textvariable=self.ime, font=font)
        self.kniga_ime_entry.grid(row=0, column=1, sticky="ew")

        self.label2 = tk.Label(master, text="Автор: ", font=font)
        self.label2.grid(row=2, column=0, sticky="w")
        self.avtor = tk.StringVar()
        self.kniga_avtor_entry = tk.Entry(master, textvariable=self.avtor, font=font)
        self.kniga_avtor_entry.grid(row=2, column=1, sticky="ew")

        self.label8 = tk.Label(master, text="Инвентарен номер", font=font)
        self.label8.grid(row=6, column=0, sticky="w")
        self.invent_num = tk.StringVar()
        self.inventar_num_entry = tk.Entry(master, textvariable=self.invent_num, font=font)
        self.inventar_num_entry.grid(row=6, column=1, sticky="ew")

        self.label4 = tk.Label(master, text="Сигнатура", font=font)
        self.label4.grid(row=8, column=0, sticky="w")
        self.signat = tk.StringVar()
        self.signatura_entry = tk.Entry(master, textvariable=self.signat, font=font)
        self.signatura_entry.grid(row=8, column=1, sticky="ew")

        self.label5 = tk.Label(master, text="БГ автор", font=font)
        self.label5.grid(row=10, column=0, sticky="w")
        self.bgavtor = tk.StringVar()
        self.bg_avtor_entry = tk.Entry(master, textvariable=self.bgavtor, font=font)
        self.bg_avtor_entry.grid(row=10, column=1, sticky="ew")

        self.label6 = tk.Label(master, text="Чужд автор", font=font)
        self.label6.grid(row=12, column=0, sticky="w")
        self.chujdavtor = tk.StringVar()
        self.chujd_avtor_entry = tk.Entry(master, textvariable=self.chujdavtor, font=font)
        self.chujd_avtor_entry.grid(row=12, column=1, sticky="ew")

        self.label9 = tk.Label(master, text="Налични книги", font=font)
        self.label9.grid(row=14, column=0, sticky="w")
        self.nalichni_knigi = tk.IntVar()
        self.nalichni_knigi = tk.Entry(master, textvariable=self.nalichni_knigi, font=font)
        self.nalichni_knigi.grid(row=14, column=1, sticky="ew")

        self.add_button = tk.Button(
            master, text="Добавяне на книга", command=self.add_book, font=font, bg="#d1cfcf", relief="raised"
        )
        self.add_button.grid(row=16, column=0, sticky="ew")

        self.view_button = tk.Button(
            master, text="Инвентар", command=self.view_invent, font=font, bg="#d1cfcf", relief="raised"
        )
        self.view_button.grid(row=16, column=1, columnspan=1, sticky="ew")

        self.view_button = tk.Button(
            master, text="Отдаване на книга", command=self.loan_book, font=font, bg="#d1cfcf", relief="raised"
        )
        self.view_button.grid(row=16, column=2, columnspan=2, sticky="ew")

        self.view_button = tk.Button(
            master, text="Взети книги", command=self.view_loans, font=font, bg="#d1cfcf", relief="raised"
        )
        self.view_button.grid(row=18, column=1, columnspan=1, sticky="ew")

        self.view_button = tk.Button(
            master, text="Връщане на книга", command=self.return_book, font=font, bg="#d1cfcf", relief="raised"
        )
        self.view_button.grid(row=18, column=2, columnspan=2, sticky="ew")
        self.view_button = tk.Button(
            master, text="Редакция", command=self.edit_book, font=font, bg="#d1cfcf", relief="raised"
        )
        self.view_button.grid(row=18, column=0, sticky="ew")
        self.view_button = tk.Button(
            master, text="Премахване на книга", command=self.remove_book, font=font, bg="#d1cfcf", relief="raised"
        )
        self.view_button.grid(row=20, column=0, sticky="ew")
        self.view_button = tk.Button(
            master, text="Търсене", command=self.search, font=font, bg="#d1cfcf", relief="raised"
        )
        self.view_button.grid(row=20, column=1, sticky="ew")

        master.grid_columnconfigure(1, weight=1)

    def get_column_names(self):
        return ["Име",
                "Автор",
                "Дата на вписване",
                "Инвентар",
                "Сигнатура",
                "Бг автор",
                "Чужд автор",
                "Наличен брой"]

    def get_column_names2(self):
    return ["Име",
            "Автор",
            "Дата_на_вписване",
            "Инвентар",
            "Сигнатура",
            "Бг_автор",
            "Чужд_автор",
            "Взети книги"]

    def add_book(self):
        cur = cnt.cursor()

        data = (self.ime.get(),
                self.avtor.get(),
                self.invent_num.get(),
                self.signat.get(),
                self.bgavtor.get(),
                self.chujdavtor.get(),
                self.nalichni_knigi.get())

        insert_query = """
                INSERT INTO available (
                    Име TEXT,
                    Автор TEXT,
                    Дата на вписване TEXT,
                    Инвентар TEXT,
                    Сигнатура TEXT,
                    Бг автор TEXT,
                    Чужд автор TEXT,
                    Наличен брой INT) 

                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
        cur.execute(insert_query, data)

        cnt.commit()

    def edit_book(self):
        cur = cnt.cursor()
        available = "available"

        data = (self.ime.get(),
            self.avtor.get(),
            self.invent_num.get(),
            self.signat.get(),
            self.bgavtor.get(),
            self.chujdavtor.get(),
            self.nalichni_knigi.get())

        original_book_name = self.original_book_name

        search_value = [(original_book_name,)]
        column_name = ["Име"]
        conditions = []
        for i, value in enumerate(search_value):
            column = column_name[i]
            conditions.append(f"{column} = ?")

        where_clause = " AND ".join(conditions)

        update_query = f"""
            UPDATE {available}
        SET Име = ?,
            Автор = ?,
            Дата на вписване = ?,
            Инвентар = ?,
            Сигнатура = ?,
            Бг автор = ?,
            Чужд автор = ?,
            Наличен брой = ?
        WHERE {where_clause}
    """
        cur.execute(update_query, (*data,))
        cnt.commit()

    def clear(self):
        self.ime.set("")
        self.avtor.set("")
        self.invent_num.set("")
        self.signat.set("")
        self.bgavtor.set("")
        self.chujdavtor.set("")
        self.nalichni_knigi.delete(0, tk.END)

    def remove_book(self):
        cur = cnt.cursor()
        available = "available"

        name = self.ime.get()

        delete_query = f"""
            DELETE FROM {available} WHERE Име = '{name}'
        """
        cur.execute(delete_query)
        cnt.commit()

    def view_invent(self):
        table_window = tk.Toplevel(self.master)
        table_window.title("Инвентарна книга")

        table = ttk.Treeview(table_window, columns=self.get_column_names(), show="headings")

        for idx, column in enumerate(self.get_column_names()):
            table.heading(column, text=column)

        table.grid(row=0, column=1)

        cur = cnt.cursor()
        available = "available"
        query = f"SELECT * FROM {available}"
        cur.execute(query)
        all_rows = cur.fetchall()
        for idx, row in enumerate(all_rows):
            table.insert("", tk.END, values=row)

        table_window.mainloop()

    def loan_book(self):
        cur = cnt.cursor()
        available = "available"
        taken = "taken"
        data = (self.ime.get(),
                self.avtor.get(),
                self.invent_num.get(),
                self.signat.get(),
                self.bgavtor.get(),
                self.chujdavtor.get(),
                self.nalichni_knigi.get())

        search_value = [(self.ime.get(),)]
        column_name = ["Име"]
        conditions = []
        for i, value in enumerate(search_value):
            column = column_name[i]
            conditions.append(f"{column} = ?")

        where_clause = " AND ".join(conditions)

        query = f"SELECT * FROM {taken} WHERE {where_clause}"
        cur.execute(query, search_value)

        existing_book = cur.fetchone()

        if existing_book:
            update_query = f"""
                UPDATE {taken}
                SET Наличен брой = Наличен брой + 1
                WHERE {where_clause}
            """
            cur.execute(update_query, search_value)
        else:
            insert_query = f"""
                INSERT INTO {taken} ({", ".join(column_name + ["Наличен брой"])})
                VALUES (?, 1)  # Add with initial count of 1
            """
            cur.execute(insert_query, data[:1])

        available_count_query = f"""
            SELECT nalichni_knigi FROM {available} WHERE kniga_ime_entry = ?
        """
        cur.execute(available_count_query, (data[0],))
        current_count = cur.fetchone()

        if current_count:
            new_count = current_count[0] - 1
            if new_count >= 0:
                update_available_query = f"""
                    UPDATE {available}
                    SET Наличен брой = ?
                    WHERE Име = ?
                """
                cur.execute(update_available_query, (new_count, data[0]))
        cnt.commit()

    def return_book(self):
        cur = cnt.cursor()
        available = "available"
        taken = "taken"
        data = (self.ime.get(),
                self.avtor.get(),
                self.invent_num.get(),
                self.signat.get(),
                self.bgavtor.get(),
                self.chujdavtor.get(),
                self.nalichni_knigi.get())

        search_value = [(self.ime.get(),)]
        column_name = ["Име"]
        conditions = []
        for i, value in enumerate(search_value):
            column = column_name[i]
            conditions.append(f"{column} = ?")

        available_count_query = f"""
            SELECT Наличен брой FROM {available} WHERE Име = ?
        """
        cur.execute(available_count_query, (data[0],))
        current_available_count = cur.fetchone()

        if current_available_count:
            new_available_count = current_available_count[0] + 1
            update_available_query = f"""
                UPDATE {available}
                SET Наличен брой = ?
                WHERE Име = ?
            """
            cur.execute(update_available_query, (new_available_count, data[0]))

        taken_count_query = f"""
            SELECT Наличен брой FROM {taken} WHERE Име = ?
        """
        cur.execute(taken_count_query, (data[0],))
        current_taken_count = cur.fetchone()

        if current_taken_count:
            new_taken_count = current_taken_count[0] - 1

            if new_taken_count >= 0:
                update_taken_query = f"""
                    UPDATE {taken}
                    SET Наличен брой = ?
                    WHERE Име = ?
                """
                cur.execute(update_taken_query, (new_taken_count, data[0]))
            else:
                delete_query = f"""
                    DELETE FROM {taken}
                    WHERE Име = ?
                """
                cur.execute(delete_query, (data[0],))

        cnt.commit()

    def view_loans(self):
        table_window = tk.Toplevel(self.master)
        table_window.title("Инвентарна книга")

        table = ttk.Treeview(table_window, columns=self.get_column_names(), show="headings")

        for idx, column in enumerate(self.get_column_names2()):
            table.heading(column, text=column)

        table.grid(row=0, column=1)

        cur = cnt.cursor()
        taken_table = "taken"

        query = f"SELECT * FROM {taken_table}"
        cur.execute(query)
        all_rows = cur.fetchall()

        for idx, row in enumerate(all_rows):
            table.insert("", tk.END, values=row)

        table_window.mainloop()

    def search(self):
        search_name = self.search_term.get()

        available_results = []
        available_cursor = cnt.cursor()
        available = "available"
        search_query = f"SELECT * FROM {available} WHERE Име = ?"
        available_cursor.execute(search_query, (search_name,))
        available_data = available_cursor.fetchall()
        if available_data:
            available_results.append(f"Налични книги:")
            for row in available_data:
                available_results.append(f"\t- {', '.join(row)}")

        taken_results = []
        taken_cursor = cnt.cursor()
        taken = "taken"
        search_query = f"SELECT * FROM {taken} WHERE Име = ?"
        taken_cursor.execute(search_query, (search_name,))
        taken_data = taken_cursor.fetchall()
        if taken_data:
            taken_results.append(f"Заети книги:")
            for row in taken_data:
                taken_results.append(f"\t- {', '.join(row)}")

        search_results = "\n".join(available_results + taken_results)
        self.search_results_label.config(text=search_results)
