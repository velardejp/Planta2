import sqlite3
import datetime
conn = sqlite3.connect('inventarioplanta.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS products(
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    unit TEXT NOT NULL,
    stock REAL NOT NULL DEFAULT 0 CHECK (stock >= 0)
)
''')
c.execute('''
    CREATE TABLE IF NOT EXISTS mezcla(
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    unit TEXT NOT NULL,
    stock REAL NOT NULL DEFAULT 0 CHECK (stock >= 0)
)
''')
c.execute('''
    CREATE TABLE IF NOT EXISTS mezcla_ingrediente (
  mezcla_id TEXT,
  products_id TEXT,
  cantidad REAL,
  FOREIGN KEY(mezcla_id) REFERENCES mezcla(id),
  FOREIGN KEY(products_id) REFERENCES products(id),
  PRIMARY KEY(mezcla_id, products_id)
)
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS entries(
        folio INTEGER PRIMARY KEY AUTOINCREMENT,
        id TEXT,
        product_id TEXT,
        quantity REAL,
        date TEXT,
        FOREIGN KEY(product_id) REFERENCES products(id)
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS exits(
        folio INTEGER PRIMARY KEY AUTOINCREMENT,
        id TEXT,
        product_id TEXT,
        quantity REAL,
        date TEXT,
        mezcla TEXT,
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


def add_product_data(id, name, unit):
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO products (id, name, unit) VALUES (?, ?, ?)", (id, name, unit))
    conn.commit()
    conn.close()
def add_mezcla_ingredient(id_mezcla, id_producto, cantidad):
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO mezcla_ingrediente (mezcla_id, products_id, cantidad) VALUES (?, ?, ?)", (id_mezcla, id_producto, cantidad))
    conn.commit()
    conn.close()
def add_mezcla_data(id, name, unit):
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO mezcla (id, name, unit) VALUES (?, ?, ?)", (id, name, unit))
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    c.execute("SELECT name, id FROM products WHERE id LIKE 'P%'")
    products = c.fetchall()
    conn.close()
    return products
def get_all_mezclas():
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    c.execute("SELECT name, id FROM mezcla WHERE id LIKE 'M%'")
    mezclas = c.fetchall()
    conn.close()
    return mezclas

def add_entry(id, product_name, quantity):
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    entry_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO entries (id, product_id, quantity, date) VALUES (?, ?, ?, ?)",
              (id, product_name, quantity, entry_date))
    c.execute("UPDATE products SET stock = stock + ? WHERE name = ?",(quantity, product_name))
    conn.commit()
    conn.close()

def add_exit(id, product_name, quantity_out, mezcla):

    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    exit_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO exits (id, product_id, quantity, date, mezcla) VALUES (?, ?, ?, ?, ?)",
              (id, product_name, quantity_out, exit_date, mezcla))
    # Obtiene la cantidad actual en stock
    c.execute("UPDATE products SET stock = stock - ? WHERE name = ?", (float(quantity_out), product_name))
    conn.commit()
    conn.close()


def make_id_prod():
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    c.execute("SELECT id FROM products WHERE id LIKE 'P%' ORDER BY id DESC LIMIT 1")
    ultimo = c.fetchone()
    if ultimo is not None:
        cadena = ultimo[0][1:]  
        numero = int(cadena) + 1
        id = "P" + str(numero)
    else:
        id = "P10001"  
    conn.commit()
    conn.close()
    return id

def make_mezcla_prod():
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    c.execute("SELECT id FROM products WHERE id LIKE 'M%' ORDER BY id DESC LIMIT 1")
    ultimo = c.fetchone()
    if ultimo is not None:
        cadena = ultimo[0][1:]  
        numero = int(cadena) + 1
        id = "M" + str(numero)
    else:
        id = "M10001"  
    conn.commit()
    conn.close()
    return id

def make_id_entry():
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    c.execute("SELECT id FROM entries ORDER BY id DESC LIMIT 1")
    ultimo = c.fetchone()
    if ultimo is not None:
        cadena = ultimo[0][1:]  
        numero = int(cadena)  # Asegurándose de que la cadena se convierte en un número entero
        numero += 1
        id = "E" + str(numero)
    else:
        id = "E10001"  
    conn.commit()
    conn.close()
    return id

def make_id_exit():
    conn = sqlite3.connect('inventarioplanta.db')
    c = conn.cursor()
    c.execute("SELECT id FROM exits ORDER BY id DESC LIMIT 1")
    ultimo = c.fetchone()
    if ultimo is not None:
        cadena = ultimo[0][1:]  
        numero = int(cadena) + 1
        id = "S" + str(numero)
    else:
        id = "S10001"  
    conn.commit()
    conn.close()
    return id