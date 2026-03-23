def sum_list(my_list):
    total = 0

    for n in my_list:
        total = total + n

    return total


numbers = [2, 4, 6, 8]

result = sum_list(numbers)

print("Sum is:", result)