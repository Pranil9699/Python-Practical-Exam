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
