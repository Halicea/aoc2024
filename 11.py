f = open(__import__("sys").argv[1])
stones = [int(x) for x in f.read().strip().split(" ")]

def blink(stone):
    if stone == 0:
        return [1]
    strstone = str(stone)
    is_even, half_len = len(strstone) % 2 == 0, len(strstone) // 2
    if is_even:
        return [int(strstone[:half_len]), int(strstone[half_len:])]
    return [2024 * stone]

def blinker(stone, times, memo={}):
    key = (stone, times)
    if key not in memo:
        if times == 1:
            memo[key] = len(blink(stone))
        else:
            memo[key] = sum([blinker(stone, times - 1, memo) for stone in blink(stone)])
    return memo[key]


print("p1", sum([blinker(s, 25) for s in stones]))
print("p2", sum([blinker(s, 75) for s in stones]))
