"""Author: Akachukwu Mba
   Aim: This program is a calculator that performs basic, medium, and complex operations."""

import keyboard
def main():
    print("        HELLO! WELCOME TO THE UNIVERSAL CALCULATOR!!!        \n")
    print("        Press Esc to quit, press Enter to continue    \n")
    while True:
        if keyboard.is_pressed("esc"):
            print("Thank you for using our calculator. Maybe some other time!")
            break

        if keyboard.is_pressed("Enter"):
            print("        Here is a list of operations this calculator can perform: \n")
            print("        Basic Operations")
            print("           A. Addition")
            print("           B. Subtraction")
            print("           C. Multiplication")
            print("           D. Division")
            print("        Medium Operations")
            print("           E. Modulo     ")
            print("           F. Exponential")
            print("           G. Square root")
            print("           H. Absolute Value")
            print("        Complex Operations")
            print("           I. Permutations")
            print("           J. Combinations")
            print("           K. Logarithms")
            print("           L. Base conversions")
            choice = input("Enter your choice:")
            if (choice == "a" or choice == "A"):
                fig1 = float(input("Enter digit 1: \n"))
                fig2 = float(input("Enter digit 2: \n"))
                print("The sum of " + str(fig1) + " and " + str(fig2) + " is: " + str(addition(fig1,fig2)))
                break

            if (choice == "b" or choice == "B"):
                fig1 = float(input("Enter digit 1: \n"))
                fig2 = float(input("Enter digit 2: \n"))
                print("The difference between " + str(fig1) + " and " + str(fig2) + " is: " + str(subtraction(fig1,fig2)))
                break

            if (choice == "c" or choice == "C"):
                fig1 = float(input("Enter digit 1: \n"))
                fig2 = float(input("Enter digit 2: \n"))
                print("The product of " + str(fig1) + " and " + str(fig2) + " is: " + str(multiplication(fig1,fig2)))
                break

            if (choice == "d" or choice == "D"):
                fig1 = float(input("Enter digit 1: \n"))
                fig2 = float(input("Enter digit 2: \n"))
                print("The quotient of " + str(fig1) + " and " + str(fig2) + " is: " + str(division(fig1,fig2)))
                break

            if (choice == "e" or choice == "E"):
                fig1 = float(input("Enter digit 1: \n"))
                fig2 = float(input("Enter digit 2: \n"))
                print("The modulo of " + str(fig1) + " and " + str(fig2) + " is: " + str(modulo(fig1,fig2)))
                break

            if (choice == "f" or choice == "F"):
                fig1 = float(input("Enter digit 1: \n"))
                fig2 = float(input("Enter digit 2: \n"))
                print("The exponent of " + str(fig1) + " and " + str(fig2) + " is: " + str(exponential(fig1,fig2)))
                break

            if (choice == "g" or choice == "G"):
                fig = float(input("Enter digit: \n"))
                print("The square root of " + str(fig) + " is: " + str(square_root(fig)))
                break

            if (choice == "h" or choice == "H"):
                fig = float(input("Enter digit: \n"))
                print("The absolute value of " + str(fig) + " is: " + str(absolute_value(fig)))
                break

            if (choice == "i" or choice == "I"):
                fig1 = int(input("Enter digit 1: \n"))
                fig2 = int(input("Enter digit 2: \n"))
                print("The permutation of " + str(fig1) + " and " + str(fig2) + " is: " + str(permutation(fig1,fig2)))
                break

            if (choice == "j" or choice == "J"):
                fig1 = int(input("Enter digit 1: \n"))
                fig2 = int(input("Enter digit 2: \n"))
                print("The combination of " + str(fig1) + " and " + str(fig2) + " is: " + str(combination(fig1,fig2)))
                break

            if (choice == "k" or choice == "K"):
                base = int(input("Enter base: \n"))
                number = float(input("Enter number: \n"))
                print("The logarithm of " + str(number) + " in base " + str(base) + " is: " + str(logarithm(base,number)))
                break

            if (choice == "l" or choice == "L"):
                number = int(input("Enter number: \n"))
                base1 = int(input("Enter initial base: \n"))
                base2 = int(input("Enter base to change to: \n"))
                print(f"{number} in base {base1} is {convert_base(number, base1, base2)} in base {base2}")
                break


"""Function to add two numbers"""

def addition(fig1,fig2):
    ans = fig1+ fig2
    return ans

"""Function to subtract two numbers"""

def subtraction(fig1,fig2):
    ans = fig1 - fig2
    return ans

"""Function to multiply two numbers"""

def multiplication(fig1,fig2):
    ans = fig1 * fig2
    return ans

"""Function to divide two numbers"""

def division(fig1,fig2):
    ans = fig1//fig2
    return ans

"""Function to find the modulo of two numbers"""

def modulo(fig1,fig2):
    ans = fig1 % fig2
    return ans
"""Function to find the exponent of a number to a particular power"""

def exponential(fig1,fig2):
    ans = fig1**fig2
    return ans

"""Function to find the square root of a number"""

def square_root(fig):
    ans = fig**0.5
    return ans

"""Function to find the absolute value of a number"""

def absolute_value(fig):
    if (fig < 0):
        ans = fig * -1
    else:
        return fig
    return ans

"""Helper function for the permutation and combination functions"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

"""Function to find the permutation of two numbers"""

def permutation(fig1,fig2):
    ans = factorial(fig1) // factorial(fig1 - fig2)
    return ans

"""Function to find the combination of two numbers"""

def combination (fig1,fig2):
    ans = factorial(fig1) // (factorial(fig2) * factorial(fig1 - fig2))
    return ans

"""Function to find the logarithm of a number to a particular base"""

def logarithm(base,number):
    power = 0
    while number >= base:
        power += 1
        number /= base
    return power

"""Function to convert a number from one base to another"""

def convert_base(num, base1, base2):
    base10 = 0
    num_str = str(num)
    for i in range(len(num_str)):
        digit = int(num_str[i])
        power = len(num_str) - i - 1
        base10 += digit * (base1 ** power)

    if base10 == 0:
        return '0'
    digits = []
    while base10 > 0:
        remainder = base10 % base2
        digits.append(str(remainder))
        base10 = base10 // base2
    digits.reverse()
    return ''.join(digits)




main()

