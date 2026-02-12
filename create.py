import sqlite3

def create_tables(conn):
    cur = conn.cursor()
    # ΚΑΤΑΣΤΗΜΑΤΑ
    cur.execute("CREATE TABLE IF NOT EXISTS stores (id INTEGER PRIMARY KEY, name TEXT, address TEXT, city TEXT, operating_hours TEXT, phone TEXT)")
    # ΠΩΛΗΤΕΣ
    cur.execute("CREATE TABLE IF NOT EXISTS salespeople (id INTEGER PRIMARY KEY, full_name TEXT, address TEXT, city TEXT, phone TEXT, email TEXT, commission_rate REAL, total_commission REAL, store_id INTEGER, FOREIGN KEY(store_id) REFERENCES stores(id))")
    # ΠΕΛΑΤΕΣ
    cur.execute("CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, full_name TEXT, address TEXT, city TEXT, phone TEXT, email TEXT, current_balance REAL, salesperson_id INTEGER, FOREIGN KEY(salesperson_id) REFERENCES salespeople(id))")
    # ΠΡΟΪΟΝΤΑ
    cur.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, description TEXT, sales_price REAL, wholesale_cost REAL, category TEXT, stock_quantity INTEGER, color TEXT, prod_size TEXT, store_id INTEGER, FOREIGN KEY(store_id) REFERENCES stores(id))")
    # ΟΜΑΔΕΣ
    cur.execute("CREATE TABLE IF NOT EXISTS teams (id INTEGER PRIMARY KEY, name TEXT, number_of_players INTEGER, discount_rate REAL, city TEXT, representative_customer_id INTEGER UNIQUE, FOREIGN KEY(representative_customer_id) REFERENCES customers(id))")
    # ΠΑΡΑΓΓΕΛΙΕΣ
    cur.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, order_date TEXT, status TEXT, total_amount REAL, customer_id INTEGER, FOREIGN KEY(customer_id) REFERENCES customers(id))")
    # ΠΡΟΪΟΝΤΑ ΠΑΡΑΓΓΕΛΙΑΣ
    cur.execute("CREATE TABLE IF NOT EXISTS order_items (order_id INTEGER, product_id INTEGER, quantity INTEGER, unit_price REAL, prod_size TEXT, color TEXT, PRIMARY KEY (order_id, product_id))")
    conn.commit()
