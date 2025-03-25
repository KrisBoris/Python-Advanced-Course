# Example 67 - PyQt5 Labels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python App")
        self.setGeometry(200, 200, 400, 640)
        self.setWindowIcon(QIcon("Blue_Raven_1.jpg"))

        label = QLabel("Hello there", self)
        label.setFont(QFont("Comic Sans", 36))
        label.setGeometry(0, 20, 400, 80)
        label.setStyleSheet("color: #e02424;"
                            "background-color: #404040;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        label.setAlignment(Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)  # Arguments passed in command line
    window = MainWindow()
    window.show()
    app.exit(app.exec_())


if __name__ == "__main__":
    main()
