import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

cnt = sqlite3.connect("inventar.db")


def create_database_and_table():
    cursor = cnt.cursor()
    available = """
    CREATE TABLE IF NOT EXISTS available (
    kniga_ime_entry TEXT,
    kniga_avtor_entry TEXT,
    data_vpisvane_entry TEXT,
    inventar_num_entry TEXT,
    signatura_entry TEXT,
    bg_avtor_entry TEXT,
    chujd_avtor_entry TEXT)
    """
    taken = """
    CREATE TABLE IF NOT EXISTS taken (
    kniga_ime_entry TEXT,
    kniga_avtor_entry TEXT,
    data_vpisvane_entry TEXT,
    inventar_num_entry TEXT,
    signatura_entry TEXT,
    bg_avtor_entry TEXT,
    chujd_avtor_entry TEXT)
    """
    cursor.execute(available)
    cursor.execute(taken)
    cnt.commit()


def run_app():
    root = tk.Tk()
    app = LibraryManagementGUI(root)
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

        self.label3 = tk.Label(master, text="Дата на вписване:", font=font)
        self.label3.grid(row=4, column=0, sticky="w")

        self.vpisvane = tk.StringVar()
        self.data_vpisvane_entry = tk.Entry(master, textvariable=self.vpisvane, font=font)
        self.data_vpisvane_entry.grid(row=4, column=1, sticky="ew")

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
        self.nalichni_knigi = tk.StringVar()
        self.nalichni_knigi = tk.Entry(master, textvariable=self.chujdavtor, font=font)
        self.nalichni_knigi.grid(row=14, column=1, sticky="ew")

        self.add_button = tk.Button(
            master, text="Добавяне на книга", command=self.add_book, font=font
        )
        self.add_button.grid(row=16, column=0, sticky="ew")

        self.view_button = tk.Button(
            master, text="Инвентар", command=self.view_invent, font=font
        )
        self.view_button.grid(row=16, column=1, columnspan=2, sticky="ew")

        self.view_button = tk.Button(
            master, text="Отдаване на книга", command=self.loan_book, font=font
        )
        self.view_button.grid(row=16, column=2, columnspan=2, sticky="ew")

        self.view_button = tk.Button(
            master, text="Взети книги", command=self.view_loans, font=font
        )
        self.view_button.grid(row=18, column=0, columnspan=2, sticky="ew")

        self.view_button = tk.Button(
            master, text="Връщане на книга", command=self.return_book, font=font
        )
        self.view_button.grid(row=18, column=2, columnspan=2, sticky="ew")

        master.grid_columnconfigure(1, weight=1)

    def add_book(self):
        data = [(self.ime.get(),
                 self.avtor.get(),
                 self.vpisvane.get(),
                 self.invent_num.get(),
                 self.signat.get(),
                 self.bgavtor.get(),
                 self.chujdavtor.get())]
        insert_query_multiple = """
        INSERT INTO available (
        kniga_ime_entry,
        kniga_avtor_entry,
        data_vpisvane_entry,
        inventar_num_entry,
        signatura_entry,
        bg_avtor_entry,
        chujd_avtor_entry,
        nalichni_knigi) 

        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        cur = cnt.cursor()
        cur.execute(insert_query_multiple, *data)
        cnt.commit()

    def loan_book(self):
        cur = cnt.cursor()
        table_name = "available"
        table_name_taken = "taken"

        search_value = [(self.ime.get(),
                         self.avtor.get(),
                         self.vpisvane.get(),
                         self.invent_num.get(),
                         self.signat.get(),
                         self.bgavtor.get(),
                         self.chujdavtor.get())]

        column_names = ["kniga_ime_entry",
                        "kniga_avtor_entry",
                        "data_vpisvane_entry",
                        "inventar_num_entry",
                        "signatura_entry",
                        "bg_avtor_entry",
                        "chujd_avtor_entry",
                        "nalichni_knigi"]

        conditions = []

        for i, value in enumerate(search_value):
            column = column_names[i]
            conditions.append(f"{column} = ?")

            where_clause = " AND ".join(conditions)

            query = f"SELECT * FROM {table_name} WHERE {where_clause}"

            cur.execute(query, search_value)

            row = cur.fetchone()
            if row:
                insert_query = f"""
                            INSERT INTO {table_name_taken} ({", ".join(column_names)})
                            VALUES (?, ?, ?)
                            """
                cur.execute(insert_query, row)

                delete_query = f"""
                            DELETE FROM {table_name} WHERE {column_names[0]} = ?
                            """
                cur.execute(delete_query, (row[0],))
                break
        cnt.commit()

    def get_column_names(self):
        return ["kniga_ime_entry",
                "kniga_avtor_entry",
                "data_vpisvane_entry",
                "inventar_num_entry",
                "signatura_entry",
                "bg_avtor_entry",
                "chujd_avtor_entry",
                "nalichni_knigi"]

    def view_invent(self):
        table_window = tk.Toplevel(self.master)
        table_window.title("Инвентарна книга")

        table = ttk.Treeview(table_window, columns=self.get_column_names() + ["Count"])
        table.heading("#0", text="ID")

        for idx, column in enumerate(self.get_column_names()):
            table.heading(column, text=column)

        table.heading("Count", text="Брой")

        table.grid(row=0, column=0)

        cur = cnt.cursor()
        table_name = "available"

        count_query = f"""
            SELECT kniga_ime_entry, COUNT(*) AS book_count
            FROM {table_name}
            GROUP BY kniga_ime_entry
            """
        cur.execute(count_query)

        book_counts = dict(cur.fetchall())

        query = f"SELECT * FROM {table_name}"
        cur.execute(query)
        all_rows = cur.fetchall()

        for idx, row in enumerate(all_rows):
            book_title = row[0]
            count = book_counts.get(book_title, 0)

            table.insert("", tk.END, values=(idx + 1,) + row + (count,))

        nalichni_table = "nalichni_knigi"
        update_query = f"""
            UPDATE {nalichni_table}
            SET nalichni_knigi = ?
            WHERE kniga_ime = ?
            """

        for book_title, count in book_counts.items():
            cur.execute(f"SELECT nalichni_knigi FROM {nalichni_table} WHERE kniga_ime = ?", (book_title,))
            existing_count = cur.fetchone()

            if existing_count and existing_count[0] != count:
                cur.execute(update_query, (count, book_title))

        cnt.commit()

        table_window.mainloop()

    def view_loans(self):
        table_window = tk.Toplevel(self.master)
        table_window.title("Инвентарна книга")

        table = ttk.Treeview(table_window, columns=self.get_column_names() + ["Count"])
        table.heading("#0", text="ID")

        for idx, column in enumerate(self.get_column_names()):
            table.heading(column, text=column)

        table.heading("Count", text="Брой")

        table.grid(row=0, column=0)

        cur = cnt.cursor()
        table_name = "available"

        count_query = f"""
                    SELECT kniga_ime_entry, COUNT(*) AS book_count
                    FROM {table_name}
                    GROUP BY kniga_ime_entry
                    """
        cur.execute(count_query)

        book_counts = dict(cur.fetchall())

        query = f"SELECT * FROM {table_name}"
        cur.execute(query)
        all_rows = cur.fetchall()

        for idx, row in enumerate(all_rows):
            book_title = row[0]
            count = book_counts.get(book_title, 0)

            table.insert("", tk.END, values=(idx + 1,) + row + (count,))

        nalichni_table = "nalichni_knigi"
        update_query = f"""
                    UPDATE {nalichni_table}
                    SET nalichni_knigi = ?
                    WHERE kniga_ime = ?
                    """

        for book_title, count in book_counts.items():
            cur.execute(f"SELECT nalichni_knigi FROM {nalichni_table} WHERE kniga_ime = ?", (book_title,))
            existing_count = cur.fetchone()

            if existing_count and existing_count[0] != count:
                cur.execute(update_query, (count, book_title))

        cnt.commit()

        table_window.mainloop()

    def return_book(self):
        cur = cnt.cursor()
        table_name = "taken"
        table_name_taken = "available"

        search_value = [(self.ime.get(),
                         self.avtor.get(),
                         self.vpisvane.get(),
                         self.invent_num.get(),
                         self.signat.get(),
                         self.bgavtor.get(),
                         self.chujdavtor.get())]

        column_names = ["kniga_ime_entry",
                        "kniga_avtor_entry",
                        "data_vpisvane_entry",
                        "inventar_num_entry",
                        "signatura_entry",
                        "bg_avtor_entry",
                        "chujd_avtor_entry"]

        conditions = []

        for i, value in enumerate(search_value):
            column = column_names[i]
            conditions.append(f"{column} = ?")

            where_clause = " AND ".join(conditions)

            query = f"SELECT * FROM {table_name} WHERE {where_clause}"

            cur.execute(query, search_value)

            row = cur.fetchone()
            if row:
                insert_query = f"""
                                    INSERT INTO {table_name_taken} ({", ".join(column_names)})
                                    VALUES (?, ?, ?)
                                """
                cur.execute(insert_query, row)

                # Construct DELETE query for 'available' table
                delete_query = f"""
                                    DELETE FROM {table_name} WHERE {column_names[0]} = ?
                                """
                cur.execute(delete_query, (row[0],))
                break
        cnt.commit()
