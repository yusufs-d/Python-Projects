import sys
from PyQt5 import QtWidgets
from database import Database


db = Database()

class Mainw(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text_area = QtWidgets.QLabel("")
        self.username_text = QtWidgets.QLabel("Username:")
        self.username = QtWidgets.QLineEdit()
        self.password_text = QtWidgets.QLabel("Password:")
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton("Login")
        self.register = QtWidgets.QPushButton("Register")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.username_text)
        v_box.addWidget(self.username)
        v_box.addWidget(self.password_text)
        v_box.addWidget(self.password)
        v_box.addWidget(self.login)
        v_box.addWidget(self.register)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Login To System")
        self.login.clicked.connect(self.check_infos)
        self.register.clicked.connect(self.reg)
        self.show()

    def check_infos(self):
        u_name = self.username.text()
        pw = self.password.text()
        infos = db.check_login_infos(u_name, pw)
        if len(infos) == 0:
            self.text_area.setText("username or password is incorrect!")
        else:
            self.text_area.setText("welcome " + u_name)

    def reg(self):
        self.reg = Registerw()




class Registerw(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui_2()

    def init_ui_2(self):
        self.count = 0
        self.text_area = QtWidgets.QLabel("")
        self.username_text = QtWidgets.QLabel("Username: ")
        self.register_username = QtWidgets.QLineEdit()
        self.password_text = QtWidgets.QLabel("Password: ")
        self.register_password = QtWidgets.QLineEdit()
        self.password_again_text = QtWidgets.QLabel("Password Again: ")
        self.register_password_again = QtWidgets.QLineEdit()
        self.show_hide_password = QtWidgets.QPushButton("show/hide password")
        self.register_button = QtWidgets.QPushButton("Register")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.username_text)
        v_box.addWidget(self.register_username)
        v_box.addWidget(self.password_text)
        v_box.addWidget(self.register_password)
        v_box.addWidget(self.password_again_text)
        v_box.addWidget(self.register_password_again)
        v_box.addWidget(self.show_hide_password)
        v_box.addWidget(self.register_button)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Register")
        self.show_hide_password.clicked.connect(self.show_hide)
        self.register_button.clicked.connect(self.add_user)
        self.show()

    def show_hide(self):
        if self.count % 2 == 0:
            self.register_password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.register_password_again.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.register_password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.register_password_again.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.count += 1

    def add_user(self):
        u_name = self.register_username.text()
        pw = self.register_password.text()
        pw_again = self.register_password_again.text()
        if pw == pw_again and pw != "" and pw_again != "" and u_name != "":
            db.add_user(u_name, pw)
            self.text_area.setText("Successfully registered!")
        else:
            self.text_area.setText("Registration failed! Check your infos")




app = QtWidgets.QApplication(sys.argv)
w = Mainw()
sys.exit(app.exec_())
