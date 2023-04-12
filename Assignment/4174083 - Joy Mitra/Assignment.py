
import datetime as d
Birthday_input = input("Enter:year-month-day=")
Birthday = "2003-02-04"


my_Birthday = d.datetime.now().strftime(Birthday)


if Birthday_input == my_Birthday:
    print("Happy birthday Joy")
else:
    print("Have a nice day.Thanks for enter something")
"""
import BIRTHDAY as B
Input_My_Birthday = input("Enter:year-month-day=")
my_Birthday = B.MY_BIRTHDAY

if Input_My_Birthday == my_Birthday:
    print("Happy Birthday")
else:
    print("Sorry sir i don't solve this Strptime format")
"""