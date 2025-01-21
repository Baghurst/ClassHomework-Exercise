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

#7.
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






