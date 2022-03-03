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
		self.txt_widget = QWidget(self)
		self.menu = QMenuBar(self)
		self.setMenuBar(self.menu)
		self.MenuBar()
		self.txtField()
		#self.rightclick()

	def MenuBar(self):
		self.file = QMenu("&File", self)
		self.edit = QMenu("&Edit", self)
		self.style = QMenu("&Style", self)
		self.menu.addMenu(self.file)
		self.menu.addMenu(self.edit)
		self.menu.addMenu(self.style)
		self.menu.setObjectName(objects[3])

		#  File button setting
		self.file.addAction(QAction("&New   Ctrl+N", self))
		self.file.addAction(QAction("&Open   Ctrl+N", self))
		self.file.addAction(QAction("&Save   Ctrl+N", self))
		self.file.addSeparator()
		self.file.addAction(QAction("&Quit   Ctrl+N", self))

		#  Edit button setting
		self.edit.addAction(QAction("&Copy", self))
		self.edit.addAction(QAction("&Paste", self))
		self.edit.addAction(QAction("&Cut", self))

		#  Style button setting
		self.style.addAction(QAction("&BatStyle", self))
		self.style.addAction(QAction("&Photony", self))


	def txtField(self):
		self.txt_editor.setObjectName(objects[1])
		self.txt_layout.setObjectName(objects[2])
		self.txt_layout.addWidget(self.txt_editor)
		self.txt_widget.setLayout(self.txt_layout)
		self.setCentralWidget(self.txt_widget)

	#def rightclick(self):
		#self.txt_widget.setContextMenuPolicy(Qt.ActionsContextMenu)
		#self.txt_widget.addAction(QAction("&Copy", self))
		#self.txt_widget.addAction(QAction("&Paste", self))
		#self.txt_widget.addAction(QAction("&Cut", self))


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
