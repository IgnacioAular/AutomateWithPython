
# Developer: Ignacio Aular
# ignacio345@gmail.com
# Tue Jun 2, 11:00 PM


# Write a function named collatz() that has one parameter named number. 
def collatz(number):
    # If number is even, then collatz() should print number // 2 and return this value.
    if number % 2 == 0:
        print(number)
        number //= 2
    # If number is odd, then collatz() should print and return 3 * number + 1.
    else:
        print(number)
        number = number * 3 + 1
    # we check if the value of the variable number is equal to one to print it
    # before the condition of the external while loop is evaluated
    if number == 1:
        print(number)
    return number

# Then write a program that lets the user type in an integer
try:
    n = int(input("Enter an integer number: "))
    # and that keeps calling collatz() on that number until the
    # function returns the value 1.
    while n != 1:
        n = collatz(n)
except ValueError:
    print("You must enter an integer number.")
s
