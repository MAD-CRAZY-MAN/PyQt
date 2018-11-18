from untitled import *
from PyQt5 import QtCore, QtGui, QtWidgets

def intro_menu(self):
	self.intro_bt.clicked.connect(lambda x:self.stackedWidget.setCurrentIndex(1))
	self.esc_1.clicked.connect(lambda x:self.stackedWidget.setCurrentIndex(0))
	self.member_bt.clicked.connect(lambda x:self.stackedWidget.setCurrentIndex(2))
	self.achive_bt.clicked.connect(lambda x:self.stackedWidget.setCurrentIndex(3))
	self.esc_2.clicked.connect(lambda x:self.stackedWidget.setCurrentIndex(0))
	self.esc_3.clicked.connect(lambda x:self.stackedWidget.setCurrentIndex(0))
	
Ui_MainWindow.intro_menu = intro_menu

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.intro_menu()

    MainWindow.show()
    sys.exit(app.exec_())