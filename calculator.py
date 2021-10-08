import math 
import PySide6

from PySide6.QtWidgets import *
from functools import partial
from PySide6.QtUiTools import *
from PySide6.QtCore import *



class HelloWorld(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()

        self.ui = loader.load('new.ui', None)
        self.ui.show()
  
        

        self.ui.btn_1.clicked.connect(partial(self.num,'1'))
        self.ui.btn_2.clicked.connect(partial(self.num,'2'))
        self.ui.btn_3.clicked.connect(partial(self.num,'3'))
        self.ui.btn_4.clicked.connect(partial(self.num,'4'))
        self.ui.btn_5.clicked.connect(partial(self.num,'5'))
        self.ui.btn_6.clicked.connect(partial(self.num,'6'))
        self.ui.btn_7.clicked.connect(partial(self.num,'7'))
        self.ui.btn_8.clicked.connect(partial(self.num,'8'))
        self.ui.btn_9.clicked.connect(partial(self.num,'9'))
        self.ui.btn_0.clicked.connect(partial(self.num,'0'))

    def num(self, x):
        self.ui.textbox.setText(self.ui.textbox.text()+ x)



    
        self.ui.btn_sum.clicked.connect(self.numsum)
        self.ui.btn_min.clicked.connect(self.nummin)
        self.ui.btn_equal.clicked.connect(self.numeq)
        self.ui.btn_mul.clicked.connect(self.nummul)
        self.ui.btn_div.clicked.connect(self.numdiv)
        self.ui.btn_dot.clicked.connect(self.numdot)
        self.ui.btn_clear.clicked.connect(self.numclear)
        self.ui.numtan.clicked.connect(self.numtan)
        self.ui.numsin.clicked.connect(self.numsin)
        self.ui.numcos.clicked.connect(self.numcos)
        self.ui.numrad.clicked.connect(self.numradical)
        self.ui.numfac.clicked.connect(self.numfactorial)
        self.ui.numcot.clicked.connect(self.numcot)

    def numbers(self,x):
        self.ui.textbox.setText(self.ui.textbox.text()+ x)
    
    def numdot(self):
        for i in self.ui.textbox.text():
            if '.' not in self.ui.textbox.text():
                self.ui.textbox.setText(self.ui.textbox.text()+ '.')
        
    def numsum(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.sign = '+'

    def nummin(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.sign = '-'
    
    def nummul(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.sign = '*'

    def numdiv(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.sign = '/'
    
        
    def numclear(self):
        self.ui.textbox.setText('')
    
    def numtan(self):
        self.num1 = float(self.ui.textbox.text())
        result=math.tan(math.radians(self.num1))
        self.ui.textbox.setText(str(result))

    def numcos(self):
        self.num1 = float(self.ui.textbox.text())
        result=math.cos(math.radians(self.num1))
        self.ui.textbox.setText(str(result))

    def numsin(self):
        self.num1 = float(self.ui.textbox.text())
        result=math.sin(math.radians(self.num1))
        self.ui.textbox.setText(str(result))

    def numcot(self):
        self.num1 = float(self.ui.textbox.text())
        result=cot(math.radians(self.num1))
        self.ui.textbox.setText(str(result))

    def numradical(self):
        self.num1 = float(self.ui.textbox.text())
        result=math.sqrt(self.num1)
        self.ui.textbox.setText(str(result))

    def numfactorial(self):
        self.num1 = float(self.ui.textbox.text())
        result=math.factorial(self.num1)
        self.ui.textbox.setText(str(result))

    def numeq(self):
        self.num2 = float(self.ui.textbox.text())

        if self.sign == '+':
            result = self.num1 + self.num2
        elif self.sign == '-':
            result = self.num1 - self.num2
        elif self.sign == '*':
            result = self.num1 * self.num2
        elif self.sign == '/':
            if self.num2 != 0:
                result = self.num1 / self.num2
            else:
                self.ui.textbox.setText("Can't devided by Zero")

        self.ui.textbox.setText(str(result))
    
app = QApplication([])
window = HelloWorld()

app.exec()



