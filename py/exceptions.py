import sys as s

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
except ValueError:
    print("Kindly type a valid number !!!")
    s.exit(1)

try:
    z = x / y
except ZeroDivisionError:
    print("Cannot divode by zero !!")
    s.exit(1)

print(f"{x} divided by {y} is {z}")
