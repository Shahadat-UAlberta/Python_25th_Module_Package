import datetime

_Birth_date = datetime.date(2010,3,21)
print("You must have (date,month,year) format to wish Arafat")
print("Write the date,month and year below line to verify it")
try:
    date_str = input(" Enter the birth date of Arafat in (date,month,year) format:-")
    date,month,year= map(int,date_str.split(","))
    _user_date = datetime.date(year,month,date)
    if _user_date == _Birth_date  :
        print("Happy Birthday Arafat!")
    else:
        print("Sorry.But today is not my birthday user")
except ValueError:
    print("Invalid date format. Please use (date, month, year) format. ")









