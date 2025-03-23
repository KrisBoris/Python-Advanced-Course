# Example 64 - Multithreading

import threading
import time


def do_homework():
    time.sleep(8)
    print("You have done your homework")


def write_in_notebook(name, cause):
    time.sleep(4)
    print(f"{name} dies of {cause}")


def eat_potato_chip():
    time.sleep(2)
    print("You took a potato chip and ate it!")


thread1 = threading.Thread(target=do_homework)
thread2 = threading.Thread(target=write_in_notebook, args=("Lind L. Taylor", "heart attack"))
thread3 = threading.Thread(target=eat_potato_chip)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("You are now a God of the new world!")
