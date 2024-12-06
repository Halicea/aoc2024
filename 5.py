instr = open(__file__[:-3]).read().splitlines()
constrains: list[list[str]]= [x.split("|") for x in instr[:instr.index("")]]
updates: list[list[str]] = [x.split(",") for x in instr[instr.index("")+1:]]
valid = fixed = []
p1 = p2 = 0
for update in updates:
    was_faulty = False
    i = 0
    while i < len(update):
        issues = [c[1] for c in constrains if c[0] == update[i] and c[1] in update[:i]]
        faulty = [x for x in update[:i] if x in issues]
        minidx = 0
        if faulty:
            was_faulty = True
            minidx = min([update.index(f) for f in faulty])
            item = update.pop(i)
            update.insert(minidx, item)

            constraints = [c[1] for c in constrains if c[0] == item]
            faulty = [x for x in update[:i] if x in constraints]

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
