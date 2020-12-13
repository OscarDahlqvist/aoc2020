import re
import json
import itertools

f = open("input.txt","r").read()

rx = re.sub(r"\n", r'",\n"', f)
rx = '[\n\"'+rx+'\"\n]'

inp = json.loads(rx)

def rot(str, angle):
    if angle == 270:
        if str == "N": return "E"
        if str == "E": return "S"
        if str == "S": return "W"
        if str == "W": return "N"
    elif angle == 180:
        if str == "N": return "S"
        if str == "E": return "W"
        if str == "S": return "N"
        if str == "W": return "E"
    elif angle == 90:
        if str == "N": return "W"
        if str == "E": return "N"
        if str == "S": return "E"
        if str == "W": return "S"
    else:
        print(f"error for angle={angle}")
        exit()

facing = "E"
e = 0
n = 0
for c in inp:
    dir = c[0]
    arg = int(c[1:])

    if dir == "N":
        n += arg
    if dir == "S":
        n -= arg
    if dir == "E":
        e += arg
    if dir == "W":
        e -= arg
    if dir == "L":
        facing = rot(facing, arg)
    if dir == "R":
        facing = rot(facing, 360-arg)
    if dir == "F":
        if facing == "N": n += arg
        if facing == "S": n -= arg
        if facing == "E": e += arg
        if facing == "W": e -= arg
    print(f"{c}\t => ({e},{n}), facing:{facing}")
print(abs(e)+abs(n))
