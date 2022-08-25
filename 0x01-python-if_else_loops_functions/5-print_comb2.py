#!/usr/bin/python3
for number in range(100):
    lastNumber = range(100)[-1]
    if number == lastNumber:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
