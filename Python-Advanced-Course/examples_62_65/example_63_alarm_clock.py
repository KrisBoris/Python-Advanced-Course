# Example 63 - Alarm clock

import time
import datetime
import pygame


def set_alarm(alarm_time):

    print(f"Alarm set for {alarm_time}")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    music_file = "SnK OST - Armored Titan Theme.mp3"

    while current_time != alarm_time:
        print(current_time)
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

    print("Wake the f up samurai!")

    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
