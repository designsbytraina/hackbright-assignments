"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

def pick_operation():
    """ Chooses which math operation to use based on user input of operator.

    Takes the first character and evaluates which math operation the user wants to use to do math!
    """

    print """Welcome to our calculator. Please use the below examples for formatting your entry!

    > + 1 2
    3
    > - 10 5
    5
    > * 2 3
    6
    > / 7 2
    3.500000
    > square 2
    4
    > cube 3
    27
    > pow 2 5
    32
    > mod 10 3
    1
    > q
    """

    while True:

        user_input = raw_input(">")
        tokenized_input = user_input.split()

        num1 = tokenized_input[1]
    
        if tokenized_input[0] == "+":
            num2 = tokenized_input[2]
            print add(num1, num2)

        elif tokenized_input[0] == "-":
            num2 = tokenized_input[2]
            print subtract(num1, num2)
        
        elif tokenized_input[0] == "*":
            num2 = tokenized_input[2]
            print multiply(num1, num2)

        elif tokenized_input[0] == "/":
            num2 = tokenized_input[2]
            print divide(num1, num2)

        elif tokenized_input[0] == "square":
            print square(num1)

        elif tokenized_input[0] == "cube":
            print cube(num1)

        elif tokenized_input[0] == "pow":
            num2 = tokenized_input[2]
            print power(num1, num2)

        elif tokenized_input[0] == "mod":
            num2 = tokenized_input[2]
            print mod(num1, num2)

        elif tokenized_input[0] == "q":
            break

        else:
            print "I don't understand."


pick_operation()