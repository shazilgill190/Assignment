# Create a program to calculate the sum of the digits of an inputted integer.


def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

number = int(input("Enter an integer: "))
print("The sum of the digits is:", sum_of_digits(number))
