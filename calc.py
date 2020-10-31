import time

seconds = 0
minutes = 0
hours = 0

while True:  # goes on forever
    for m in range(60):  # minutes loop
        for s in range(60):  # seconds loop
            seconds = seconds + 1  # every loop add 1 second to seconds counter
            time.sleep(1)  # wait 1 second (so that our seconds counter is correct)
            print(hours, minutes, seconds)  # print out the counter
        minutes = minutes + 1  # after the 60 loops of the seconds loop (which is 60 seconds) add increment minute
        seconds = 0  # reset seconds counter (so it doesn't go above 60)
    hours = hours + 1  # after minutes has looped 60 times which means that seconds looped 60 * 60 times increment hours
    minutes = 0  # reset minutes so it doesn't go above 60
