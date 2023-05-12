# 1. Write a program to find all prime numbers between two given integers.

number1 = int(input("enter your first number: "))
number2 = int(input("enter your second number: "))

while(number1 == number2):
    print("your numbers should not be same so enter again")
    number1 = int(input("enter your first number: "))
    number2 = int(input("enter your second number: "))

if number1 > number2:
    number1, number2 = number2, number1
 
list_of_prime_numbers = []

for i in range(number1, number2+1):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        list_of_prime_numbers.append(i)
        
print(list_of_prime_numbers)
    
    
    
    
    
    
    
    
    
    
    
    
    