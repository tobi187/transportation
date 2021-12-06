with open("lulzi.txt", "r") as file:
    data = file.read()

data = data.split("\n\n")

bingo_input = data[0].split(",")
data.pop(0)

data = [i.split("\n") for i in data]

print(data, bingo_input)