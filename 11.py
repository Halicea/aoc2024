instr = [int(x) for x in open(__import__("sys").argv[1]).read().strip().split(" ")]

def blinker(stone, times, memo={}):
    key = (stone, times)
    if key not in memo:
        if times == 1:
            memo[key] = len(blink(stone))
        else:
            memo[key] = sum([blinker(stone, times - 1, memo) for stone in blink(stone)])
    return memo[key]


def blink(stone):
    if stone == 0:
        return [1]
    strstone = str(stone)
    if len(strstone) % 2 == 0:
        stlen = len(strstone) // 2
        return [int(strstone[:stlen]), int(strstone[stlen:])]
    return [2024 * stone]


print("p1", sum([blinker(stone, 25) for stone in instr]))
print("p2", sum([blinker(stone, 75) for stone in instr]))
