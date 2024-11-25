import tkinter as tk
from tkinter import ttk

import sqlite3


# Функция для инициализации базы данных
def init_db():
    conn = sqlite3.connect('business_orders.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            order_details TEXT NOT NULL,
            order_date REAL NOT NULL,
            order_price REAL NOT NULL,
            order_status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()



# Функция для добавления заказа
def add_order():
    conn = sqlite3.connect('business_orders.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO orders (customer_name, order_details, order_date, order_price, order_status)
        VALUES (?, ?, ?, ?, 'Новый заказ')''',
        (customer_name_entry.get(), order_details_entry.get(), order_date_entry.get(), order_price_entry.get()))
    conn.commit()
    conn.close()
    customer_name_entry.delete(0, tk.END) # очистка полей
    order_details_entry.delete(0, tk.END)
    order_date_entry.delete(0, tk.END)
    order_price_entry.delete(0, tk.END)
    view_orders()


# Функция для просмотра заказов в самой таблице
def view_orders():
    for i in tree.get_children():
        tree.delete(i)
    conn = sqlite3.connect('business_orders.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders')
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row) # вывод содержимого таблицы в интерфейсе tkinter (tk.END)
    conn.close()


# Графический интерфейс
app = tk.Tk()
app.title("Система управления заказами")


tk.Label(app, text='Имя клиента').pack()

customer_name_entry = tk.Entry(app)
customer_name_entry.pack()


tk.Label(app, text='Детали заказа').pack()

order_details_entry = tk.Entry(app)
order_details_entry.pack()


order_date_label = tk.Label(app, text='Дата заказа')
order_date_label.pack()

order_date_entry = tk.Entry(app)
order_date_entry.pack()


order_price_label = tk.Label(app, text='Цена заказа')
order_price_label.pack()

order_price_entry = tk.Entry(app)
order_price_entry.pack()


# Кнопка "Добавить заказ"
add_button = tk.Button(app, text='Добавить заказ', command=add_order)
add_button.pack()


# Таблица
columns = ('ID', 'Имя клиента', 'Детали заказа', 'Дата заказа', 'Цена заказа', 'Статус заказа')
tree = ttk.Treeview(app, columns=columns, show='headings')
for column in columns:
    tree.heading(column, text=column)
tree.pack()



init_db()
view_orders()
app.mainloop()


# Вывод содержимого таблицы в терминал
# conn = sqlite3.connect('business_orders.db')
# cursor = conn.cursor()
# cursor.execute('SELECT * FROM orders')
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
# conn.close()


# app.geometry("500x300")
# app.resizable(False, False)