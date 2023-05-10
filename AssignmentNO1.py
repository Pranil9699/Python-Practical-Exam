import sys
value = int(sys.argv[1])
if value >= 1 and value <= 50:
    print("Ok")
else:
    print("Out of range")
# Enter this Command From Shell- python main.py 24


# Write a program which finds sum of digits of a number.
# Example n=130 then output is 4 (1+3+0).

n = input("Enter a number: ")  # take input from user
# initialize sum variable to 0
sum = 0
# iterate over each digit in the number
for digit in n:
    # add the digit to the sum
    sum += int(digit)
print("Sum of digits:", sum)  # print the sum




#Print All Prime number Until Number Touched
n = int(input("Enter a number: "))
prime_numbers = []

for num in range(2, n+1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

print("Prime numbers till", n, "are:")
for prime in prime_numbers:
    print(prime)

    
    # Write a program that accept two integer values and if both are equal then prints “SAME 
# identity” otherwise prints, “DIFFERENT identity" . Look Accoring this program i write code you just check it correct or not and tell me ok ,
a=int(input("Enter First Num:"))
b=int(input("Enter Second Num:"))

if a is b:
  print("Same Identity")
else:
  print("DIFFERENT identity")


# Write a program to display following pattern.
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# look this ques and for my side 
for i in range(4, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
