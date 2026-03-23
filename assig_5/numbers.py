numbers = []

user_input = input("Enter a number: ")

while user_input != "":
    num = int(user_input)
    numbers.append(num)
    user_input = input("Enter a number: ")

numbers.sort(reverse=True)

print("Top numbers:")

i = 0
while i < 5 and i < len(numbers):
    print(numbers[i])
    i = i + 1