
"""
-> Imput = 17-12-2003
-> Pre-defind = 17-12-2003

-> If input == pre-defind : "HBD" else "sorry"

"""

import datetime as d

HBD='17-12-2003'
date_user=input("Enter (day-month-year): ")

try:
    HBD_format=d.datetime.strptime(HBD,date_user)
    date_user_format=d.datetime.strptime(date_user,HBD)

    if HBD_format == date_user_format:
        print("My Birthday is",date_user)

    else:
        print("Don't match")

except ValueError as V:
    print(V)
except Exception as e:
    print("You enter wrong")









