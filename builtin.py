'''
Write a Python program with builtin function to multiply all the numbers in a list

Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

Write a Python program with builtin function that checks whether a passed string is palindrome or not.

Write a Python program that invoke square root function after specific milliseconds.

Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858

Write a Python program with builtin function that returns True if all elements of the tuple are true
'''
#1
s = input('input some numbers: ')
arr = list(s.split(' '))
def multi(arr):
    prod = 1
    for i in arr:
        prod *= int(i)
    return prod
print(multi(arr))
#2
s = input('input some string with upper- and lowercase letters: ')
def LScounter(s):
    up = 0
    low = 0
    for i in s:
        if i.islower() and i != ' ':
            low += 1
        elif i.isupper():
            up += 1
    print(f'number of uppercase letters: {up}.\nnumber of lowercase letters: {low}.')
    return 0
LScounter(s)
#3
s = input('input string: ')
def ispalindrom(s):
    p = s[::-1]
    if p == s:
        return True
    return False
print(ispalindrom(s))
#4
from math import sqrt
from time import sleep

def calculate_square_root(number, delay_ms):
  sleep(delay_ms / 1000)  # Convert milliseconds to seconds
  result = sqrt(number)
  print(f"Square root of {number} after {delay_ms} milliseconds is {result}")

number = float(input("Enter a number: "))
delay_ms = int(input("Enter delay in milliseconds: "))

calculate_square_root(number, delay_ms)
#5
mytup1 = (True, True, False)
mytup2 = (True, True)
all_true = all(mytup1)

if all_true:
 print("All elements are True")
else:
 print("Not all elements are True")