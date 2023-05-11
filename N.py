n = int(input("Enter the number of elements in the tuple: "))

tuple_of_numbers = tuple(map(int, input("Enter the elements of the tuple separated by spaces: ").split()))

print("Tuple of numbers:", tuple_of_numbers)

print("Maximum element in the tuple:", max(tuple_of_numbers))

print("Minimum element in the tuple:", min(tuple_of_numbers))

print("Sum of elements in the tuple:", sum(tuple_of_numbers))

        Enter the number of elements in the tuple: 5

Enter the elements of the tuple separated by spaces: 1 2 3 4 5

Tuple of numbers: (1, 2, 3, 4, 5)

Maximum element in the tuple: 5

Minimum element in the tuple: 1

Sum of elements in the tuple: 15
