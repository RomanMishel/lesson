import time
import datetime

current_time = datetime.datetime.today()

day = current_time.day
mount = current_time.month

print(day, mount)
def reminder():
    user_inpur_date1 = int(input('Choose the mount to change password: '))
    user_inpur_date2 = int(input('Choose the day of the mount to change password: '))
        if user_inpur_date1 > 12:
            print('Wrong mount number\nChoose between 1 and 12')



