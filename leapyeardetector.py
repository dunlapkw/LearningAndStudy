def leap_year_detector(year):
    is_not = "This year is not a leap year."
    is_ly = "This was a leap year!"
    if year % 4 == 0 and year % 100 != 0:
        return is_ly
    elif year % 400 == 0:
        return is_ly
    else:
        return is_not


print("Please input a year.")
print(leap_year_detector((int(input()))))
