# Example 74 - PyQt5 CSS style

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python App")
        self.setWindowIcon(QIcon("Blue_Raven_1.jpg"))
        self.button1 = QPushButton("Red Ranger")
        self.button2 = QPushButton("Yellow Ranger")
        self.button3 = QPushButton("Blue Ranger")
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.setStyleSheet("""
            QPushButton{
                font-size: 24px;
                font-family: Arial;
                font-weight: bold;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 8px
            }
            QPushButton#button1{
                background-color: hsl(0, 77%, 49%)
            }
            QPushButton#button2{
                background-color: hsl(61, 98%, 50%)
            }
            QPushButton#button3{
                background-color: hsl(197, 98%, 51%)
            }
            QPushButton#button1:hover{
                background-color: hsl(0, 100%, 75%)
            }
            QPushButton#button2:hover{
                background-color: hsl(61, 100%, 75%)
            }
            QPushButton#button3:hover{
                background-color: hsl(197, 100%, 75%)
            }
        """)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exit(app.exec_())


if __name__ == "__main__":
    main()
