while True:
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} is a leap year.")
        days = 366
    else:
        print(f"{year} is not a leap year.")
        days = 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    print(f"In {year} there are:\nDays: {days}\nHours: {hours}\nMinutes: {minutes}")