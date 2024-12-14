from dataclasses import dataclass, field

f = open(__import__("sys").argv[1])
instr = f.read().splitlines()


@dataclass
class P:
    x: int = 0
    y: int = 0


@dataclass
class Machine:
    a: P = field(default_factory=P)
    b: P = field(default_factory=P)
    price: P = field(default_factory=P)


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

machines = [Machine(ln2pt(instr[i]), ln2pt(instr[i + 1]), ln2pt(instr[i + 2])) 
    for i in range(0, len(instr), 4) if instr[i]]

def solve2(m: Machine, increase=0) -> int:
    x = m.price.x + increase
    y = m.price.y + increase

    i = (m.b.x * y - m.b.y * x) / (m.a.y * m.b.x - m.b.y * m.a.x)
    j = (x - m.a.x * i) / m.b.x
    cost = i * 3 + j
    i, j, cost = int(i), int(j), int(cost)
    if i * m.a.x + j * m.b.x == x:
        return cost
    return 0


p1 = sum(map(lambda m: solve2(m, 100), machines))
p2 = sum(map(lambda m: solve2(m), machines))
print("p1", p1)
print("p2", p2)
