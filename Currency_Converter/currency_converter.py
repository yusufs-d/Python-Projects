import sys
import requests
from PyQt5 import QtWidgets,QtGui
from Currency_Converter.currency_acronyms import cur_a



url = "http://data.fixer.io/api/latest?access_key=a8548104ef96b189992956a31208ca52"
request = requests.get(url)
json = request.json()

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setFixedSize(700,300)
    def init_ui(self):
        self.cb = QtWidgets.QComboBox()
        for i in cur_a:
            self.cb.addItem(i)
        self.amount_label = QtWidgets.QLabel("Amount")
        self.amount = QtWidgets.QLineEdit()
        self.frm_label = QtWidgets.QLabel("From")
        self.frm = QtWidgets.QComboBox()
        for i in cur_a:
            self.frm.addItem(i)
        self.to_label = QtWidgets.QLabel("To")
        self.to = QtWidgets.QComboBox()
        for i in cur_a:
            self.to.addItem(i)
        self.calculate_button = QtWidgets.QPushButton("Calculate")
        self.result = QtWidgets.QLabel("")
        self.change_button = QtWidgets.QPushButton()
        self.change_button.setFixedSize(16,16)
        self.change_button.setIcon(QtGui.QIcon("change_icon.ico"))


        h_box_1 = QtWidgets.QHBoxLayout()
        h_box_2 = QtWidgets.QHBoxLayout()
        h_box_1.addWidget(self.amount_label)
        h_box_1.addWidget(self.frm_label)
        h_box_1.addWidget(self.to_label)
        h_box_2.addWidget(self.amount)
        h_box_2.addWidget(self.frm)
        h_box_2.addWidget(self.change_button)
        h_box_2.addWidget(self.to)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box_1)
        v_box.addLayout(h_box_2)
        v_box.addWidget(self.calculate_button)
        v_box.addWidget(self.result)
        v_box.addStretch()

        self.setLayout(v_box)
        self.setWindowTitle("Currency Converter")
        self.change_button.clicked.connect(self.chn)
        self.calculate_button.clicked.connect(self.calc)
        self.show()

    def chn(self):
        f = self.frm.currentText()
        t = self.to.currentText()
        self.frm.setCurrentText(t)
        self.to.setCurrentText(f)


    def calc(self):
        try:
            a = self.amount.text()
            f = self.frm.currentText()
            t = self.to.currentText()
            value_1 = json["rates"][cur_a[f]]
            value_2 = json["rates"][cur_a[t]]
            result = (value_2/value_1)*int(a)
            self.result.setText("{} {} = {} {}".format(a,f,result,t))
        except ValueError:
            self.result.setText("Please enter all information correctly !")




app = QtWidgets.QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())

