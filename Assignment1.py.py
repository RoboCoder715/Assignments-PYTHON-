# 1
print("""Twinkle, twinkle, little star,
      How I wonder what you are!
            Up above the world so high,
            Like a diamond in the sky.
Twinkle, twinkle, little star,
      How I wonder what you are""")

# 2
first = input("Enter first name: ")
last = input("Enter last name: ")
print(last + " " + first)

# 3
from math import pi
r = float(input("Enter radius: "))
print(pi * r * r)

# 4
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1])

# 5
n = int(input("Enter n: "))
print(n + int(str(n)*2) + int(str(n)*3))

# 6
data = input("Enter numbers separated by commas: ")
lst = data.split(",")
tup = tuple(lst)
print(lst)
print(tup)

# 7
c = float(input("Enter Celsius: "))
print((c * 9/5) + 32)

# 8
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print(a, b)

# 9
num = int(input("Enter number: "))
print("Even" if num % 2 == 0 else "Odd")

# 10
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# 11
import math
x1, y1 = map(float, input("Enter x1 y1: ").split())
x2, y2 = map(float, input("Enter x2 y2: ").split())
print(math.dist([x1, y1], [x2, y2]))

# 12
a, b, c = map(int, input("Enter three angles: ").split())
print("Triangle" if a+b+c == 180 else "Not Triangle")

# 13
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
print(p * ((1 + r/100) ** t - 1))

# 14
n = int(input("Enter number: "))
if n > 1:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

# 15
N = int(input("Enter N: "))
print(sum(i*i for i in range(1, N+1)))