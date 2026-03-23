def remove_odd(nums):

    new_list = []

    for n in nums:
        if n % 2 == 0:
            new_list.append(n)

    return new_list


data = [1, 2, 3, 4, 5, 6, 7, 8]

cut_list = remove_odd(data)

print("Original list:")
print(data)

print("After remove odd numbers:")
print(cut_list)