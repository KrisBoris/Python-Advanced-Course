# Example 71 - PyQt5 Checkboxes

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python App")
        self.setWindowIcon(QIcon("Blue_Raven_1.jpg"))
        self.setGeometry(200, 200, 400, 640)
        self.checkbox = QCheckBox("Do you think you're out of tune?", self)
        self.init_ui()

    def init_ui(self):
        self.checkbox.setStyleSheet("font-size: 24px;"
                                    "font-family: Comic Sans;")
        self.checkbox.setGeometry(10, 50, 380, 50)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("*Angry J.K. Simmons noises")
        else:
            print("Good job")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exit(app.exec_())


if __name__ == "__main__":
    main()
