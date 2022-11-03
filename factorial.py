#!/usr/bin/env python3

# Created by: Joseph Kwon
# Created on: November 1
# This program gets user's input and outputs the factorial


def main():

    # Tries to get the user's number as an integer.
    try:
        user_number = int(input("Enter a positive integer: "))

    # Exception thrown if the user did not enter a number
    except ValueError:
        input("You must enter a positive integer. Please try again.")

    # Restarts the program if the user entered a negative number
    if user_number < 0:
        print("You must enter a positive integer. Please try again.")

    else:

        # Initializing counter and product variables
        counter = 0
        product = 1

        # Code executed continually until user_number is equal to counter
        while True:
            counter = counter + 1
            product = product * counter
            print("Tracking {} times through the loop.".format(counter))
            if counter >= user_number:
                break

        # Outputs the factorial of user's number
        print("")
        print(("{}! = {}".format(user_number, product)))


if __name__ == "__main__":
    main()
