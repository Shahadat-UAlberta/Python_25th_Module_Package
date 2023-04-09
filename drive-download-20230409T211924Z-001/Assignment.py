"""
-> Input - 12-02-22
-> Pre-define = 12-02-22

-> If input == pre-define : "HBD" else "Sorry"
"""

import datetime as d


print(d.datetime.now())
print(d.date.today())

temp = d.date(2019,12,5)
print(temp)

today = d.date.today()

print(today.year)
print(today.month)
print(today.day)

s1 = d.datetime.now().strftime("%m/%d/%Y %H-%M-%S")
print(s1)

s2 = "2020-3-12 10:14:30"
s2Format = "%Y-%m-%d %H:%M:%S"

try:
    parse_date = d.datetime.strptime(s2, s2Format)
    print(parse_date)
    print(type(parse_date))
except Exception as e:
    print("Pattern Issue")
""" 
2020-03-12
Ymd
"""