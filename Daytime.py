import datetime
import time


def myclock():
    current_time = datetime.datetime.today()
    myhour = current_time.hour
    myminute = current_time.minute
    mysecs = current_time.second

    print(f'time now is {myhour}:{myminute}:{mysecs}')

while True:
    myclock()
    time.sleep(1)


myclock()