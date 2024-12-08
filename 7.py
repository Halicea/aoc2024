from itertools import product

fname = __import__("sys").argv[1]
instr = [line for line in open(fname).read().splitlines()]

def mul(x, y): return x * y
def add(x, y): return x + y
def concat(x, y): return int(str(x) + str(y))

ops = [mul, add, concat]
p1 = 0

for line in instr:
    res, rest = line.split(":")
    res = int(res)
    parts = [int(x) for x in rest.split(" ") if x != ""]
    operators = product(ops, repeat=len(parts) - 1)
    ok = False
    exp = None
    for opcombination in operators:
        cur = parts[0]
        for i in range(1, len(parts)):
            op = opcombination[i - 1]
            opstr = "+" if op.__name__ == "add" else "*"
            right = parts[i]
            cur = op(cur, right)
            if cur > res:
                break
        if cur == res:
            ok = True
            break
    if ok:
        p1+=res

print("p1", p1)

