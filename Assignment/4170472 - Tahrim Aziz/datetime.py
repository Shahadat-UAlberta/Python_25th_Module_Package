from datetime import datetime



pre_define = "12-02-22"



input_date = input("Enter a date (dd-mm-yy): ")



pre_define_dt = datetime.strptime(pre_define, '%d-%m-%y')
input_date_dt = datetime.strptime(input_date, '%d-%m-%y')



if input_date_dt == pre_define_dt:
    print("Happy birthday!!!")
else:
    print("Sorry, ur not the birthday person")
