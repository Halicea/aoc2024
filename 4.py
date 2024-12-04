instr = [x[:-1] for x in open(f"{__file__[:-3]}.txt").readlines()]

word = "XMAS"
p1 = 0
for i in range(len(instr)):
    line = instr[i]
    for j in range(len(line)):
        char = line[j]
        if not char == word[0]:
            continue
        xcount = 0

        vlinedown = "".join([x[j] for x in instr[i:]])
        vlineup = "".join([x[j] for x in instr[i::-1]])

        if line[j:].startswith(word):
            xcount += 1
        if line[j::-1].startswith(word):
            xcount += 1
        if vlineup.startswith(word):
            xcount += 1
        if vlinedown.startswith(word):
            xcount += 1
        if i + len(word) <= len(instr) and j + len(word) <= len(line):
            dlinedownright = "".join([instr[i + a][j + a] for a in range(len(word))])
            if dlinedownright.startswith(word):
                xcount += 1
        if i + len(word) <= len(instr) and j + 1 >= len(word):
            dlinedownleft = "".join([instr[i + a][j - a] for a in range(len(word))])
            if dlinedownleft.startswith(word):
                xcount += 1
        if  i + 1 >= len(word) and j + 1 >= len(word):
            dlineupleft = "".join([instr[i - a][j - a] for a in range(len(word))])
            if dlineupleft.startswith(word):
                xcount += 1
        if j+len(word) <= len(line) and i + 1 >= len(word):
            dlineupright = "".join([instr[i- a][j + a] for a in range(len(word))])
            if dlineupright.startswith(word):
                xcount += 1
        p1 += xcount
print("p1", p1)
p2 = 0
for i in range(len(instr)):
    line = instr[i]
    for j in range(len(line)):
        char = line[j]
        if not char == 'A':
            continue

        if i > 0 and j > 0 and i<len(instr)-1 and j<len(line)-1:
            left =  instr[i-1][j-1] == 'M' and instr[i+1][j+1] == 'S' or instr[i-1][j-1] == 'S' and instr[i+1][j+1] == 'M'
            right = instr[i-1][j+1] == 'M' and instr[i+1][j-1] == 'S' or instr[i-1][j+1] == 'S' and instr[i+1][j-1] == 'M'
            if left and right:
                p2 += 1

print('p2', p2)
