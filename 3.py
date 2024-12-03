import re

instr = open(f"{__file__[:-3]}.txt").read()
pattern = r"(mul\(\d{1,3},\d{1,3}\))|do\(\)|don\'t\(\)"
sum = 0
domul = True
for match in re.finditer(pattern, instr):
    pat = instr[match.start() : match.end()]
    if pat.startswith("mul") and domul:
        patt = instr[match.start() + 4 : match.end() - 1]
        nums = [int(x) for x in patt.split(",")]
        sum += nums[0] * nums[1]
    elif pat.startswith("do("):
        domul = True
    elif pat.startswith("don"):
        domul = False
print(sum)
