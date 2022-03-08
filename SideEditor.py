from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

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
	self.check_words = QAction("&Words...", self)
	self.txt_editor.addAction(self.check_words)
		
	self.copy_text.triggered.connect(self.txt_editor.copy)
	self.paste_text.triggered.connect(self.txt_editor.paste)
	self.cut_text.triggered.connect(self.txt_editor.cut)
	self.undo_text.triggered.connect(self.txt_editor.undo)
	self.redo_text.triggered.connect(self.txt_editor.redo)
	self.select_text.triggered.connect(self.txt_editor.selectAll)
	self.check_words.triggered.connect(self.checkWords)

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
	self.check_words.triggered.connect(self.checkWords)

	#  About menu actions
	self.repo.triggered.connect(self.openRepo)
