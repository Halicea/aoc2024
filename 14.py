from dataclasses import dataclass


instr = open(__import__("sys").argv[1]).read().splitlines()


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


def in_quad(p, q):
    top_left, bottom_right = q
    return top_left.x < p.x < bottom_right.x and top_left.y < p.y < bottom_right.y


robots = [pmap(x.replace("p=", "").replace("v=", "").split(" ")) for x in instr]
space = P(101, 103)
quads = [
    (P(-1, -1), P(space.x // 2, space.y // 2)),
    (P(space.x // 2, -1), P(space.x, space.y // 2)),
    (P(-1, space.y // 2), P(space.x // 2, space.y)),
    (P(space.x // 2, space.y // 2), P(space.x, space.y)),
]
seconds = 100000
p1 = 0
p2 = 0
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
        p2 = i + 1
        if p1:
            break

    if i == 99:
        qcount = [0, 0, 0, 0]
        for r in robots:
            for i, q in enumerate(quads):
                if in_quad(r.p, q):
                    qcount[i] += 1
        p1 = 1
        for x in qcount:
            p1 *= x
        if p2:
            break

print("p1", p1)
print("p2", p2)
