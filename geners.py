''' Create a generator that generates the squares of numbers up to some number N.

Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

Implement a generator that returns all numbers from (n) down to 0.'''
#1
def generate_squarenum(n):
    for i in range(n + 1):
        yield i*i
example = list(generate_squarenum(5))
print(*example)
#2
def generate_evens():
    n = int(input('input some number: '))
    for i in range(n + 1):
        if i%2 == 0:
            yield i
example = list(generate_evens())
print(*example, sep = ', ')
#3
def generate_34():
    n = int(input('input some number: '))
    for i in range(n + 1):
        if i%4 == 0 or i%3 == 0:
            yield i
example = list(generate_34())
print(*example, sep = ', ')
#4
def generate_squares(a, b):
    for i in range(a, b+1):
        yield i*i
example = list(generate_squares(1, 5))
print(*example, sep = ', ')
#5
def generate_back(n):
    for i in range(n, -1, -1):
        yield i
example = list(generate_back(5))
print(*example, sep = ', ')