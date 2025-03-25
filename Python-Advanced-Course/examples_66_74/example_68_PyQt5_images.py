# Example 68 - PyQt5 Images

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python App")
        self.setGeometry(200, 200, 400, 640)
        self.setWindowIcon(QIcon("Blue_Raven_1.jpg"))

        label = QLabel(self)
        label.setGeometry(0, 0, 300, 300)

        pixmap = QPixmap("Blue_Raven_1.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2,
                          label.width(),
                          label.height())


def main():
    app = QApplication(sys.argv)  # Arguments passed in command line
    window = MainWindow()
    window.show()
    app.exit(app.exec_())


if __name__ == "__main__":
    main()
