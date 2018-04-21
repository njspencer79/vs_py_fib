import json


def fib_generator(num_req=0):

    # Attempt to convert num_req to int
    try:
        int_num_req = int(num_req)
    except ValueError:
        return ['Failed to convert.  Not an Integer', 400]

    # Check if num_req is positive
    if int_num_req <= 0:
        return ['You must provide a positive integer.', 400]

    fib_list = []

    a, b = 0, 1  # Init. first two numbers in sequence
    for i in range(int_num_req):
        fib_list.append(a)  # add to end of our list
        if int_num_req - 1 != i:  # If we are on last run or not
            a, b = b, a + b  # shifting left and adding next number

    return fib_list
