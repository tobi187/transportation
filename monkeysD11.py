import sys
sys.set_int_max_str_digits(999999)

class Monkey:
    def __init__(self, n, d, op, mt, mf):
        self.num: int = n
        self.divisor: int = d
        self.operation: str = op
        self.mon_true: int = mt
        self.mon_false: int = mf
        self.items = []
        self.inspections = 0

    def test(self, item):
        op = self.operation.replace("old", str(item))
        n = eval(op)  # // 3
        if n % self.divisor == 0:
            return self.mon_true, n
        else:
            return self.mon_false, n

    def do_round(self):
        self.inspections += len(self.items)
        give = [self.test(item) for item in self.items]
        self.items.clear()
        return give

    def accept_item(self, item):
        # self.inspections += 1
        self.items.append(item)


with open("d9data.in", "r") as file:
    data = file.read().split("\n\n")

monkeys: list[Monkey] = []

for i, m in enumerate(data):
    prep = [v.strip() for v in m.split("\n")[1:]]
    monkey = Monkey(
        n=i,
        d=int(prep[2].split()[-1]),
        op=prep[1].split("=")[-1].strip(),
        mt=int(prep[-2].split()[-1]),
        mf=int(prep[-1].split()[-1])
    )
    monkey.items = [int(v) for v in prep[0].split(":")[-1].split(",")]
    monkeys.append(monkey)


for runde in range(1000):
    for m in monkeys:
        r = m.do_round()
        [monkeys[i].accept_item(v) for i, v in r]
    print(runde)
    #[print(m.items) for m in monkeys]
    #print("------------------------")

s = sorted([m.inspections for m in monkeys], reverse=True)

print(s[0] * s[1])
