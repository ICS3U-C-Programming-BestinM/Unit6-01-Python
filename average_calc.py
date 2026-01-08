#!/usr/bin/env python3
# Created by: bestin
# Created on: 10/22/2025
# This program generates 10 random numbers and calculates their average.


import random


def main():

    # Constants
    MAX_ARRAY_SIZE = 10
    MIN_NUM = 1
    MAX_NUM = 100

    # Input / Setup
    list_of_int = []

    # Process: Generate random numbers
    for counter in range(MAX_ARRAY_SIZE):
        random_number = random.randint(MIN_NUM, MAX_NUM)
        list_of_int.append(random_number)

    # Output: Display numbers
    print("The random numbers are:")
    for number in list_of_int:
        print(number)

    # Process: Calculate average using a loop
    total = 0
    for number in list_of_int:
        total = total + number

    average = total / MAX_ARRAY_SIZE

    # Output: Display average
    print("\nThe average is:", average)


# This ensures the program starts
if __name__ == "__main__":
    main()
