import sqlite3

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
