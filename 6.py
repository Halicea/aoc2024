import sys

instr = [[x for x in line] for line in open(sys.argv[1]).read().splitlines()]
dt = {"^": ">", ">": "v", "v": "<", "<": "^"}
dv = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

loops = []
def experiment(pos, d, visited={}, obstacle=None):
    start = pos
    start_d = d
    while not is_oob(pos):
        next, nextv = get_next(pos, d)
        while nextv == "#" or (obstacle is not None and next == obstacle):
            d = dt[d]
            next, nextv = get_next(pos, d)

        if not is_oob(next) and obstacle is None:
            _, is_loop = experiment(start, start_d, {}, next)
            if is_loop and next not in loops:
                loops.append(next)
        if pos in visited:
            if d in visited[pos]:
                return visited, True
            else:
                visited[pos].append(d)
        else:
            visited[pos] = [d,]
        pos = next
    return visited, False

def get_start():
    for i, line in enumerate(instr):
        for j, chr in enumerate(line):
            if chr in dv.keys():
                d = chr
                pos = (i, j)
                return pos, d
    raise Exception("No start found")

def is_oob(pos):
    return pos[0] >= len(instr) or pos[1] >= len(instr[0]) or pos[0] < 0 or pos[1] < 0


def get_next(pos, d):
    next_pos = tuple([x + y for x, y in zip(pos, dv[d])])
    if is_oob(next_pos):
        return next_pos, None
    i, j = next_pos
    next_val = instr[i][j]
    return next_pos, next_val

def pp(visited=None, pos=None, d=None, obstacle=None):
    for i, line in enumerate(instr):
        for j, chr in enumerate(line):
            if (i, j) == pos:
                print(d, end="")
            elif visited and (i, j) in visited:
                print(visited[(i, j)][-1], end="")
            elif obstacle and (i, j) == obstacle:
                print("O", end="")
            else:
                print(chr, end="")
        print()
    print("---------------")
pos, d = get_start()
visited, _ = experiment(pos, d)
print(visited)
print("p1", len(visited))
print("p2", len(loops))
print("p2-unique", len(set(loops)))
