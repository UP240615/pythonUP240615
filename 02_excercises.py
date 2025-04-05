score = int(input("Enter your score: "))

if score < 50:
    print(f"Your grade is F")
elif score <= 59 and score >= 50:
    print(f"Your grade is D")
elif score <= 69 and score >= 60:
    print(f"Your grade is C")
elif score <= 89 and score >= 70:
    print(f"Your grade is B")
elif score <= 100 and score >= 90:
    print(f"Your grade is A")
else:
    print(f"Score no valid")

    month = input("Enter the current month: ").upper()

if month == "SEPTEMBER" or month == "OCTOBER" or month == "NOVEMBER":
    print(f"The current season is Autumn")
elif month == "DECEMBER" or month == "JANUARY" or month == "FEBRUARY":
    print(f"The current season is Winter")
elif month == "MARCH" or month == "APRIL" or month == "MAY":
    print(f"The current season is Spring")
elif month == "JUNE" or month == "JULY" or month == "AUGUST":
    print(f"The current season is Summer")
else:
    print(f"Invalid Data")

fruits = ['Bannana', 'Orange', 'Apple', 'Strawberry']
newFruit = input("Enter a fruit: ").lower()

if newFruit in fruits:
    print(f"The {newFruit} it's already in the list: ")
else:
    print(f"Adding the {newFruit}...")
    fruits.append(newFruit)
print(fruits)