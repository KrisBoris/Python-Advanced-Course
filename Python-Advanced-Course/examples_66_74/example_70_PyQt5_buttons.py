# Example 70 - PyQt5 Buttons

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python App")
        self.setWindowIcon(QIcon("Blue_Raven_1.jpg"))
        self.setGeometry(200, 200, 400, 640)
        self.button = QPushButton("Launch a missile", self)
        self.label = QLabel("Missile ready", self)
        self.init_ui()

    def init_ui(self):
        self.button.setGeometry(50, 300, 300, 40)
        self.button.setStyleSheet("font-size: 20px;")
        self.button.clicked.connect(self.on_clicked)

        self.label.setGeometry(50, 350, 300, 50)
        self.label.setStyleSheet("font-size: 24px")

    def on_clicked(self):
        self.label.setText("Missile launch detected")
        self.button.setDisabled(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exit(app.exec_())


if __name__ == "__main__":
    main()