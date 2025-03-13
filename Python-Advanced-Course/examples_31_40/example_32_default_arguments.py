# Example 31 - Default arguments

import time


# Default arguments must be at the end of function declaration
def count(end, start=0):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)
    print("Done!")


count(3)
count(15, 10)
