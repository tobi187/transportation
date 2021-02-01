from datetime import date
import json
import sys

# days = [{
#     "key": 1,
#     "date": "2021-26-1",
#     "time_coded": 1,
#     "time_videos": 1,
#     },
#     {
#         "key": 2,
#         "date": "2021-27-1",
#         "time_coded": 1,
#         "time_videos": 1,
#     },
#     {
#         "key": 3,
#         "date": "2021-26-1",
#         "time_coded": 1,
#         "time_videos": 1,
#     },
# {
#         "key": 4,
#         "date": "2021-26-1",
#         "time_coded": 1,
#         "time_videos": 1,
#     },
# {
#         "key": 5,
#         "date": "2021-26-1",
#         "time_coded": 1,
#         "time_videos": 1,
#     },
# {
#         "key": 6,
#         "date": "2021-26-1",
#         "time_coded": 1,
#         "time_videos": 1,
#     }
# ]

with open("test.txt", "r") as fr:
    days = json.load(fr)


new_item = {
    "key": days[-1]["key"] + 1,
    "date": str(date.today())
}


def is_unique(item, item_list):
    for i in item_list:
        if item["date"] == i["date"]:
            return False

    return True


if not is_unique(new_item, days):
    print("No 2nd chances")
    exit()

time_coded = input("How long did you code today(in h)? ")
time_videos = input("How long have you watched (coding)videos today(in h)? ")

new_item["time_coded"] = time_coded
new_item["time_videos"] = time_videos

days.append(new_item)

with open("test.txt", "w") as fw:
    json.dump(days, fw)

