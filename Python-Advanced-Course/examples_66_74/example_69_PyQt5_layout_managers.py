# Example 69 - PyQt5 Layout Managers

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python App")
        self.setGeometry(200, 200, 400, 640)
        self.setWindowIcon(QIcon("Blue_Raven_1.jpg"))
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("Red Ranger", self)
        label2 = QLabel("Blue Ranger", self)
        label3 = QLabel("Green Ranger", self)
        label4 = QLabel("Yellow Ranger", self)
        label5 = QLabel("Pink Ranger", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: blue;")
        label3.setStyleSheet("background-color: #1Aed0e;")
        label4.setStyleSheet("background-color: yellow;")
        label5.setStyleSheet("background-color: #ff00d9;")

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)
        hbox.addWidget(label5)

        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 1, 2)

        central_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)  # Arguments passed in command line
    window = MainWindow()
    window.show()
    app.exit(app.exec_())


if __name__ == "__main__":
    main()
