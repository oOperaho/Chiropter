import os
import sys
from SideEditor import Rightclick
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

objects = ["Menu", "LineEdit", "Box", "MenuBar", "StatusBar"]


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
		self.makeStatusBar()
		Rightclick(self)

	def MenuBar(self):
		#  Main window
		self.file = QMenu("&File", self)
		self.edit = QMenu("&Edit", self)
		self.settings = QMenu("&Settings", self)
		self.menu.addMenu(self.file)
		self.menu.addMenu(self.edit)
		self.menu.addMenu(self.settings)
		self.menu.setObjectName(objects[3])

		#  File button setting
		self.new_file = QAction("&New", self)
		self.new_file.setShortcut("Ctrl+N")
		self.open_file = QAction("&Open...", self)
		self.open_file.setShortcut("Ctrl+O")
		self.save_file = QAction("&Save", self)
		self.save_file.setShortcut("Ctrl+S")
		self.saveas_file = QAction("&Save as...", self)
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

		#  Settings button setting
		self.styles = self.settings.addMenu("&Styles")
		self.language = self.settings.addMenu("&Language")
		self.batstyle = QAction("&BatStyle", self)
		self.afterbreeze = QAction("&Afterbreeze", self)
		self.english = QAction("&English", self)
		self.portuguese = QAction("&Portuguese")

		#  Adding submenus
		self.styles.addAction(self.batstyle)
		self.styles.addAction(self.afterbreeze)
		self.language.addAction(self.english)
		self.language.addAction(self.portuguese)


	def TxtField(self):
		#  Adding plain text to layout
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

	def keyPressEvent(self, signal):
		return self.manageStatusMessage()

	def manageStatusMessage(self):
		if self.pulled_file != None:
			self.check_file = open(self.pulled_file, "r").read()
			self.current_file = self.txt_editor.toPlainText()
			if self.check_file == self.current_file:
				pass
			else:
				self.currentStatus.setText("Unsaved")
		else:
			pass

	def newFile(self):
		#  Create window for new file

		self.new_file_window = TextEditor(self)
		self.new_file_window.show()
		self.new_file_window.setWindowTitle("Unknown.txt | Chiropter")

	def openFile(self):
		#  Open selected file

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
		#  Save current file

		if self.pulled_file is None:
			return self.saveFileas()
		
		self.manageSave(self.pulled_file)
		self.currentStatus.setText("Saved")

	def saveFileas(self):
		#  Create file and save it

		self.pulled_file, _ = QFileDialog.getSaveFileName(self, "Save Your File", "Unknown.txt")

		if self.pulled_file == "":
			pass
		
		self.manageSave(self.pulled_file)

	def manageSave(self, path):
		#  Does the process of saveFile() and saveFileas()

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
		#  Updates the title of the window

		if self.pulled_file is None:
			self.setWindowTitle("Unknown.txt")
		else:
			self.pulled_filename = QUrl.fromLocalFile(self.pulled_file)
			self.setWindowTitle(self.pulled_filename.fileName() + " | Chiropter")

	def quitEditor(self):
		#  Quit Chiropter

		self.quitask = QMessageBox.question(self, "Leaving?", "\nDo you want to quit?", QMessageBox.Yes | QMessageBox.No)
		if self.quitask == QMessageBox.Yes:
			sys.exit()
		else:
			pass

	def makeStatusBar(self):
		self.statusbar = self.statusBar()
		self.currentStatus = QLabel()
		self.currentStatus.setText("Unsaved")
		self.statusbar.addWidget(self.currentStatus)
		self.currentStatus.setObjectName(objects[4])
