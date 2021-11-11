import itertools

original = ["07R/25L", "07C/25C", "18/36"]
prepared = [7, 25, 7, 25, 18, 36 ]

wind_speed = 10
wind_dir = 266

def get_nearest(direction: int) -> str:
    direction = round(direction / 10)
    nearest = (360, 0) # (difference, runway)  
    for dire in prepared:
        other_dir = abs(36 - dire + direction)
        if other_dir < nearest[0]:
            nearest = (other_dir, dire)
        if abs(direction - dire) < nearest[0]:
            nearest = (abs(direction - dire), dire)
    
    noob = [i.split("/") for i in original]
    nab = list(itertools.chain.from_iterable(noob))
    index = prepared.index(nearest[1])


    return nab[index + 1] if index % 2 == 0 else nab[index - 1]

print(get_nearest(266))