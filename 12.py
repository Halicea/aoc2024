from itertools import combinations

f = open(__import__("sys").argv[1])
instr = [x for x in f.read().splitlines()]

positions = [(i, j) for i, row in enumerate(instr) for j, _ in enumerate(row)]


def val(pos):
    i, j = pos
    return instr[i][j]


def eqval(pos1, pos2):
    return val(pos1) == val(pos2)


def neighbors(pos, region):
    i, j = pos
    return [x for x in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)] if x in region]


def get_region(start, region=[]):
    i, j = start
    region += [start]
    positions.remove((i, j))
    nbrs = [n for n in neighbors(start, positions) if eqval(start, n)]
    for n in nbrs:
        if n not in region:
            region = get_region(n, region)
    return region


def is_concave_edge(pos, region):
    nbr = neighbors(pos, region)
    nbr_pairs = [
        (n1, n2) for n1, n2 in combinations(nbr, 2) if n1[0] != n2[0] and n1[1] != n2[1]
    ]
    edges = 0
    for n1, n2 in nbr_pairs:
        if n1[0] != pos[0]:
            if (n1[0], n2[1]) not in region:
                edges += 1
        else:
            if (n2[0], n1[1]) not in region:
                edges += 1
    return edges


def is_convex_edge(pos, region):
    nbr = neighbors(pos, region)
    nbrlen = len(nbr)
    if nbrlen == 0:
        return 4
    if nbrlen == 1:
        return 2
    if nbrlen == 2:
        if nbr[0][0] == nbr[1][0] or nbr[0][1] == nbr[1][1]:
            return 0
        else:
            return 1
    else:
        return 0


def print_region(region):
    for i, row in enumerate(instr):
        for j, _ in enumerate(row):
            if (i, j) in region:
                print(val((i, j)), end="")
            else:
                print(".", end="")
        print()
    print()


p1 = 0
p2 = 0
while positions:
    v = val(positions[0])
    pp = positions[0]
    if pp == (4,7):
        print("here", v)
    reg = get_region(positions[0], region=[])
    if v == ".":
        continue
    # reg = [x for x in reg if len(neighbors(x, reg))]
    reg_fence = 0
    sides = 0
    for pos in reg:
        reg_fence += 4 - len([x for x in neighbors(pos, reg)])
        convex = is_convex_edge(pos, reg)
        concave = is_concave_edge(pos, reg)
        # if convex + concave:
        #     print("edge", pos, convex + concave)
        sides += convex + concave
    # print_region(reg)
    # print(v, pp, f"{len(reg)} * {sides} = {len(reg) * sides}")
    # print_region(reg)
    p1 += len(reg) * reg_fence
    p2 += len(reg) * sides
    # print(v, reg_fence)
    # print()

print("p1", p1)
print("p2", p2)
