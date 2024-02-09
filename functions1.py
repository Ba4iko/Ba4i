#1
def my_funciton():
    print("hello from the function")
#2
def my_funciton():
    print("hello from the function")
my_funciton()
#hello from the function
#3
def my_function(fname, lname):
  print(fname)
#prints fname
#4
def my_function(x):
   return x + 5
#5
def my_function(*kids):
  print("The youngest child is " + kids[2])
#"The youngest child is " + third elemnt of kids
#6
def my_function(**kid):
  print("His last name is " + kid["lname"])
#functions1.md
#1 recipe
def converting_to_ounces(x):
   return x * 28.3495241
#2 fahrenheit
def to_centigrade(x):
   print(float((5/9) * (x-32)))
#3 classic puzzle
def solve(numheads, numlegs):
    if numheads > numlegs:
        print("error")
    elif(numlegs % 2 != 0):
        print("error")
    else:
        rabbits=(numlegs-2*numheads)/2
        chickens = numheads - rabbits
        print(int(chickens),int(rabbits))
x, y = 35, 94
solve(x, y)
#4 filter primes
def check_prime(i):
  for x in range(2, i):
      if i % x == 0 or i == 1:
        return False
  return True

lis = [1, 3, 4, 5, 8, 12, 11]      
def filter_prime(some_list):
  arr = []
  for i in some_list:
    if check_prime(i) == True:
        arr.append(i)
  return arr
lis1 = filter_prime(lis)
#5
from itertools import permutations
st = input("input the string you want to permutate - ")
list1 = list(permutations(st))
for x in list1:
  print(x)
#6
string = 'abd fre der'
def Convert(string):
  li = list(string.split(" "))
  print(*li[::-1])
Convert(string)
#7
def has_33(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 3 and nums[i+1] == 3:
       return True
  return False

has_33([1, 3, 3]) #→ True
has_33([1, 3, 1, 3]) #→ False
has_33([3, 1, 3]) #→ False
#8
def spy_game(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 0:
      count += 1
    if count == 2 and nums[i] == 7:
      return True
    elif count != 2 and nums[i] == 7:
      return False
  return False

print(spy_game([1,2,4,0,0,7,5])) #--> True
print(spy_game([1,0,2,4,0,5,7])) #--> True
print(spy_game([1,7,2,0,4,5,0])) #--> False
#9
def Volume(rad):
  print(4/3 * 3.14 * rad**3)
Volume(3)
#10
def uniqe(smth):
  for i in range(len(smth)):
    for j in range(i + 1, len(smth)):
      if smth[j] == smth[i]:
        smth[j] = -1
  arr = []
  for i in smth:
    if i != -1:
      arr.append(i)
  return arr
smth = [1, 1, 1, 1, 3, 3, 4, 5, 6, 7, 7, 8]
print(*uniqe(smth))
#11
def ispalindrome(word):
  copy = word[::-1]
  if copy == word:
    return True
  return False
print(ispalindrome("abbad")) # false
print(ispalindrome("abba")) #true
#12
def histogram(arr):
  for i in arr:
    strin = '*'
    print(strin * i)
histogram([3, 4, 2])
#13
import random
def guess():
  number = random.randint(1, 21)
  name = input("Hello! What is your name?\n")
  print("Well, "+ name + ", I am thinking of a number between 1 and 20.\n")
  count = 0
  for i in range(20):
    count += 1
    x = int(input("Take a guess.\n"))
    if x < number:
      print("Your guess is too low.\n")
    elif x > number:
      print("Your guess is too high.")
    elif x == number:
      print("Good job, " + name +", You guessed my number in "+ str(count)+ " guesses!")
      break
guess()