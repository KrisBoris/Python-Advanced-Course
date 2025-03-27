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
                font-size: 80px;
                font-family: calibri;
                font-weight: bold;                
                border: 3px solid;
                border-radius: 20px;
                padding: 20;
                margin: 8;                
            }
            QPushButton{
                background-color: hsl(203, 100%, 50%);
            }
            QLabel{
                background-color: white;
            }
        """)
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.restart_button)

        vbox.addWidget(self.time_label)
        vbox.addLayout(hbox)

        self.time_label.setAlignment(Qt.AlignHCenter)

        self.setLayout(vbox)

        self.start_button.clicked.connect(self.start_timer)
        self.stop_button.clicked.connect(self.stop_timer)
        self.restart_button.clicked.connect(self.restart_timer)

        self.timer.timeout.connect(self.update_timer)

    def start_timer(self):
        self.timer.start(10)
        self.start_button.setDisabled(True)

    def stop_timer(self):
        self.timer.stop()
        self.start_button.setDisabled(False)

    def restart_timer(self):
        self.stop_timer()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))
        self.start_button.setDisabled(False)

    def update_timer(self):
        self.time_label.setText(self.format_time(self.time))
        self.time = self.time.addMSecs(10)

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"


def start_stopwatch():
    app = QApplication(sys.argv)
    stopwatch_window = Stopwatch()
    stopwatch_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start_stopwatch()
