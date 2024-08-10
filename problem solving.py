def numbers():
    # Read from the console
    input_numbers = input("Enter a list of integers : ")
    numbers = list(map(int, input_numbers.split()))

    # Remove duplicates by converting to a set
    unique_numbers = set(numbers)

    #descending order
    sorted_numbers = sorted(unique_numbers, reverse=True)

    # Print the result
    print("Sorted numbers in descending order without duplicates:", sorted_numbers)

numbers()