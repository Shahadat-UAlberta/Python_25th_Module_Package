import datetime as d
Birthday = "2003-02-04 07:44:44"
BirthdayFormat = "%Y-%m-%d %H:%M:%S"

MY_BIRTHDAY = d.datetime.strptime(Birthday, BirthdayFormat)
print(MY_BIRTHDAY)