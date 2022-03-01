import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

objects = ["Menu", "LineEdit"]

class TextEditor(QWidget):

	def __init__(self):
		QWidget.__init__(self)
		self.setGeometry(300, 300, 500, 500)
		self.setMinimumSize(200, 200)
		self.setObjectName(objects[0])
		self.txt_editor = QPlainTextEdit(self)
		self.current_path = None
		self.mainui()

	def mainui(self):
		self.txt_editor.setObjectName(objects[1])




def display():
	import sys
	w = QApplication(sys.argv)
	w.setApplicationName("Chiropter")
	BatStyle = open("BatStyle.qss", "r")
	with BatStyle:
		qss = BatStyle.read()
		w.setStyleSheet(qss)
	w.setStyle("Breeze")
	ui = TextEditor()
	ui.show()
	sys.exit(w.exec())


display()
