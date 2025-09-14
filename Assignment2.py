# Q1
L = [11, 12, 13, 14]
L.extend([50, 60])                     
print(L)
L.remove(11); L.remove(13)             
print(L)
print(sorted(L))                       
print(sorted(L, reverse=True))         
print(13 in L)                         
print(len(L))                          
print(sum(L))                          
print(sum(x for x in L if x % 2 != 0)) 
print(sum(x for x in L if x % 2 == 0)) 
def is_prime(n): 
    return n>1 and all(n%i for i in range(2,int(n**0.5)+1))
print(sum(x for x in L if is_prime(x)))
L.clear()                              
print(L)
del L                                 

# Q2
lst = [2, 4, 6, 8]
s = 0
for i in lst: s += i
print(s)

# Q3
lst = [2, 3, 4]
m = 1
for i in lst: m *= i
print(m)

# Q4
arr = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
print(arr)

# Q5
D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
D[8] = 8.8                             
del D[2]                               
print(6 in D)                          
print(len(D))                          
print(sum(D.values()))                 
D[3] = 7.1                             
D.clear()                              
print(D)

# Q6
S1 = {10,20,30,40,50,60}
S2 = {40,50,60,70,80,90}
S1.update([55,66])                     
S1.discard(10); S1.discard(30)         
print(40 in S1)                        
print(S1 | S2)                         
print(S1 & S2)                         
print(S1 - S2)                         

# Q7
import random, string
for _ in range(100):                   
    l = random.randint(6,8)
    print(''.join(random.choice(string.ascii_letters) for _ in range(l)))
for n in range(600,801):               
    if is_prime(n): print(n)
for n in range(100,1001):              
    if n%7==0 and n%9==0: print(n)

# Q8
exam_st_date = (11,12,2025)
print(f"The examination will start from: {exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}")

# Q9
nums = [10,15,20,25,33,40,55]
for n in nums:
    if n%5==0: print(n)

# Q10
n = int(input("Enter number: "))
is_even = (n%2==0)
print("Even" if is_even else "Odd")

# Q11
txt = "Emma is good. Emma likes Python. Emma works hard."
print(txt.count("Emma"))

# Q12
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
new_list = [x for x in list1 if x%2!=0] + [y for y in list2 if y%2==0]
print(new_list)

# Q13
positions = [(2,3),(4,5),(6,7),(7,8)]
print([p for p in positions if p[0]%2==0])

# Q14
sensor_data = {1:2.3,2:4.5,3:1.8,4:3.6}
print([k for k,v in sensor_data.items() if v>3.0])

# Q15
commands_received = {"MOVE","TURN_LEFT","TURN_RIGHT","STOP"}
commands_executed = {"MOVE","TURN_LEFT","STOP"}
print(commands_received - commands_executed)
