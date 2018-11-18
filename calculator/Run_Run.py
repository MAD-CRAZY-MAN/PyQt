from Run import *

def event(self):
	self.pushButton.clicked.connect(self.cal)

def cal(self):
	a = self.lineEdit_1.text()
	b = self.lineEdit_2.text()
	opreator = self.comboBox.currentText()

	try:
		c = eval(a+opreator+b)
		self.lineEdit_3.setText(str(c))
	except:
		 Qtwidgets.QMessageBox.critical(MainWindow, 'Error', 'Invalid inputs!', Qtwidgets.QMessageBox.Ok)

Ui_MainWindow.event = event
Ui_MainWindow.cal = cal

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.event()
    MainWindow.show()
    sys.exit(app.exec_())