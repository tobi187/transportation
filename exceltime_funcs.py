import datetime

print(datetime.datetime(year=2021, month=8, day=23).weekday())

# weekday -> mo = 0, so = 6

for i in range(10):
    if i == 3:
        i += 4
    print(i)