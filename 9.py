instr = open(__import__("sys").argv[1]).read()[:-1]
disk = []

EMPTY = "X"
DATA = "D"


def is_data(i):
    if i < 0 or i >= len(disk):
        return False
    return disk[i][0] == DATA


def is_empty(i):
    if i < 0 or i >= len(disk):
        return False
    return disk[i][0] == EMPTY


for i, c in enumerate(instr):
    c = int(c)
    if i % 2 == 0 and c > 0:
        disk.append((DATA, c, i // 2))
    elif c > 0:
        disk.append((EMPTY, c))


def compact(disk):
    i = len(disk) - 1
    while i >= 0:
        kind = disk[i][0]
        size = disk[i][1]
        id = None
        if kind == DATA:
            id = disk[i][2]
        else:
            i -= 1
            continue
        j = 0
        while j < i:
            jkind = disk[j][0]
            jsize = disk[j][1]
            if jkind == EMPTY and jsize >= size:
                disk[j] = (DATA, size, id)

                left = None
                right = None
                if is_empty(i+1): 
                    right = disk[i+1]
                if is_empty(i-1): 
                    left = disk[i-1]

                middle = (EMPTY, size)
                if right:
                    middle = (EMPTY, middle[1] + right[1])
                if left:
                    middle = (EMPTY, middle[1] + left[1])

                disk[i] = middle

                if jsize > size:
                    disk.insert(j + 1, (EMPTY, jsize - size))
                    i +=1

                if right:
                    disk.pop(i+1)
                if left:
                    disk.pop(i-1)

                dp(disk)
                break
            j += 1
        i -= 1


def dp(disk, should_print=False):
    i = 0
    sum = 0
    for t in disk:
        if t[0] == "X":
            for _ in range(t[1]):
                if should_print:
                    print(".", end="")
                i += 1
        else:
            for _ in range(t[1]):
                if should_print:
                    print(t[2], end="")
                sum += i * t[2]
                i += 1
    return sum

dp(disk)
compact(disk)
p2 = dp(disk)
print(p2)
