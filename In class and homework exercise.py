#2.
print("Number 2: ")
temp = int(input("Enter a temperature: "))
if temp < 32 :
    print ("ice")
elif temp < 112:
    print ("water")
else:
    print ("steam")
        
#3.
print("Number 3: ")
x = 1
if x > 3:
    if x > 4:
        print("A", end=" ")
    print("B", end=" ")
elif x < 2:
    if x > 0:
        print("C", end=" ")
    print("D")

#4.
print("Number 4: ")
weather = "rain"
if weather == "sunny":
    print("wear sunblock")
elif weather == "snow":
    print("going skiing")
else:
    print(weather)

#5.
#This line of code is meant to be wrong.
'''print('Number5: ')
if int('zero') == 0 :
    print ("zero")
elif str(0) == 'zero' :
    print(0)
elif str(0) == '0 ' :
    print (str(0))
else:
    print ("none of the above") '''

#6.
print('Number6: ')
n = int(input("Enter the value of n: "))
if n == 0:
    print("zero")
elif n == 1:
    print("one")
elif n == 2:
    print("two")
else:
    print("three")

#7. (Don't understand the output)
print('Number7: ')
n = int(input("Enter an integer: "))
if n < 1:
    print("invalid value")
else:
    for i in range(1, n + 1):
        print(i * i)

#8.     
print('Number8: ')
#(A)
print('A: ')
n = int(input("Enter an integer: "))
if n > 0:
    for a in range(1, n + n):
        print(a / (n /2))
    else:
        print("Now quitting")
#(B)
print('B: ')
n = int (input( "Enter an integer: "))
if n > 0:
    for a in range(1, n + n) :
        print(a / (n/2))
else:
    print("Now quitting")

#9.
print('Number9: ')
#A
print('A: ')
for i in range(100, 0, -3):
    print(i)
#B
print("B: ")
num = int(input("Enter a number: "))
for i in range(num):
    if num > 0:
        print(num % 10)
        num = num // 10
    else:
        break
#C
print("C: ")
num = int(input("Enter a number: "))
count = 0
sum = 0
for i in range(num):
    if num > 0:
        count += 1
        sum += num % 10
        num = num // 10
    else:
        break

if count == 10:
    print(sum / float(count))
#10
print("10: ")
#(a)
print("A: ")
min = 0
max = num
num = int(input("Enter num: "))
if num < 0:
    min = num
    max = 0
sum = 0
i = min
while i <= max:
    sum += i
    i += 1
#(b)    
print("B: ")
i = 1
while i < 16:
    if i % 3 == 0:
        print(i)
    i += 1
#(c)
print("C: ")   
i = 0
while i < 4:
    j = 0
    while j < 5:
        if i + 1 == j or j + i == 4:
            print("+", end=' ')
        else:
            print("o", end=' ')
        j += 1
    print()
    i += 1
#11
print("11: ")
#A
print("A: ")
count = 0
while count < 10:
    print("Hello")
    count += 1
#B (Don't understand the output)
print("B: ")
x = 10
y = 0
while x > y:
    print(x, y)
    x = x - 1
    y = y + 1
#C
print("C: ")    
keepgoing = True
x = 100
while keepgoing:
    print(x)
    x = x - 10
    if x < 50:
        keepgoing = False
#D(Don't understand the output)
'''print("D: ")
x = 45
while x < 50 :
    print (x)'''
#E
print("E: ")
for x in [1,2,3,4,5]:
    print (x)
#F
print("F: ")
for x in range(5):
    print (x)
#G
print("G: ")
for p in range(1,10):
    print (p)
#H
print("H: ")
for q in range(100,50,-10):
    print (q)
#I
print("I: ")
for z in range(-500, 500, 100):
    print (z)
#J
print("J: ")
for y in range(500,100,100):
    print (" * ", y)
#K
print("K: ")
x = 10
y = 5
for i in range(x-y * 2):
    print (" % ", i)
#L (Don't understand the output)
print("L: ")
for x in[1,2,3]:
    for y in [4, 5, 6]:
        print (x, y)
#M (Don't understand the output)
print("M: ")     
for x in range(3):
    for y in range(4):
        print (x, y, x + y)
#N
print("N: ")
c = 0
for x in range(10):
    for y in range(5):
        c += 1
print (c)

#12 (I don't understand the output)
print("12: ")
for i in range(4):
    for j in range(5):
        if i + 1 == j or j + i == 4:
            print("+", end=' ')
        else:
            print("o", end=' ')
    print()
#13 How many times is of the if clause evaluated? (for 12)

#14
print("14: ")
#A
print("A: ")      
        
#15   
print("15: ") 
a = int(input("Enter a value: ")) 
while a != 0:
    count = count + 1
    a = int(input("Enter a value: "))
print("You entered", count, "value.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
   
