import time

seconds = 0
minutes = 0
hours = 0

while True:  # loop that goes on forever
    time.sleep(1)  # print sleep one second so timer is correct
    seconds = seconds + 1  # increment seconds by one
    if seconds == 60:  # check if seconds is = 60 if yes:
        seconds = 0  # reset seconds so it doesn't go above 60
        minutes = minutes + 1  # increment minutes
    if minutes == 60:  # check if minutes are 60 if yes:
        minutes = 0  # reset minutes so it doesn't go above 60
        hours = hours + 1 # increment hours
    print(hours, minutes, seconds)  # print out everything, the loop restarts
