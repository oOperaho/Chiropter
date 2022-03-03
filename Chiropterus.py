import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

objects = ["Menu", "LineEdit", "Box", "MenuBar", "SubMenu"]


class TextEditor(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.resize(500, 500)
		self.setObjectName(objects[0])
		self.txt_editor = QPlainTextEdit(self)
		self.txt_layout = QVBoxLayout(self)
		self.txt_widget = QWidget(self)
		self.menu = QMenuBar(self)
		self.setMenuBar(self.menu)
		self.txtField()
		self.MenuBar()

	def MenuBar(self):
		self.file = QMenu("&File", self)
		self.edit = QMenu("&Edit", self)
		self.style = QMenu("&Style", self)
		self.menu.addMenu(self.file)
		self.menu.addMenu(self.edit)
		self.menu.addMenu(self.style)
		self.menu.setObjectName(objects[3])

		#  File button setting
		self.new_file = QAction("&New", self)
		self.file.addAction(self.new_file)
		self.open_file = QAction("&Open")
		self.file.addAction(self.open_file)
		self.save_file = QAction("&Save", self)
		self.file.addAction(self.save_file)
		self.quit = QAction("&Quit", self)
		self.file.addAction(self.quit)





	def txtField(self):
		self.txt_editor.setObjectName(objects[1])
		self.txt_layout.setObjectName(objects[2])
		self.txt_layout.addWidget(self.txt_editor)
		self.txt_widget.setLayout(self.txt_layout)
		self.setCentralWidget(self.txt_widget)
		

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
