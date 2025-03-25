# Example 72 - PyQt5 Radio Buttons

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python App")
        self.setWindowIcon(QIcon("Blue_Raven_1.jpg"))
        self.setGeometry(200, 200, 400, 640)
        self.radio1 = QRadioButton("Mastercard", self)
        self.radio2 = QRadioButton("Visa", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)
        self.group1 = QButtonGroup(self)
        self.group2 = QButtonGroup(self)
        self.init_ui()

    def init_ui(self):
        self.radio1.setGeometry(10, 10, 380, 50)
        self.radio2.setGeometry(10, 60, 380, 50)
        self.radio3.setGeometry(10, 110, 380, 50)
        self.radio4.setGeometry(10, 160, 380, 50)
        self.radio5.setGeometry(10, 210, 380, 50)
        self.setStyleSheet("QRadioButton{"
                           "font-size: 24px;"
                           "font-family: Arial;}")

        self.group1.addButton(self.radio1)
        self.group1.addButton(self.radio2)
        self.group1.addButton(self.radio3)
        self.group2.addButton(self.radio4)
        self.group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_toggled)
        self.radio2.toggled.connect(self.radio_button_toggled)
        self.radio3.toggled.connect(self.radio_button_toggled)
        self.radio4.toggled.connect(self.radio_button_toggled)
        self.radio5.toggled.connect(self.radio_button_toggled)

    def radio_button_toggled(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exit(app.exec_())

if __name__ == "__main__":
    main()
