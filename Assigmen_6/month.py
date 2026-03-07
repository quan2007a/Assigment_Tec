seasons = ("spring", "summer", "autumn", "winter")

month = int(input("Enter month number: "))

if month == 3 or month == 4 or month == 5:
    print(seasons[0])

elif month == 6 or month == 7 or month == 8:
    print(seasons[1])

elif month == 9 or month == 10 or month == 11:
    print(seasons[2])

else:
    print(seasons[3])