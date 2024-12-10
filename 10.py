instr = [[int(x) for x in line[:-1]] for line in open(__import__("sys").argv[1]).readlines()]
print(instr)
