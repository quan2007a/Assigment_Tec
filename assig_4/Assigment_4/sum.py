def sum_numbers(text):

    words = text.split()
    total = 0

    for word in words:
        if word.isdigit():
            total += int(word)

    return total


text = "Today is January 16 2025 The temperature is 11 degrees Celsius"
print(sum_numbers(text))