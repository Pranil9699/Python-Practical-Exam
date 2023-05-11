n = int(input("Enter the number of elements in the tuple: "))

tuple_of_numbers = tuple(map(int, input("Enter the elements of the tuple separated by spaces: ").split()))

print("Tuple of numbers:", tuple_of_numbers)

print("Maximum element in the tuple:", max(tuple_of_numbers))

print("Minimum element in the tuple:", min(tuple_of_numbers))

print("Sum of elements in the tuple:", sum(tuple_of_numbers))

        n = int(input("Enter a positive integer: "))

if n <= 1:

    print("No prime numbers in this range")

else:

    print("Prime numbers between 1 and", n, "are:")

    for i in range(2, n+1):

        is_prime = True

        for j in range(2, int(i**0.5)+1):

            if i % j == 0:

                is_prime = False

                break

        if is_prime:

            print(i, end=" ")
