import time
import datetime

current_time = datetime.datetime.today()

day = current_time.day
mount = current_time.month
max_mounts = 12
max_days_of_the_mount = 31
print(day, mount)
def reminder():
    user_input_date1 = int(input('Choose the mount to change password: '))
    user_input_date2 = int(input('Choose the day of the mount to change password: '))
    if user_input_date1 > max_mounts:
        print('Wrong mount number\nChoose between 1 and 12!')
    if user_input_date2 > max_days_of_the_mount:
        print('Wrong date\nChoose between 1 and 31!')




