# Assignmennt 1
# Basic If–Else Problems:
# 1.
# solution 
'''n = int (input("Enter any number either postive or negavite: "))

if n > 0:
    print("Number is positive.")
elif n < 0:
    print('Number is negative.')
else:
    print('Number is zero.')

# 2.
# Solution
n = int(input('enter the number: '))
if n%2 == 0 :
    print ('Number is even')
else:
    print('Number is odd')

# 3.
# Solution
year = int (input ('Enter the year: '))

if year%4 == 0 and year % 100 == 0:
    print ('Leap year')
else:
    print('Not a leap year')

# 4.
# Solution
num1 = float (input('Enter first number: '))
num2 = float (input('Enter second number: '))

if num1 > num2 :
    print('Num1 is grater than num2.')
else:
    print('Num2 is greater than num1.')

# 5.
# Solution
age = int (input('Enter the age: '))
if age >= 18 :
    print('Eligible to vote')
else:
    print("You're not Eligible to vote.")

# 6.
# Solution
alpha = str(input('Enter alphabet to check vowel or consonant: '))
if (alpha == 'a', alpha == 'e', alpha == 'i', alpha == 'o', alpha == 'u', alpha == 'A', alpha == 'E', alpha== 'I', alpha == 'O', alpha == 'U'):
    print("entered alphabet is vowel")
else:
    print("Entered alphabet is consonent")

# 7.
# Solution
num = int( input('Enter the number : '))

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# 8.
# Solution
dg = int(input('Enter the digit: '))
num = len(str(dg))
if num == 1:
    print ('One digit')
elif num == 2:
    print('Two digit')
else:
    print('More than two digits')

# 9.
# Solution
marks = float (input ('Enter your marks: '))

if marks >= 40:
    print ('PASS')
else :
    print ("FAIL")

# 10.
# Solution
num = int (input ('Enter the number: '))

if num % 3  == 0 and num %7 == 0:
    print ("Number is multiple of both 3 and 7")
else:
    print ('Number is not multiple of both 3 and 7')'''

# Ladder If & Nested If:
# 1.
# Solution
'''num1 = float(input ('Enter frist number: '))
num2 = float (input('Enter second number: '))
num3 = float (input('Enter third number: '))

if num1 >= num2 and num1 >= num3: 
    
    print (f'{num1} is greatest number.')
elif num2 > num1 and num2 > num3:
    
    print (f'{num2} is greatest number.')
else:
    print (f'{num3} is greatest number.')

# 2.
# Solution
age = int(input("enter your age: "))

if age < 13 and age >= 0:
    print('You are child.')
elif age>= 13 and age <= 19:
    print ("You're Teenager")
elif age >= 20 and age <= 59:
    print("You're adult.")
elif age >= 60:
    print('You\'re Senior')
else:
    print("INVALID INPUT")

# 3.
# Solution
marks = float (input("Enter your marks: "))

if marks <= 100 and marks >= 90:
    print('You got \'A\' grade.')
elif marks >=75 and marks <= 89:
    print('You got \'B\' grade.')
elif marks >= 50 and marks <75:
    print ('You got \'C\' grade.')
elif marks >= 35 and marks <50:
    print ('You got \'C\' grade.')
else :
    print ("You're FAIL")

# 4.
# Solution
side1 = float(input ('Enter the first side of triangle: '))
side2 = float (input('Enter the second side of triangle: '))
side3 = float (input('Enter the third side of triangle: '))

if side1 == side2 == side3:
    print ("It's an equilateral triangle.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("It's an isosceles triangle.")
elif side1 != side2 != side3:
    print("It's a scalene triangle.")
else :
    print("Enter the correct input.")

# 5.
# Solution
char = input("Enter any character: ")
if ord(char) in range(65,91):
    print('UPPERCASE')
elif ord(char) in range (97,123):
    print('LOWERCASE')
elif ord(char) in range (48,58):
    print('DIGITs')
else:
    print('Special Characters')

# 6.
# Solution
units = int(input('Enter your units of electricity: '))
bill = 0
if units <= 100:
    bill = units * 5
    print(f"Electricity bill is {bill}")
    
elif 101 <= units <= 200:
    bill = (100*5) + ((units-100) * 7)
    print(f"Electricity bill {bill}")
else:
    bill = (100*5)+(100*7)+((units-200)*10)
    print(f"Electricity bill is {bill}")
# 7.
# Solution
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter forth number: "))

if num1 >= num2:
    if num1 >= num3:
        if num1 >= num4:
            print (num1, 'is greatest number')
        else :
            print (num4, 'is the greatest nummber') 
    else:
        if num3 >= num4:
            print(num4," is the greatest number")
        else:
            print(num4, 'is the greatest number')
else :
    if num2 >= num1:
        if num2 >= num3:
            if num2 >= num4:
                print(num2, 'is the greatest number')
            else :
                print (num4, 'is the greatest nummber')
        else:
            if num3 >= num4:
                print(num3, 'is the greatest number')
            else:
                print(num4, 'is the greatest number')

# 8.
# Solution
year = int (input('Enter the year: '))

if year % 100 == 0:
    if year % 4 == 0:
        print('Year is century year and also leap year')
    else:
        print('Given year is century year')
else:
        print('Given year is leap year')

# 9.
# Solution
wght = float(input('Enter your weight in kg: '))
hght = float(input('Enter you height in meter: '))
BMI = (wght/(hght**2))

if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI <= 24.9:
    print('Normal')
elif 25 <= BMI <= 29.9:
    print('Overweight')
else:
    print('Obese')

# 10.
# Solution
num1 = float(input("enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 <= num2:
    if num1 <= num3:
        print(num1, 'is smallest number')
    else:
        print(num3, "is smallest number")
else:
    if num2 <= num1:
        if num2 < num3:
            print(num2, 'is smallest number')
        else:
            print(num3, 'is smallest number')'''
    
# For Loop Problems:
# 1.
# Solution
# i =100
'''def sum_digit(n):
    return sum((int(d)**len(str(n))) for d in str(n))
for i in range(100,1000):
    if sum_digit(i) == i:
        print(i)

# 2.
# Solution
def prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
        
    return True
        
num = int(input("Enter your number : "))
for j in range(2,num+1):
    if prime(j):
        print(j)


# 3.
# Solution
def sum_digit(n):
    return sum(int(d) for d in str(n))
ls = []
for i in range(1,501):
    if i % 3 == 0 and sum_digit(i) <= 10:
        ls.append(i)
print(ls)

# 4.
# Solution
n = int(input("Enter your number : "))
for i in range(n):
    for j in range(i,n):
        print(" ", end = " ")
    # print()
# for i in range(n):
    for j in range (i):
        print("*", end = " ")
    for j in range(i+1):
        print("*", end = " ")
    print()

# 5.
# Solution
s = input("Enter the string: ")
s= s.lower()
pangram = True
for ch in "abcdefghijklmnopqrstuvwxyz":
    if ch not in s:
        pangram = False
        break

if pangram:
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")

# 6.
# Solution





# 7.
# Solution
num = int(input("Enter the number to check Harshad number: "))
sum_digit = sum(int(d) for d in str(num))
if num % sum_digit == 0:
    print(f'{num} is Harshad number')
else:
    print(f'{num} is not Harshad number')


# 8.
# Solution





#9.
#Solution 
n = 10
result = 0 
for i in range (1, n+1):
    result += (i**2)
    i += 1
print(result)



# 10.
# Solution




'''
# While Loop Problems:
# 11.
# Solution




# 12.
# Solution
'''total = 0
while total <= 100:
    num = int(input("Enter the number: "))
    i = num
    while i > 0:
        ld = i % 10
        total += ld
        i //= 10
    print(f"Current total sum :{total}")

print(f"Final total: {total}")

# 13.
# Solution

# while True:
#     num = input("Enter the number : ")
#     if len(num) == 0:
#         break
#     if num.startswith("0"):
#         print("It's not a duck number.")
#     else:
#         print("It's a duck number.")

# 14.
# Solution


# 17.
# Solution
i = 9875
num = i
while num >= 10:
    sum_digit = 0
    while num > 0:
        ld = num % 10
        sum_digit += ld
        num //= 10
    num = sum_digit
print(sum_digit)

# 20.Write a program to simulate an ATM machine using a while loop where a user can:
• Check balance
• Deposit money
• Withdraw money (only if balance is sufficient)
• Exit
Continue until the user chooses to exit.

# 
# ch = input("Enter the character : ")
# if ch ==' ':
#     ch += 1
#     print(ch)
    '''

'''num = int(input("Enter your number : "))
for i in range(2,num):
    if num%i == 0:
        print("Not prime")
    else:
        print(f"{i} is prime")'''




    