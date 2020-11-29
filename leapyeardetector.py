"""
def leapyeardetector(year):
    isnot = "This year is not a leap year."
    isly = "This was a leap year!"
    print("The values for the modulo of the year are as follows: % 4 =", year % 4, "| % 100 =", year % 100, "| % 400 =",
          year % 400)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return isly
            else:
                return isnot
        else:
            return isly
    else:
        return isnot
"""


def leapyeardetector(year):
    isnot = "This year is not a leap year."
    isly = "This was a leap year!"
    print("The values for the modulo of the year are as follows: % 4 =", year % 4, "| % 100 =", year % 100, "| % 400 =",
          year % 400)
    if year % 4 == 0 and year % 100 != 0:
        return isly
    elif year % 400 == 0:
        return isly
    else:
        return isnot

def leapyeardetectormod(year):
    isnot = "This year is not a leap year."
    isly = "This was a leap year!"
    yearvalue = year
    if yearvalue % 4 == 0 and yearvalue % 100 == 0 and yearvalue % 400 == 0:
        return isly
    else:
        print(yearvalue % 4)
        print(yearvalue % 100)
        print(yearvalue % 400)
        return isnot


print("Please input a year.")
print(leapyeardetector((int(input()))))
