# Example 73 - PyQt5 Line Edits

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python App")
        self.setWindowIcon(QIcon("Blue_Raven_1.jpg"))
        self.setGeometry(100, 100, 400, 640)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.init_ui()

    def init_ui(self):
        self.line_edit.setGeometry(10, 10, 380, 50)
        self.line_edit.setStyleSheet("font-size: 24px;"
                                     "font-family: Arial;")
        self.button.setGeometry(50, 70, 300, 50)
        self.button.setStyleSheet("font-size: 24px;"
                                  "font-family: Arial;")
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        print(f"Hello there {self.line_edit.text()}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exit(app.exec_())


if __name__ == "__main__":
    main()
