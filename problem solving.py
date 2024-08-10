def numbers():
   
    input_numbers = input("Enter a list of integers : ")
    numbers = list(map(int, input_numbers.split()))

    unique_numbers = set(numbers)

    sorted_numbers = sorted(unique_numbers, reverse=True)

    print("Sorted numbers in descending order without duplicates:", sorted_numbers)

numbers()