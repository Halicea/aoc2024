from dataclasses import dataclass, field

f = open(__import__("sys").argv[1])
instr = f.read().splitlines()


@dataclass
class P:
    x: int = 0
    y: int = 0

    cost: int = 0


@dataclass
class Machine:
    a: P = field(default_factory=P)
    b: P = field(default_factory=P)
    price: P = field(default_factory=P)
    solution: P | None = field(default_factory=P)

    def x(self):
        return (self.a.x, self.b.x, self.price.x)

    def y(self):
        return (self.a.y, self.b.y, self.price.y)


def solve(ba, bb, prize):
    solutions = []
    prize = prize
    r1 = min(prize // ba + 1, 100)
    r2 = min(prize // bb + 1, 100)

    for i in range(r1):
        for j in range(r2):
            if (i * ba) + (j * bb) == prize:
                cost = i * 3 + j
                solutions.append(P(i, j, cost))
    return solutions


def solve2(m: Machine) -> P | None:
    ax = m.a.x
    bx = m.b.x
    ay = m.a.y
    by = m.b.y
    x = m.price.x + 10000000000000
    y = m.price.y + 10000000000000

    i = (bx * y - by * x) / (ay * bx - by * ax)
    j = (x - ax * i) / bx
    cost = i * 3 + j
    i, j, cost = int(i), int(j), int(cost)
    if i * ax + j * bx == x:
        return P(i, j, cost)
    return None


def ln2pt(line: str):
    return P(
        *[
            int(x)
            for x in line.replace("Button A: ", "")
            .replace("Button B: ", "")
            .replace("Prize: ", "")
            .replace("X=", "")
            .replace("Y=", "")
            .replace("X", "")
            .replace("Y", "")
            .strip()
            .split(",")
        ]
    )


machines = []
for i in range(0, len(instr), 4):
    if not instr[i]:
        continue
    m = Machine(ln2pt(instr[i]), ln2pt(instr[i + 1]), ln2pt(instr[i + 2]))
    m.solution = solve2(m)
    if m.solution:
        machines.append(m)

p1 = sum([m.solution.cost for m in machines if m.solution])
print("p1", p1)
