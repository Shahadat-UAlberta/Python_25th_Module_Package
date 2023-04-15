import datetime as d

Today = d.date.today().strftime("%d-%m")
print("NOTE: INPUT FORMAT = DATE-MONTH")
Birthday = input("PLEASE ENTER YOUR BIRTHDAY DATE: ")
if Today == Birthday:
    print("WISH YOU A HAPPY BIRTHDAY!")
elif Today != Birthday:
    print("SORRY, TODAY IS NOT YOUR BIRTHDAY")
