import os
import sys
from SideEditor import Rightclick
from SideEditor import Actions
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

objects = ["Menu", "LineEdit", "Box", "MenuBar", "StatusBar"]


class TextEditor(QMainWindow):

	def __init__(self, parent=None):
		super().__init__(parent=parent)
		self.resize(500, 500)
		self.setObjectName(objects[0])
		self.txt_editor = QPlainTextEdit(self)
		self.txt_layout = QVBoxLayout(self)
		self.txt_widget = QWidget(self)
		self.menu = QMenuBar(self)
		self.currentStatus = QLabel(self)
		self.pulled_file = None
		self.setMenuBar(self.menu)
		self.MenuBar()
		Actions(self)
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

		#  Status bar setting
		self.txt_editor.textChanged.connect(self.manageStatus)

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
		self.check_words = QAction("&Words...", self)
		self.check_words.setShortcut("Ctrl+Shift+A")
		self.edit.addAction(self.copy_text)
		self.edit.addAction(self.paste_text)
		self.edit.addAction(self.cut_text)
		self.edit.addAction(self.undo_text)
		self.edit.addAction(self.redo_text)
		self.edit.addAction(self.select_text)
		self.edit.addAction(self.check_words)

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

	def makeStatusBar(self):
		self.statusbar = self.statusBar()
		self.statusbar.addWidget(self.currentStatus)
		self.currentStatus.setText("Unsaved")
		self.currentStatus.setStyleSheet("""color: white; font-size: 12px""")

	def manageStatus(self):
		#  Everytime the text changes, the status changes to Unsaved

		self.currentStatus.setText("Unsaved")

	def checkWords(self):
		self.words_on_text = self.txt_editor.toPlainText().replace(" ", "")
		if self.currentStatus.text() == "Unsaved" or self.currentStatus.text() == "Saved":
			self.currentStatus.setText(f"{self.currentStatus.text()}   {len(self.words_on_text)} characters")

	def newFile(self):
		#  Create window for new file

		self.new_file_window = TextEditor(self)
		self.new_file_window.show()
		#self.new_file_window.setWindowTitle("Unknown.txt | Chiropter")
		self.changeWindowTitle()

	def openFile(self):
		#  Open selected file

		if self.currentStatus.text() == "Unsaved":
			self.alert_box = QMessageBox.question(self, "Open file", "\nYou have unsaved changes. \nDo you want to open a file anyway?.", QMessageBox.Yes | QMessageBox.Cancel)
			if self.alert_box == QMessageBox.Yes:
				return self.manageOpenFile()
			else:
				pass
		else:
			return self.manageOpenFile()

	def manageOpenFile(self):
		self.currentStatus.setText("Opening new file")
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

	def saveFile(self):
		#  Save current file

		if self.pulled_file is None:
			self.currentStatus.setText("Saving")
			return self.saveFileas()
		
		self.manageSave(self.pulled_file)
		self.currentStatus.setText("Saved")  #  Sets status bar everytime the file is saved

	def saveFileas(self):
		#  Create file and save it

		self.pulled_file, _ = QFileDialog.getSaveFileName(self, "Save Your File", "Unknown.txt")

		if self.pulled_file == "":
			pass
		
		self.manageSave(self.pulled_file)
		self.currentStatus.setText("Saved")

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

	def closeEvent(self, signal):
		#  Quit with X button

		if self.currentStatus.text() == "Unsaved":
			self.quitask = QMessageBox.question(self, "Leaving?", "\nYou have unsaved changes. \nAre you sure you want to quit?", QMessageBox.Yes | QMessageBox.No)
			if self.quitask == QMessageBox.Yes:
				signal.accept()
			else:
				signal.ignore()
		else:
			signal.accept()

	def quitEditor(self):
		#  Quit button pressed

		if self.currentStatus.text() == "Unsaved":
			print("how")
			self.quitask = QMessageBox.question(self, "Leaving?", "\nYou have unsaved changes. \nAre you sure you want to quit?", QMessageBox.Yes | QMessageBox.No)
			if self.quitask == QMessageBox.Yes:
				sys.exit()
			else:
				pass
		else:
			sys.exit()
