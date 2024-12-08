from itertools import combinations

fname = __import__("sys").argv[1]
instr = [[x for x in line] for line in open(fname).read().splitlines()]
frequencies = {}
antidotes = {}


def is_aob(pos):
    i, j = pos
    return i < 0 or j < 0 or i >= len(instr) or j >= len(instr[i])


for i in range(len(instr)):
    for j in range(len(instr[i])):
        if instr[i][j] != ".":
            freq = instr[i][j]
            if freq not in frequencies:
                frequencies[freq] = []
            frequencies[freq].append((i, j))

for freq in frequencies:
    for comb in list(combinations(frequencies[freq], 2)):
        i1, j1 = comb[0]
        i2, j2 = comb[1]
        delta = (i1 - i2, j1 - j2)
        a1 = (i1 + delta[0], j1 + delta[1])
        if comb[0] not in antidotes:
            antidotes[comb[0]] = []
        antidotes[comb[0]].append(freq)
        if comb[1] not in antidotes:
            antidotes[comb[1]] = []
        antidotes[comb[1]].append(freq)

        while not is_aob(a1):
            if a1 not in antidotes:
                antidotes[a1] = []
            antidotes[a1].append(freq)
            a1 = (a1[0] + delta[0], a1[1] + delta[1])
        a2 = (i2 - delta[0], j2 - delta[1])
        while not is_aob(a2):
            if a2 not in antidotes:
                antidotes[a2] = []
            antidotes[a2].append(freq)
            a2 = (a2[0] - delta[0], a2[1] - delta[1])
print(len(antidotes))
