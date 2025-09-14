# 1
def diff17(n):
    return abs(n-17)*2 if n>17 else 17-n

# 2
def test_range(n):
    return abs(1000-n)<=100 or abs(2000-n)<=100

# 3
def reverse_string(s):
    return s[::-1]

# 4
def count_case(s):
    d={"UPPER":0,"LOWER":0}
    for c in s:
        if c.isupper(): d["UPPER"]+=1
        elif c.islower(): d["LOWER"]+=1
    return d

# 5
def distinct_list(lst):
    return list(set(lst))

# 6
def even_numbers(lst):
    return [x for x in lst if x%2==0]

# 7
def robot():
    def move():
        return "Moving"
    return move()

# 8
def student(name,age,course):
    pass
print(student.__code__.co_varnames[:student.__code__.co_argcount])

# 9
def move_robot(x,y,direction):
    if direction=="up": return (x,y+1)
    if direction=="down": return (x,y-1)
    if direction=="left": return (x-1,y)
    if direction=="right": return (x+1,y)
    return (x,y)

# 10
def classify_temperature(temp):
    if temp<15: return "Cold"
    if 15<=temp<=30: return "Moderate"
    return "Hot"

# 11
def is_goal_reached(path):
    x=y=0
    for p in path:
        if p=="up": y+=1
        elif p=="down": y-=1
        elif p=="left": x-=1
        elif p=="right": x+=1
    return (x,y)==(2,0)

# 12
class Student:
    def __init__(self,student_id,student_name,student_class):
        self.student_id=student_id
        self.student_name=student_name
        self.student_class=student_class
    def display(self):
        return self.__dict__

# 13
class Student:
    def __init__(self,student_id,student_name,student_class):
        self.student_id=student_id
        self.student_name=student_name
        self.student_class=student_class
student1=Student(1,"Alex","Math")
student2=Student(2,"Bob","Science")
print(student1.__dict__)
print(student2.__dict__)

# 14
import math
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return math.pi*self.r*self.r
    def perimeter(self):
        return 2*math.pi*self.r

# 15
class StringClass:
    def get_String(self):
        self.s=input("Enter string: ")
    def print_String(self):
        print(self.s.upper())

# 16
class Robot:
    def __init__(self,name,task,battery_level=100):
        self.name=name
        self.task=task
        self.battery_level=battery_level
    def perform_task(self):
        print(f"{self.name} is performing {self.task}")
        self.battery_level=max(0,self.battery_level-10)
    def recharge(self):
        self.battery_level=100
    def status(self):
        print(f"Name: {self.name}, Task: {self.task}, Battery: {self.battery_level}%")