# import time
# import os
#
# countdown = 60
#
# if os.stat("time_left.txt").st_size != 0:
#     save_rest = open("time_left.txt", "r")
#     countdown = int(save_rest.readline())
#
# try:
#     for i in range(countdown):
#         print(countdown)
#         countdown -= 1
#         time.sleep(60)
#
#     print("")
#     print("You're done")
#     delete_rest = open("time_left.txt", "w")
#     delete_rest.truncate()
#
# except KeyboardInterrupt:
#     countdown += 1
#     print("")
#     print(f"You still have {countdown} minutes to go")
#     save_rest = open("time_left.txt", "w")
#     save_rest.write(str(countdown))
#     save_rest.close()

import unittest.

