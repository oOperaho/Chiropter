import sys
import os
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
		self.pulled_file = None
		self.setMenuBar(self.menu)
		self.MenuBar()
		self.Actions()
		self.TxtField()
		self.Rightclick()

	def MenuBar(self):
		self.file = QMenu("&File", self)
		self.edit = QMenu("&Edit", self)
		self.style = QMenu("&Styles", self)
		self.menu.addMenu(self.file)
		self.menu.addMenu(self.edit)
		self.menu.addMenu(self.style)
		self.menu.setObjectName(objects[3])

		#  File button setting
		self.new_file = QAction("&New", self)
		self.new_file.setShortcut("Ctrl+N")
		self.open_file = QAction("&Open", self)
		self.open_file.setShortcut("Ctrl+O")
		self.save_file = QAction("&Save", self)
		self.save_file.setShortcut("Ctrl+S")
		self.saveas_file = QAction("&Save as", self)
		self.saveas_file.setShortcut("Ctrl+Shift+S")
		self.quit = QAction("&Quit", self)
		self.quit.setShortcut("Ctrl+Q")
		self.file.addAction(self.new_file)
		self.file.addAction(self.open_file)
		self.file.addAction(self.save_file)
		self.file.addAction(self.saveas_file)
		self.file.addSeparator()
		self.file.addAction(self.quit)

		#  Edit button setting
		self.copy_text = QAction("&Copy", self)
		self.copy_text.setShortcut("Ctrl+C")
		self.paste_text = QAction("&Paste", self)
		self.paste_text.setShortcut("Ctrl+V")
		self.cut_text = QAction("&Cut", self)
		self.cut_text.setShortcut("Ctrl+X")
		self.undo_text = QAction("&Undo", self)
		self.undo_text.setShortcut("Ctrl+Z")
		self.redo_text = QAction("&Redo", self)
		self.redo_text.setShortcut("Ctrl+Shift+Z")
		self.select_text = QAction("&Select All", self)
		self.select_text.setShortcut("Ctrl+A")
		self.edit.addAction(self.copy_text)
		self.edit.addAction(self.paste_text)
		self.edit.addAction(self.cut_text)
		self.edit.addAction(self.undo_text)
		self.edit.addAction(self.redo_text)
		self.edit.addAction(self.select_text)

		#  Style button setting
		self.style.addAction(QAction("&BatStyle", self))
		self.style.addAction(QAction("&Photony", self))
		self.style.addAction(QAction("&Afterbreeze", self))


	def TxtField(self):
		self.txt_editor.setObjectName(objects[1])
		self.txt_layout.setObjectName(objects[2])
		self.txt_layout.addWidget(self.txt_editor)
		self.txt_widget.setLayout(self.txt_layout)
		self.setCentralWidget(self.txt_widget)

	def Actions(self):
		#  File menu actions
		self.new_file.triggered.connect(self.newFile)
		self.open_file.triggered.connect(self.openFile)
		self.save_file.triggered.connect(self.saveFile)
		self.saveas_file.triggered.connect(self.saveFileas)
		self.quit.triggered.connect(self.quitEditor)

		#  Edit menu actions
		self.copy_text.triggered.connect(self.txt_editor.copy)
		self.paste_text.triggered.connect(self.txt_editor.paste)
		self.cut_text.triggered.connect(self.txt_editor.cut)
		self.undo_text.triggered.connect(self.txt_editor.undo)
		self.redo_text.triggered.connect(self.txt_editor.redo)
		self.select_text.triggered.connect(self.txt_editor.selectAll)

	def newFile(self):
		self.create_new = QMessageBox()
		self.create_new.setWindowTitle("Create new file")
		self.create_new.setText("\nHow do you want to create a new file?")
		self.buttons = self.create_new.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
		self.yesButton = self.create_new.button(QMessageBox.Yes)
		self.yesButton.setText("Save and open new file")
		self.noButton = self.create_new.button(QMessageBox.No)
		self.noButton.setText("Just open a new file")
		self.cancelButton = self.create_new.button(QMessageBox.Cancel)
		self.create_new.exec_()
		if self.create_new.clickedButton() == self.yesButton:
			pass


		elif self.create_new.clickedButton() == self.noButton:
			self.txt_editor.setPlainText("")
			self.changeWindowTitle()
		else:
			pass

	def openFile(self):
		self.alert_box = QMessageBox.question(self, "Open file", "\nThe current changes will be overwrited. \nMake sure you saved the file.", QMessageBox.Ok | QMessageBox.Cancel)
		if self.alert_box == QMessageBox.Ok:
			self.pulled_file, _ = QFileDialog.getOpenFileName(self, "Search Your File", ".", "Text Docs (*.txt);All files (*.*)")
			if self.pulled_file == "":
				pass
			else:
				try:
					self.pulled_file_text = open(self.pulled_file).read()
				except Exception as e:
					#  Change this to QMessageBox
					print(str(e))
				else:
					self.txt_editor.setPlainText(self.pulled_file_text)
					self.changeWindowTitle()
		else:
			pass

	def saveFile(self):
		if self.pulled_file is None:
			return self.saveFileas()
		
		self.manageSave(self.pulled_file)


	def saveFileas(self):
		self.pulled_file, _ = QFileDialog.getSaveFileName(self, "Save Your File", "Unknown.txt")

		if self.pulled_file == "":
			pass
		
		self.manageSave(self.pulled_file)

	def manageSave(self, path):
		self.currently_writing = self.txt_editor.toPlainText()

		try:
			with open(path, "w") as f:
				f.write(self.currently_writing)
		except Exception as e:
			#  Change this to QMessageBox
			print(str(e))
		else:
			self.pulled_file = path
			self.changeWindowTitle()

	def changeWindowTitle(self):
		if self.pulled_file is None:
			self.setWindowTitle("Unknown.txt")
		else:
			self.pulled_filename = QUrl.fromLocalFile(self.pulled_file)
			self.setWindowTitle(self.pulled_filename.fileName() + " | Chiropter")

	def quitEditor(self):
		self.quitask = QMessageBox.question(self, "Leaving?", "Did you save your file?", QMessageBox.Yes | QMessageBox.No)
		if self.quitask == QMessageBox.Yes:
			sys.exit()
		else:
			pass

	def Rightclick(self):
		#  Right click menu
		self.txt_editor.setContextMenuPolicy(Qt.ActionsContextMenu)
		self.copy_text = QAction("&Copy", self)
		self.copy_text.setShortcut("Ctrl+C")
		self.txt_editor.addAction(self.copy_text)
		self.paste_text = QAction("&Paste", self)
		self.paste_text.setShortcut("Ctrl+V")
		self.txt_editor.addAction(self.paste_text)
		self.cut_text = QAction("&Cut", self)
		self.cut_text.setShortcut("Ctrl+X")
		self.txt_editor.addAction(self.cut_text)
		self.undo_text = QAction("&Undo", self)
		self.undo_text.setShortcut("Ctrl+Z")
		self.txt_editor.addAction(self.undo_text)
		self.redo_text = QAction("&Redo", self)
		self.redo_text.setShortcut("Ctrl+Shift+Z")
		self.txt_editor.addAction(self.redo_text)
		self.select_text = QAction("&Select All", self)
		self.select_text.setShortcut("Ctrl+A")
		self.txt_editor.addAction(self.select_text)
		
		self.copy_text.triggered.connect(self.txt_editor.copy)
		self.paste_text.triggered.connect(self.txt_editor.paste)
		self.cut_text.triggered.connect(self.txt_editor.cut)
		self.undo_text.triggered.connect(self.txt_editor.undo)
		self.redo_text.triggered.connect(self.txt_editor.redo)
		self.select_text.triggered.connect(self.txt_editor.selectAll)
		


def display():
	import sys
	w = QApplication(sys.argv)
	w.setApplicationName("Chiropter")
	BatStyle = open("Styles/BatStyle.qss", "r")
	with BatStyle:
		qss = BatStyle.read()
		w.setStyleSheet(qss)
	w.setStyle("Breeze")
	ui = TextEditor()
	ui.show()
	w.exec()


display()
