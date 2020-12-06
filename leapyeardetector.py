def leapyeardetector(year):
    isnot = "This year is not a leap year."
    isly = "This was a leap year!"
    if year % 4 == 0 and year % 100 != 0:
        return isly
    elif year % 400 == 0:
        return isly
    else:
        return isnot


print("Please input a year.")
print(leapyeardetector((int(input()))))
