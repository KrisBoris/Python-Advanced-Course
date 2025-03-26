# Example 76 - Stopwatch program

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.restart_button = QPushButton("Restart", self)
        self.time = QTime(0, 0, 0, 0)
        self.timer = QTimer(self)
        self.ini_ui()

    def ini_ui(self):
        self.setGeometry(300, 400, 300, 150)
        self.setWindowTitle("Stopwatch App")
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-size: 50px;
                font-family: calibri;                
            }
        """)
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.restart_button)

        vbox.addWidget(self.time_label)

    def start_timer(self):
        pass

    def stop_timer(self):
        pass

    def restart_timer(self):
        pass

    def update_timer(self):
        pass

    def format_time(self, time):
        pass

def start_stopwatch():
    app = QApplication(sys.argv)
    stopwatch_window = Stopwatch()
    stopwatch_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start_stopwatch()
