f = open(__import__("sys").argv[1])
input = f.read().split("\n")[:-1]
input = [[int(j) for j in i.split()] for i in input]

left = sorted([x[0] for x in input])
right = sorted([x[1] for x in input])

# p1
p1 = sum([abs(left[i] - right[i]) for i in range(len(left))])
print("p1", p1)

# p2
p2 = 0
current = 0
while len(left) > 0 and len(right) > 0:
    lp, rp = left[0], right[0]
    if lp >= rp:
        right.pop(0)
        if lp == rp:
            current += lp
    else:
        cp = left[0]
        while cp == lp:
            left.pop(0)
            p2 += current
            if len(left) == 0:
                break
            cp = left[0]
        current = 0

print("p2", p2)
