import sqlite3
import datetime
conn = sqlite3.connect('inventarioplanta.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        unit TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS entries(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        quantity INTEGER,
        date TEXT,
        FOREIGN KEY(product_id) REFERENCES products(id)
    )
''')
conn.commit()
conn.close()



def add_product_data(name, unit):
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    c.execute("INSERT INTO products (name, unit) VALUES (?, ?)", (name, unit))
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    c.execute("SELECT name FROM products")
    products = c.fetchall()
    conn.close()
    return products

def add_entry(product_name, quantity):
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    entry_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO entries (product_id, quantity, date) VALUES (?, ?, ?)",
              (product_name, quantity, entry_date))
    conn.commit()
    conn.close()
