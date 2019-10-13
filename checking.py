import sys
from PyQt5.QtWidgets import QApplication, QWidget
from main import Ui_MainWindow


class Calc(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.PLUS.clicked.connect(self.summ)
        self.MINUS.clicked.connect(self.diff)
        self.MULT.clicked.connect(self.mult)
        self.DIV.clicked.connect(self.div)
        self.INT_DIV.clicked.connect(self.int_div)
        self.MOD.clicked.connect(self.mod)

    def summ(self):
        self.answer.setText(str(float(self.first_num.text()) + float(self.second_num.text())))
    
    def diff(self):
        self.answer.setText(str(float(self.first_num.text()) - float(self.second_num.text())))
        
    def mult(self):
        self.answer.setText(str(float(self.first_num.text()) * float(self.second_num.text())))
        
    def div(self):
        if float(self.second_num.text()):
            self.answer.setText(str(float(self.first_num.text()) / float(self.second_num.text())))
        else:
            self.answer.setText("ERROR. DIVIZION BY ZERO ! ! !")

    def int_div(self):
        if float(self.second_num.text()):
            self.answer.setText(str(float(self.first_num.text()) // float(self.second_num.text())))
        else:
            self.answer.setText("ERROR. DIVIZION BY ZERO ! ! !")

    def mod(self):
        if float(self.second_num.text()):
            self.answer.setText(str(float(self.first_num.text()) % float(self.second_num.text())))
        else:
            self.answer.setText("ERROR. DIVIZION BY ZERO ! ! !")
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calc()
    ex.show()
    sys.exit(app.exec())