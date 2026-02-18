from datetime import datetime, date

# This ensures the value entered is a digit


def valid_digit(digit_type):
    invalid_digit = True
    while invalid_digit:
        digit = input("Enter the " + digit_type + ": ")
        if digit.isdigit():
            digit = int(digit)
            invalid_digit = False
        else:
            print("Invalid value entered")
    return digit

# This ensures the value entered is in the range given


def valid_digit_in_range(digit_type, min, max):
    invalid_digit = True
    while invalid_digit:
        digit = valid_digit(digit_type)
        if digit >= min and digit <= max:
            invalid_digit = False
        else:
            print("Invalid value entered")
    return digit


"""Asks the user for the date validating at each step and 
then combines and formats the inputs. Doesn't consider leap years"""


def user_date():
    year = valid_digit("year")
    month = valid_digit_in_range("month", 1, 12)
    if month == 2:
        day = valid_digit_in_range("day", 1, 28)
    elif month in [4, 6, 9, 11]:
        day = valid_digit_in_range("day", 1, 30)
    else:
        day = valid_digit_in_range("day", 1, 31)
    date = str(year) + "-" + str(month) + "-" + str(day)
    return datetime.strptime(date, "%Y-%m-%d").date()


"""Alternative method to input date without input validation"""
# date_input = input("Enter a date (YYYY-MM-DD): ")
# date_input = datetime.strptime(date_input, "%Y-%m-%d").date()

"""Takes the date input and todays date, calculates difference as a
timedelta then output the years"""
date_input = user_date()
today = date.today()
delta = today - date_input
print(int(delta.days // 365.25))
