import sqlite3
import datetime
conn = sqlite3.connect('inventarioplanta.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        unit TEXT NOT NULL,
        stock REAL NO NULL DEFAULT 0
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS mezclas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        unit TEXT NOT NULL,
        stock REAL NO NULL DEFAULT 0
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS entries(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        quantity REAL,
        date TEXT,
        FOREIGN KEY(product_id) REFERENCES products(id)
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS exits(
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        quantity REAL,
        date TEXT,
        FOREIGN KEY(product_id) REFERENCES products(id)
    )
''')
conn.commit()
conn.close()

def get_product_id(product_name):
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    c.execute("SELECT id FROM products WHERE name = ?", (product_name,))
    product_id = c.fetchone()
    conn.close()
    if product_id is not None:
        return product_id[0]
    else:
        return None


def add_product_data(name, unit):
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO products (name, unit) VALUES (?, ?)", (name, unit))
    conn.commit()
    conn.close()
def add_mezcla_data(name):
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO mezclas (name, unit) VALUES (?, ?)", (name, "Kilogramos"))
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    c.execute("SELECT name FROM products")
    products = c.fetchall()
    conn.close()
    return products
def get_all_mezclas():
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    c.execute("SELECT name FROM mezclas")
    mezclas = c.fetchall()
    conn.close()
    return mezclas

def add_entry(product_name, quantity):
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    entry_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO entries (product_id, quantity, date) VALUES (?, ?, ?)",
              (product_name, quantity, entry_date))
    c.execute("UPDATE products SET stock = stock + ? WHERE name = ?",(quantity, product_name))
    conn.commit()
    conn.close()


def add_exit(product_name, quantity_out):
    product_id = get_product_id(product_name)
    if product_id is None:
        # Manejar el caso en que el producto no se encuentra en la base de datos
        return

    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    exit_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO exits (product_id, quantity, date) VALUES (?, ?, ?)",
              (product_id, quantity_out, exit_date))
        # Obtiene la cantidad actual en stock
    c.execute("UPDATE products SET stock = stock - ? WHERE id = ?", (float(quantity_out), product_id))
    conn.commit()
    conn.close()




