# Example 75 - Digital clock

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont, QFontDatabase


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.timer_label = QLabel("12:00:00", self)
        self.timer = QTimer(self)
        self.init_ui()

    def init_ui(self):
        self.setGeometry(400, 300, 300, 100)
        self.setWindowTitle("Digital Clock App")

        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("font-size: 150px;"
                                       "color: hsl(105, 100%, 50%);")
        self.setStyleSheet("background-color: black;")

        font_id = QFontDatabase.addApplicationFont("DS_Fonts/DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        clock_font = QFont(font_family, 150)
        self.timer_label.setFont(clock_font)

        vbox = QVBoxLayout()
        vbox.addWidget(self.timer_label)
        self.setLayout(vbox)

        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

        self.update_timer()

    def update_timer(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.timer_label.setText(current_time)


def digital_clock():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    digital_clock()
