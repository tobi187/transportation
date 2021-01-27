import time
import os

countdown = 60

if os.stat("time_left.txt").st_size == 0:
    countdown = open("time_left.txt", "r")


try:
    for i in range(countdown):
        time.sleep(1)
        print(countdown)
        countdown = countdown - 1

    print("")
    print("You're done")
    with open("time.txt", "w") as f:
        f.truncate()

except KeyboardInterrupt:
    print("")
    print(f"You still have {countdown} minutes to go")
    with open("time_left.txt", "w") as f:
        f.write(countdown)




