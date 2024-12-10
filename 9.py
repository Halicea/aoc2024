instr = open(__import__("sys").argv[1]).read()[:-1]

disk = []
for i, c in enumerate(instr):
    c = int(c)
    if i % 2 == 0:
        for j in range(c):
            disk.append(str(i // 2))
    else:
        for j in range(c):
            disk.append(".")

j = 0
for i in range(len(disk) - 1, -1, -1):
    if disk[i] == ".":
        continue
    else:
        while disk[j] != "." and j < i:
            j += 1
        if j < i:
            disk[j] = disk[i]
            disk[i] = "."
        else:
            break
p1 = 0
for i, c in enumerate(disk):
    if c == ".":
        break
    p1 += i * int(c)
print("p1", p1)
