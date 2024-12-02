instr = open(f"{__file__[:-3]}.txt").read().split("\n")[:-1]
# instr = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# """.split("\n")[:-1]
input = [[int(y) for y in x.split()] for x in instr]
p1 = None

def analyze(inp):
    if len(inp) <= 2: 
        return True
    inc=inp[0] < inp[1]
    for i in range(len(inp)-1):
        if abs(inp[i] - inp[i+1]) > 3 or inp[i] == inp[i+1]:
            return False
        if inc:
            if inp[i] > inp[i+1] :
                return False
        else:
            if inp[i] < inp[i+1]:
                return False
    return True

def run( tolerate = False):
    count = 0
    for inp in input:
        ok = analyze(inp)
        if ok:
            count += 1
            continue

        if not tolerate:
            continue

        for i in range(len(inp)):
            inpa = [inp[j] for j in range(len(inp)) if i != j]
            ok = analyze(inpa)
            if ok: 
                count += 1
                break
    return count

p1 = run()
print("p1", p1)

p2 = run(True)
print("p2", p2)
