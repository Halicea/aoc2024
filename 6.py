fname = f"{__file__[:-3]}"
instr = [[x for x in line] for line in open(fname).read().splitlines()]
pos = (0, 0)
d = "^"
dv = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
dt= {"^": ">", ">": "v", "v": "<", "<": "^"}
p1 = 0
def add(a, b):
    return tuple([x+y for x, y in zip(a, b)])

for i, line in enumerate(instr):
    for j, chr in enumerate(line):
        if chr in dv.keys():
            d = chr
            pos = (i, j)
            instr[i][j] = "X"
while True: 
    next = add(pos, dv[d])
    if next[0] >= len(instr) or next[1] >= len(instr[0]) \
       or next[0] < 0 or next[1] < 0:
        break

    if instr[next[0]][next[1]] == "#":
        d = dt[d]
    else:
        if instr[next[0]][next[1]] == ".":
            p1 += 1
        pos = next
        instr[pos[0]][pos[1]] = "X"
print("p1", p1+1)
