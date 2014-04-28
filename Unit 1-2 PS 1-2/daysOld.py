# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#
 
def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif (year % 100 == 0):
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

    years = year2 - year1
    daysInYears = 0
    i = 0
    counted = False
    if years > 0:
        counted = True
    while years > 0:
        if isLeapYear(year1 + i + 1):
            daysInYears += 366
        else:
            daysInYears += 365
        years -= 1
        i += 1


    months = month2 - month1
    daysInMonths = 0
    j = 0
    # Loop for each month
    while months > 0:
        # days in this month: month1 = starting point; j = incrementor; -1 b/c daysOfMonths list starts at 0
        days = daysOfMonths[month1 + j - 1]
        if days == 28 and isLeapYear(year2) and not counted: # If February, check if it is a leap year
            daysInMonths += 29
        else:
            daysInMonths += days
        months -= 1
        j += 1


    days = day2 - day1

    total = daysInYears + daysInMonths + days
    print daysInYears, daysInMonths, days, total
    return total


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()


# MORE CONCISE VERSION

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    def isLeapYear(year):
        if year % 400 == 0:
            return True
        elif (year % 100 == 0):
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    def daysInYear(year, month, day):
        daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
        total = day
        month -= 1 # We don't want to count the current month, day covers that
        if isLeapYear(year) and month >= 2: # if this is a leap year and we have passed February (2 in this case = March)
            total += 1
        while month > 0:
            total += daysOfMonths[month-1]
            month -= 1
        return total

    days = 0
    y1 = year1
    y2 = year2
    while y2 > y1:
        days += 365
        if isLeapYear(y1):
            days += 1
        y1 += 1

    total = days + daysInYear(year2, month2, day2) - daysInYear(year1, month1, day1)
    return total


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()