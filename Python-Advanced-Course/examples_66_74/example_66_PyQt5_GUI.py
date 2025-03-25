# Example 66 - PyQt5 GUI Intro

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python App")
        self.setGeometry(200, 200, 400, 640)
        self.setWindowIcon(QIcon("Blue_Raven_1.jpg"))


def main():
    app = QApplication(sys.argv)  # Arguments passed in command line
    window = MainWindow()
    window.show()
    app.exit(app.exec_())


if __name__ == "__main__":
    main()
