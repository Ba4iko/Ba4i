#1
class first:
  def __init__(self) -> None:
    self.string = ""
  def getstring(self):
    self.string = input('write something:\n')
  def printString(self):
    
    print(self.string.upper())
rom = first()
rom.getstring()
rom.printString()
#2
class Shape:
  def area(self):
    return 0
class Square(Shape):
  def __init__(self, length):
    super().__init__()
    self.length = length
  def area(self):
    return self.length * self.length
square = Square(5)
print(f"The area of the square is: {square.area()}")
#3
class Rectangle(Shape):
  def __init__(self, length, width):
    super().__init__()
    self.length = length
    self.width = width
  def area(self):
    return self.length * self.width
rect = Rectangle(4, 5)
print(f"The area of the rectangle is: {rect.area()}")
#4
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def move(self, x, y):
    self.x += x
    self.y += y
  def show(self):
    print(f"The coordinates are: {self.x} and {self.y}")
  def dist(self, b):
    res = ((self.x - b.x)**2 + (self.y - b.y)**2)**0.5
    print(f'distance between 2 points is: {res}')
p1 = Point(4, 5)
p2 = Point(1, 3)
p1.show()
p2.move(2, 3)
p2.show()
p1.dist(p2)
#5
class Account:
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance
  def info(self):
    print(self.owner)
    print(self.balance)
  def deposit(self, amount):
    self.balance += amount
  def withdraw(self, amount):
    if self.balance - amount < 0:
      print('no enough money to withdraw')
    else:
      self.balance -= amount
rob = Account('Rob', 25000)
rob.info()
rob.withdraw(26000)
rob.deposit(1000)
rob.withdraw(26000)
rob.info()
#6
def is_prime(num):
  if num <= 1:
        return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x : is_prime(x), numbers))
print(*prime_numbers)