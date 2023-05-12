# 4. Write a program that prints out the sum of all numbers in a list that are divisible by 3 or 5.
numbers = [2,4,6,8,9,10,11,12,15,20,25,30]


sum = 0

for number in numbers:
    if(number %3 ==0 or number%5==0):
        sum = sum + number
        
print("sum:", sum)




nums = [2, 4, 6, 8, 9, 10, 11, 12, 15, 20, 25, 30]

total = 0
for num in nums:
    if num % 3 == 0 or num % 5 == 0:
        total += num

print("The sum of all numbers in the list divisible by 3 or 5 is", total)