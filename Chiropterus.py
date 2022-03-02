import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

objects = ["Menu", "LineEdit", "Box", "MenuBar"]

class TextEditor(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.resize(500, 500)
		self.setObjectName(objects[0])
		self.txt_editor = QPlainTextEdit(self)
		self.txt_layout = QVBoxLayout(self)
		self.txtField()
		self._createMenuBar()


	def _createMenuBar(self):
		self.menu = QMenuBar(self)
		self.setMenuBar(self.menu)
		self.menu.addMenu("&File")
		self.menu.addMenu("&Edit")
		self.menu.addMenu("&Style")
		self.menu.setObjectName(objects[3])

	def txtField(self):
		self.txt_editor.setObjectName(objects[1])
		self.txt_layout.setObjectName(objects[2])
		self.txt_layout.addLayout(self.txt_editor)



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
