instr = [
    [-1 if x == "." else int(x) for x in line[:-1]]
    for line in open(__import__("sys").argv[1]).readlines()
]


def is_oob(pos):
    i, j = pos
    return i < 0 or j < 0 or i >= len(instr) or j >= len(instr[0])


def find_trails(trail: list[tuple[int, int]]) -> list[list[tuple[int, int]]]:
    i, j = trail[-1]
    num = instr[i][j]
    if num == 9:
        return [trail]
    results: list[list[tuple[int, int]]] = []
    for neighb in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        di, dj = neighb
        if not is_oob(neighb) and instr[di][dj] == num + 1:
            res = find_trails(trail + [neighb])
            for r in res:
                if not r:
                    continue
                endi, endj = r[-1]
                if instr[endi][endj] == 9:
                    results.append(r)
    return results


starting = []
for i, row in enumerate(instr):
    for j, pos in enumerate(row):
        if pos == 0:
            starting.append((i, j))

p1 = 0
p2 = 0
for x in starting:
    endings = {}
    trails = find_trails([x])
    p2 += len(trails)
    for y in find_trails([x]):
        if y[-1] not in endings:
            endings[y[-1]] = []
        endings[y[-1]].append(y)
    p1 += len(endings)

print("p1", p1)
print("p2", p2)
