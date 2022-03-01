import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

objects = ["Menu", "TxtLayout"]

class TextEditor(QWidget):

	def __init__(self):
		QWidget.__init__(self)
		self.setGeometry(300, 300, 500, 500)
		self.setMinimumSize(200, 200)
		self.setObjectName(objects[0])
		self.current_path = None
		self.mainui()

	def mainui(self):
		self.layout = QVBoxLayout(self)
		self.txt_editor = QPlainTextEdit(self)

		self.layout.addWidget(self.txt_editor)
		self.layout.setObjectName(objects[1])




def display():
	import sys
	w = QApplication(sys.argv)
	w.setApplicationName("Chiropter")
	with open("BatStyle.qss", "r") as f:
		qss = f.read()
		w.setStyleSheet(qss)
	ui = TextEditor()
	ui.show()
	sys.exit(w.exec())


display()
