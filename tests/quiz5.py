# 5. Write a program to find the largest and smallest numbers in a list without using built-in functions like max() or min().
numbers = [3,8,2,9,4,7,1,6,5]


min = numbers[0]
max = numbers[0]


for number in numbers:
    if min > number:
        min = number
    if max < number:
        max = number
        
        
print("maximum = ", max)
print("minimum = ", min)

