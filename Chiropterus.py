import sys
from MainEditor import TextEditor
from PyQt5.QtWidgets import QApplication


def display():
    w = QApplication(sys.argv)
    w.setApplicationName("Main | Chiropter")
    TextEditor()
    BatStyle = open("Styles/BatStyle.qss", "r")
    with BatStyle:
        qss = BatStyle.read()
        w.setStyleSheet(qss)
    w.setStyle("Fusion")
    ui = TextEditor()
    ui.show()
    w.exec()


if __name__ == "__main__":
    display()
