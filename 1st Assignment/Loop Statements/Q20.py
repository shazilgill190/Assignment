# Create a program that simulates a countdown timer starting from a given number down to zero.

import time


start = int(input("Enter the starting number for the countdown: "))

for number in range(start, -1, -1):
    print(number)
    time.sleep(1)

print("Countdown complete!")