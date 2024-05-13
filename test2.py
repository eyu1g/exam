def count_occurrences(numbers, search_number):
    count = 0
    for num in numbers:
        if num == search_number:
            count += 1
    return count

# Get the sequence of numbers from the user
sequence = input("Enter a sequence of numbers, separated by spaces: ")
numbers = list(map(int, sequence.split()))

# Get the number to be searched from the user
search_number = int(input("Enter a number to be searched: "))

# Determine if the number is present in the array
occurrences = count_occurrences(numbers, search_number)

# Display the number of times it appears
if occurrences == 0:
    print("The number", search_number, "is not present in the array.")
else:
    print("The number", search_number, "appears", occurrences, "time(s) in the array.")