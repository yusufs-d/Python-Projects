from PyQt5 import QtWidgets
import sys
# This calculator only supports two-number operations.

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,300)
        self.init_ui()
        self.operations = list()

    def init_ui(self):
        self.text_area = QtWidgets.QLineEdit()
        self.one = QtWidgets.QPushButton("1")
        self.two = QtWidgets.QPushButton("2")
        self.three = QtWidgets.QPushButton("3")
        self.four = QtWidgets.QPushButton("4")
        self.five = QtWidgets.QPushButton("5")
        self.six = QtWidgets.QPushButton("6")
        self.seven = QtWidgets.QPushButton("7")
        self.eight = QtWidgets.QPushButton("8")
        self.nine = QtWidgets.QPushButton("9")
        self.zero = QtWidgets.QPushButton("0")
        self.point = QtWidgets.QPushButton(".")
        self.plus = QtWidgets.QPushButton("+")
        self.minus = QtWidgets.QPushButton("-")
        self.mult = QtWidgets.QPushButton("*")
        self.divis = QtWidgets.QPushButton("/")
        self.equal = QtWidgets.QPushButton("=")
        self.clear = QtWidgets.QPushButton("C")
        self.text_area.setFixedSize(370,35)
        self.one.setFixedSize(120,50)
        self.two.setFixedSize(120, 50)
        self.three.setFixedSize(120, 50)
        self.four.setFixedSize(120, 50)
        self.five.setFixedSize(120, 50)
        self.six.setFixedSize(120, 50)
        self.seven.setFixedSize(120, 50)
        self.eight.setFixedSize(120, 50)
        self.nine.setFixedSize(120, 50)
        self.zero.setFixedSize(180, 50)
        self.point.setFixedSize(180,50)
        self.plus.setFixedSize(60, 50)
        self.minus.setFixedSize(60, 50)
        self.mult.setFixedSize(60, 50)
        self.divis.setFixedSize(60, 50)
        self.equal.setFixedSize(60, 50)
        self.clear.setFixedSize(60,50)


        h_box_1 = QtWidgets.QHBoxLayout()
        h_box_2 = QtWidgets.QHBoxLayout()
        h_box_3 = QtWidgets.QHBoxLayout()
        h_box_4 = QtWidgets.QHBoxLayout()
        h_box_5 = QtWidgets.QHBoxLayout()
        h_box_1.addWidget(self.one)
        h_box_1.addWidget(self.two)
        h_box_1.addWidget(self.three)
        h_box_2.addWidget(self.four)
        h_box_2.addWidget(self.five)
        h_box_2.addWidget(self.six)
        h_box_3.addWidget(self.seven)
        h_box_3.addWidget(self.eight)
        h_box_3.addWidget(self.nine)
        h_box_4.addWidget(self.zero)
        h_box_4.addWidget(self.point)
        h_box_5.addWidget(self.plus)
        h_box_5.addWidget(self.minus)
        h_box_5.addWidget(self.mult)
        h_box_5.addWidget(self.divis)
        h_box_5.addWidget(self.equal)
        h_box_5.addWidget(self.clear)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.text_area)
        v_box.addLayout(h_box_1)
        v_box.addLayout(h_box_2)
        v_box.addLayout(h_box_3)
        v_box.addLayout(h_box_4)
        v_box.addLayout(h_box_5)
        v_box.addStretch()

        self.setLayout(v_box)
        self.setWindowTitle("Calculator")
        self.one.clicked.connect(lambda: self.display_number(self.one.text()))
        self.two.clicked.connect(lambda : self.display_number(self.two.text()))
        self.three.clicked.connect(lambda: self.display_number(self.three.text()))
        self.four.clicked.connect(lambda: self.display_number(self.four.text()))
        self.five.clicked.connect(lambda: self.display_number(self.five.text()))
        self.six.clicked.connect(lambda: self.display_number(self.six.text()))
        self.seven.clicked.connect(lambda: self.display_number(self.seven.text()))
        self.eight.clicked.connect(lambda: self.display_number(self.eight.text()))
        self.nine.clicked.connect(lambda: self.display_number(self.nine.text()))
        self.zero.clicked.connect(lambda: self.display_number(self.zero.text()))
        self.point.clicked.connect(lambda: self.display_number(self.point.text()))
        self.plus.clicked.connect(lambda: self.display_number(self.plus.text()))
        self.minus.clicked.connect(lambda: self.display_number(self.minus.text()))
        self.mult.clicked.connect(lambda: self.display_number(self.mult.text()))
        self.divis.clicked.connect(lambda: self.display_number(self.divis.text()))
        self.clear.clicked.connect(self.clear_text_area)
        self.equal.clicked.connect(self.calculate)


        self.show()

    def display_number(self,number):
        if number == "+" or number == "-" or number == "*" or number == "/":
            self.operations.append(number)
        pre_text = self.text_area.text()
        if self.text_area.text() == "":
            self.text_area.setText(number)
        else:
            self.text_area.setText(pre_text+number)


    def calculate(self):
        try:
            operation = self.operations[0]
            text = self.text_area.text()
            text = text.split(operation)
            if operation == "+":
                s = 0
                for i in text:
                    s += float(i)
                self.text_area.setText(str(s))
            elif operation == "-":
                result = float(text[0])-float(text[1])
                self.text_area.setText(str(result))
            elif operation == "*":
                m = 1
                for i in text:
                    m *= float(i)
                self.text_area.setText(str(m))
            elif operation == "/":
                try:
                    result = float(text[0])/float(text[1])
                    self.text_area.setText(str(result))
                except ZeroDivisionError:
                    self.text_area.setText("ZeroDivisionError!")
        except:
            self.text_area.setText("Syntax Error!")

    def clear_text_area(self):
        self.text_area.clear()


app = QtWidgets.QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())

