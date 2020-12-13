import re
import json
import itertools

f = open("input.txt","r").read()

rx = re.sub(r"\n", r'",\n"', f)
rx = '[\n\"'+rx+'\"\n]'

inp = json.loads(rx)

relE = 10
relN = 1
boatE = 0
boatN = 0
for c in inp:
    dir = c[0]
    arg = int(c[1:])

    if dir == "N":
        relN += arg
    if dir == "S":
        relN -= arg
    if dir == "E":
        relE += arg
    if dir == "W":
        relE -= arg
    if dir in ["L","R"]:
        angle = arg
        if dir == "R":
            angle = 360-angle
            
        if angle == 90:
            oldE = relE
            oldN = relN
            relE = -oldN
            relN = oldE
        if angle == 180:
            relE *= -1
            relN *= -1
        if angle == 270:
            oldE = relE
            oldN = relN
            relE = oldN
            relN = -oldE
        
    if dir == "F":
        for i in range(0,arg):
            boatE += relE
            boatN += relN
        
    print(f"{c}\t => pos:({boatE},{boatN}) target:({relE},{relN})")
print(abs(boatE)+abs(boatN))
