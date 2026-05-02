import sqlite3

def init_db():
    with sqlite3.connect('store.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, price REAL)')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM items")
        if cursor.fetchone()[0] == 0:
            products = [
                ('Audi logo', 20.0),
                ('PC Gaming', 1250.0),
                ('Iphone 17', 699.0),
                ('Keyboard', 150.0),
                ('Gym Equipment', 230.0),
                ('Monitor', 300.0),
                ('Energy Drink', 2.0)
            ]
            conn.executemany("INSERT INTO items (name, price) VALUES (?, ?)", products)

def get_items():
    with sqlite3.connect('store.db') as conn:
        return conn.execute("SELECT * FROM items").fetchall()