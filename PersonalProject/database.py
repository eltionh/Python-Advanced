import sqlite3


def init_db():
    """Creates the tables and seeds inventory if empty."""
    with sqlite3.connect('store.db') as conn:
        # Create items table
        conn.execute('''CREATE TABLE IF NOT EXISTS items
                        (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            price REAL
                        )''')

        # Create users table for Registration/Authentication
        conn.execute('''CREATE TABLE IF NOT EXISTS users
                        (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE,
                            password TEXT,
                            role TEXT
                        )''')

        # Seed initial inventory
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM items")
        if cursor.fetchone()[0] == 0:
            products = [
                ('Audi logo', 20.0), ('PC Gaming', 1250.0), ('Iphone 17', 699.0),
                ('Keyboard', 150.0), ('Gym Equipment', 230.0), ('Monitor', 300.0),
                ('Energy Drink', 2.0)
            ]
            conn.executemany("INSERT INTO items (name, price) VALUES (?, ?)", products)

        # Seed a default admin account if it doesn't exist
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = 'admin'")
        if cursor.fetchone()[0] == 0:
            conn.execute(
                "INSERT INTO users (username, password, role) VALUES ('admin', 'admin123', 'admin')"
            )

        conn.commit()


def register_user(username, password):
    try:
        with sqlite3.connect('store.db') as conn:
            conn.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, 'user')",
                (username, password)
            )
        return True
    except sqlite3.IntegrityError:
        return False  # Username already taken


def verify_user(username, password):
    """Checks credentials and returns the user's role if valid."""
    with sqlite3.connect('store.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT role FROM users WHERE username = ? AND password = ?",
            (username, password)
        )
        result = cursor.fetchone()
        return result[0] if result else None


def get_all_users():
    """Admin function to view registered users."""
    with sqlite3.connect('store.db') as conn:
        return conn.execute("SELECT id, username, role FROM users").fetchall()


def get_items():
    """Fetch all items from inventory."""
    with sqlite3.connect('store.db') as conn:
        return conn.execute("SELECT * FROM items").fetchall()


def update_item_price(item_id, new_price):
    with sqlite3.connect('store.db') as conn:
        conn.execute("UPDATE items SET price = ? WHERE id = ?", (new_price, item_id))


def delete_item(item_id):
    with sqlite3.connect('store.db') as conn:
        conn.execute("DELETE FROM items WHERE id = ?", (item_id,))


def add_new_item(name, price):
    with sqlite3.connect('store.db') as conn:
        conn.execute("INSERT INTO items (name, price) VALUES (?, ?)", (name, price))
