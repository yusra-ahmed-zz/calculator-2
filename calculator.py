"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

while True:
    maths = raw_input("Please enter your problem: ")
    maths = maths.split()
    if maths[0] == "+":
        print add(float(maths[1]), float(maths[2]))
    if maths[0] == "-":
        print subtract(float(maths[1]), float(maths[2]))
    if maths[0] == "*":
        print multiply(float(maths[1]), float(maths[2]))
    if maths[0] == "/":
        print divide(float(maths[1]), float(maths[2]))
    if maths[0] == "square":
        print square(float(maths[1]))
    if maths[0] == "cube":
        print cube(float(maths[1]))
    if maths[0] == "pow":
        print power(float(maths[1]), float(maths[2]))
    if maths[0] == "mod":
        print mod(float(maths[1]), float(maths[2]))
    if maths[0] == "q" or maths[0] == "quit":
        print "Get out of here!"
        break

