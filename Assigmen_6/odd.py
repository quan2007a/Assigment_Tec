def remove_odd(numbers):

    new_list = []

    for n in numbers:
        if n % 2 == 0:
            new_list.append(n)

    return new_list


# main program
nums = [1, 2, 3, 4, 5, 6, 7, 8]

result = remove_odd(nums)

print("Original list:")
print(nums)

print("List without odd numbers:")
print(result)