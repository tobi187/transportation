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


def get_item(item_list, print_one_category=""):
    for i in item_list:
        # if print_one_day:
        #    if print_one_day == item_list[i]["date"]:
        #        print(i)
        if print_one_category:
            if print_one_category == "key":
                print(days[i]["key"])
            elif print_one_category == "date":
                print(item_list[i]["date"])
            elif print_one_category == "time_coded":
                print(item_list[i]["time_coded"])
            elif print_one_category == "time_videos":
                print(item_list[i]["videos_watched"])
        else:
            print(i)


# cmd_line_args = {
#     "-s": days[0]["date"],
#     "-g": get_item(days, sys.argv[2])
# }


# if f_argument == "-s":
#     print(days[0]["date"])
#     exit()
# elif f_argument == "-g":
#     get_item(days)
#     exit()


# for i in cmd_line_args:
#     if f_argument == i:
#         print(cmd_line_args[i])
#         exit()

# gen new item and update the list
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

if sys.argv[1] and sys.argv[1] == "-a" or "--add":
    if sys.argv[2] == "-n":
        for i in days:
            if i["date"] == str(date.today()):
                i["note"] = []
                for j in range(int(sys.argv[3])):
                    note = input("note: ")
                    i["note"].append(note)
            elif sys.argv[3] == i["date"]:
                if "note" not in i:
                    i["note"] = []
                for h in range(int(sys.argv[4])):
                    note = input("note: ")
                    i["note"].append(note)


time_coded = int(input("How long did you code today(in h)? "))
time_videos = int(input("How long have you watched (coding)videos today(in h)? "))

new_item["time_coded"] = time_coded
new_item["time_videos"] = time_videos

days.append(new_item)

with open("test.txt", "w") as fw:
    json.dump(days, fw)

