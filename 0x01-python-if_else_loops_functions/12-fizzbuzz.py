#!/usr/bin/python3
def fizzbuzz():
    for _ in range(1, 101):
        if _ % 3 == 0 and _ % 5 == 0:
            print("{} ".format("FizzBuzz"), end="")
        elif _ % 3 == 0:
            print("{} ".format("Fizz"), end="")
        elif _ % 5 == 0:
            print("{} ".format("Buzz"), end="")
        else:
            print("{} ".format(_), end="")
