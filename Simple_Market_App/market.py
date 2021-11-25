import sqlite3


class Database:
    def __init__(self):
        self.create_database()
        self.create_table()

    def create_database(self):
        self.connection = sqlite3.connect("market.db")
        self.cursor = self.connection.cursor()

    def create_table(self):
        query = "Create table if not exists products (Product_Name TEXT, Product_Type TEXT, Stock INT)"
        self.cursor.execute(query)
        self.connection.commit()


class Product:
    def __init__(self):
        self.database = Database()

    def all_items(self):
        q = "select * from products"
        self.database.cursor.execute(q)
        self.items = self.database.cursor.fetchall()
        return self.items

    def add_item(self, p_name, p_type, st):
        q = "insert into products values (?,?,?)"
        self.database.cursor.execute(q, (p_name, p_type, st))
        self.database.connection.commit()

    def delete_item(self, p_name):
        q = "Delete from products where Product_Name = ?"
        self.database.cursor.execute(q, (p_name,))
        self.database.connection.commit()

    def change_stock(self,stock,p_name):
        q = "Update products set Stock = ? where Product_Name = ?"
        self.database.cursor.execute(q, (stock,p_name))
        self.database.connection.commit()

