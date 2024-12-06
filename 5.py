from typing import List

instr = open(__file__[:-3]).read().splitlines()

constrains: List[List[str]] = []
updates: List[List[str]] = []
i = 0
for i in range(len(instr)):
    if instr[i] == "":
        break
    constrains.append(instr[i].split("|"))
i += 1
for j in range(i, len(instr)):
    line = instr[j]
    if not line.startswith("#"):
        updates.append(line.split(","))

valid = []
fixed = []
p1 = 0
p2 = 0
for update in updates:
    was_faulty = False
    i = 0
    while i < len(update):
        item = update[i]
        issues = [c[1] for c in constrains if c[0] == item and c[1] in update[:i]]
        faulty = [x for x in update[:i] if x in issues]
        minidx = 0
        if faulty:
            was_faulty = True
            minidx = min([update.index(f) for f in faulty])
            update.pop(i)
            update.insert(minidx, item)
            constraints = [c[1] for c in constrains if c[0] == item]
            faulty = [x for x in update[:i] if x in constraints]
            was_faulty += 1
            i = minidx
        i += 1

    if not was_faulty:
        p1 += int(update[len(update) // 2])
        valid.append(update)
    else:
        p2 += int(update[len(update) // 2])
        fixed.append(update)
print("p1", p1)
print("p2", p2)
