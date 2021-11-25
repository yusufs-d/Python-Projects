import sys
import time

from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout \
    , QApplication, QPushButton, QLineEdit, QLabel
from PyQt5 import QtGui
from market import Database, Product

db = Database()
p = Product()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.refresh_items()

    def init_ui(self):
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setRowCount(len(p.all_items()))
        self.table.setFixedSize(317, 50 * len(p.all_items()))
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem("Product Name"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Product Type"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Stock"))
        self.add_item_button = QPushButton("Add Product")
        self.delete_item_button = QPushButton("Delete Product")
        self.change_stock_button = QPushButton("Change Stock Of A Product")

        h_box = QHBoxLayout()
        h_box.addWidget(self.add_item_button)
        h_box.addWidget(self.delete_item_button)
        h_box.addWidget(self.change_stock_button)

        v_box = QVBoxLayout()
        v_box.addWidget(self.table)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.add_item_button.clicked.connect(self.add_item)
        self.delete_item_button.clicked.connect(self.delete_item)
        self.change_stock_button.clicked.connect(self.change_stock)
        self.show()

    def refresh_items(self):
        a = 0
        for i in p.all_items():
            self.table.setItem(a, 0, QTableWidgetItem(i[0]))
            self.table.setItem(a, 1, QTableWidgetItem(i[1]))
            self.table.setItem(a, 2, QTableWidgetItem(str(i[2])))
            a += 1

    def add_item(self):
        self.add = AddItem()

    def delete_item(self):
        self.d = DeleteItem()
        self.update()

    def change_stock(self):
        self.c = ChangeStock()


class AddItem(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.item_name_label = QLabel("Product Name:")
        self.item_name = QLineEdit()
        self.item_type_label = QLabel("Product Type:")
        self.item_type = QLineEdit()
        self.stock_label = QLabel("Stock:")
        self.stock = QLineEdit()
        self.add_button = QPushButton("Add")

        h_box_1 = QHBoxLayout()
        h_box_2 = QHBoxLayout()
        h_box_3 = QHBoxLayout()
        h_box_4 = QHBoxLayout()
        h_box_1.addWidget(self.item_name_label)
        h_box_1.addWidget(self.item_name)
        h_box_2.addWidget(self.item_type_label)
        h_box_2.addWidget(self.item_type)
        h_box_3.addWidget(self.stock_label)
        h_box_3.addWidget(self.stock)
        h_box_4.addWidget(self.add_button)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box_1)
        v_box.addLayout(h_box_2)
        v_box.addLayout(h_box_3)
        v_box.addLayout(h_box_4)

        self.setWindowTitle("Add Product")
        self.setLayout(v_box)
        self.add_button.clicked.connect(self.add_product)
        self.show()

    def add_product(self):
        name = self.item_name.text()
        typ = self.item_type.text()
        st = self.stock.text()
        p.add_item(name, typ, st)
        self.close()


class DeleteItem(QWidget):
    def __init__(self):
        super().__init__()
        self.user_ui()

    def user_ui(self):
        self.item_name_label = QLabel("Product Name:")
        self.item_name = QLineEdit()
        self.delete_button = QPushButton("Delete")

        h_box = QHBoxLayout()
        h_box.addWidget(self.item_name_label)
        h_box.addWidget(self.item_name)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addWidget(self.delete_button)

        self.setLayout(v_box)
        self.setWindowTitle("Delete Product")
        self.delete_button.clicked.connect(self.delete)
        self.show()

    def delete(self):
        p.delete_item(self.item_name.text())
        self.close()


class ChangeStock(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.item_name_label = QLabel("Product Name:")
        self.item_name = QLineEdit()
        self.new_stock_label = QLabel("New Stock:")
        self.new_stock = QLineEdit()
        self.change_button = QPushButton("Change")

        h_box_1 = QHBoxLayout()
        h_box_2 = QHBoxLayout()
        h_box_1.addWidget(self.item_name_label)
        h_box_1.addWidget(self.item_name)
        h_box_2.addWidget(self.new_stock_label)
        h_box_2.addWidget(self.new_stock)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box_1)
        v_box.addLayout(h_box_2)
        v_box.addWidget(self.change_button)

        self.setLayout(v_box)
        self.setWindowTitle("Change Stock Of A Product")
        self.change_button.clicked.connect(self.change)
        self.show()

    def change(self):
        p.change_stock(self.new_stock.text(), self.item_name.text())
        self.close()

app = QApplication(sys.argv)

w = Window()
sys.exit(app.exec_())
