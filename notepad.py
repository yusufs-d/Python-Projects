import os
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, \
     QVBoxLayout, QHBoxLayout, QFileDialog,QMainWindow,QAction


class NotePad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text_area = QTextEdit()
        self.clear_button = QPushButton("Clear")
        self.open_button = QPushButton("Open")
        self.save_button = QPushButton("Save")


        h_box = QHBoxLayout()
        h_box.addWidget(self.clear_button)
        h_box.addWidget(self.open_button)
        h_box.addWidget(self.save_button)

        v_box = QVBoxLayout()
        v_box.addWidget(self.text_area)
        v_box.addLayout(h_box)


        self.setLayout(v_box)
        self.setWindowTitle("NotePad")
        self.clear_button.clicked.connect(self.clear_text_area)
        self.open_button.clicked.connect(self.open_file)
        self.save_button.clicked.connect(self.save_text_area)
        self.show()
    def clear_text_area(self):
        self.text_area.clear()
    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self,"Open File",os.getenv("Desktop"))
        with open(file_name[0],"r") as file:
            self.text_area.setText(file.read())
    def save_text_area(self):
        file_name = QFileDialog.getSaveFileName(self,"Save File",os.getenv("Desktop"))
        with open(file_name[0],"w") as file:
            file.write(self.text_area.toPlainText())


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.notepad = NotePad()
        self.setCentralWidget(self.notepad)

        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")

        open_f = QAction("Open File...", self)
        open_f.setShortcut("Ctrl+O")
        save_f = QAction("Save As...", self)
        save_f.setShortcut("Ctrl+S")
        quit_f = QAction("Quit", self)
        quit_f.setShortcut("Ctrl+Q")

        cl = QAction("Clear",self)
        cl.setShortcut("Ctrl+Shift+C")


        file.addAction(open_f)
        file.addAction(save_f)
        file.addAction(quit_f)

        edit.addAction(cl)

        menubar.setNativeMenuBar(False)
        self.setWindowTitle("NotePad")
        file.triggered.connect(self.response)
        edit.triggered.connect(self.response_2)
        self.show()

    def response(self,action):
        if action.text() == "Open File...":
            self.notepad.open_file()
        elif action.text() == "Save As...":
            self.notepad.save_text_area()
        elif action.text() == "Quit":
            quit()

    def response_2(self,action):
        if action.text() == "Clear":
            self.notepad.clear_text_area()











app = QApplication(sys.argv)
m = Menu()
sys.exit(app.exec_())




