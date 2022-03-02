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

		self.menu = QMenuBar(self)
		self.setMenuBar(self.menu)
		#self.txt_widget = QWidget(self)
		self.txtField()
		self._createMenuBar()


	def _createMenuBar(self):
		self.menu.addMenu("&File")
		self.menu.addMenu("&Edit")
		self.menu.addMenu("&Style")
		self.menu.setObjectName(objects[3])

	def txtField(self):
		self.txt_editor.setObjectName(objects[1])
		self.txt_editor.resize(self.frameGeometry().height(), self.frameGeometry().width())
		#self.txt_editor.move()
		#self.txt_widget.setLayout(self.txt_layout)


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
	w.exec()


display()
