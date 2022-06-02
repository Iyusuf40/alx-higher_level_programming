#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
list_ = sys.argv
num = 0
for _ in list_:
    num += 1
err1 = "Usage: ./100-my_calculator.py <a> <operator> <b>"
err2 = "Unknown operator. Available operators: +, -, * and /"
operators = "+-/*"
if num != 4:
    print("{}".format(err1))
    exit(1)

if list_[2] not in operators:
    print("{}".format(err2))
    exit(1)

a = int(list_[1])
b = int(list_[3])
op = list_[2]

if __name__ == "__main__":
    if op == "+":
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif op == "-":
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    elif op == "/":
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
    elif op == "*":
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
