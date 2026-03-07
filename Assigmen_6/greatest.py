numbers = []

text = input("Enter number: ")

while text != "":
    num = float(text)
    numbers.append(num)
    text = input("Enter number: ")

numbers.sort(reverse=True)

print("Five greatest numbers:")

count = 0
for n in numbers:
    if count < 5:
        print(n)
        count = count + 1