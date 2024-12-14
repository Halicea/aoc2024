from dataclasses import dataclass


f = open(__import__("sys").argv[1])


@dataclass
class P:
    x: int = 0
    y: int = 0


@dataclass
class Robot:
    p: P
    v: P


def pmap(tpl):
    p = [int(x) for x in tpl[0].split(",")]
    v = [int(x) for x in tpl[1].split(",")]
    return Robot(P(*p), P(*v))

space = P(101, 103)
quads = [
    [P(-1, -1), P(space.x // 2, space.y // 2)],
    [P(space.x // 2, -1), P(space.x, space.y // 2)],
    [P(-1, space.y // 2), P(space.x // 2, space.y)],
    [P(space.x // 2, space.y // 2), P(space.x, space.y)]]

def in_quad(p, q):
    return q[0].x < p.x < q[1].x and q[0].y < p.y < q[1].y


def pp(*points):
    for i in range(space.y):
        for j in range(space.x):
            c = len([x for x in points if x == P(j, i)])
            if c > 0:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print()


robots = [
    pmap(x.replace("p=", "").replace("v=", "").split(" "))
    for x in f.read().splitlines()
]
def pt():
    pp(*[x.p for x in robots])

print("Initial state:")
seconds = 10000
pt()
for i in range(seconds):
    for r in robots:
        x = r.v.x + r.p.x
        y = r.v.y + r.p.y
        if x < 0:
            x = space.x + x
        elif x >= space.x:
            x = x - space.x
        if y < 0:
            y = space.y + y
        elif y >= space.y:
            y = y - space.y
        r.p = P(x, y)
    

    colision = False
    for r in robots:
        if len([x for x in robots if x.p == r.p]) > 1:
            colision = True
            break
    if not colision:
        print("After", i + 1, "seconds:")
        pt()
qcount = [0, 0, 0, 0]
for r in robots:
    for i, q in enumerate(quads):
        if in_quad(r.p, q):
            qcount[i] += 1
print(qcount)
p1 = 1
for x in qcount:
    p1 *= x
print("p1", p1)

