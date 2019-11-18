'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
 
 
class MySignal(QObject):
    signal1 = pyqtSignal()
 
    def run(self):
        self.signal1.emit()
 
 
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        mysignal = MySignal()
        mysignal.signal1.connect(self.signal1_emitted)
        mysignal.run()
    
    @pyqtSlot()
    def signal1_emitted(self):
        print("signal1 emitted")
 

 
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MySignal(QObject):
    siganl1 = pyqtSignal()
    siganl2 = pyqtSignal(int, int)

    def run(self):
        self.siganl1.emit()
        self.siganl2.emit(1, 2)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mysignal = MySignal()
        mysignal.siganl1.connect(self.signal1_emitted)
        mysignal.siganl2.connect(self.signal2_emitted)
        mysignal.run()

    @pyqtSlot()
    def signal1_emitted(self):
        print("signal1 emitted")

    @pyqtSlot(int, int)
    def signal2_emitted(self, arg1, arg2):
        print("siganl2 emitted", arg1, arg2)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()