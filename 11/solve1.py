import re
import json
import itertools

f = open("input.txt","r").read()

rx = re.sub(r"\n", r'",\n"', f)
rx = '[\n\"'+rx+'\"\n]'

d = json.loads(rx)


def prnt(arr):
    [print("".join(line)) for line in arr]

def sg(arr,y,x):
    if y<0: return ""
    if y>=len(arr): return ""
    if x<0: return ""
    if x>=len(arr[y]): return ""
    return arr[y][x]
    
old = [list(line) for line in d]
next = [list(line) for line in d]

while True:
    
    next = [l.copy() for l in old]
    
    for y,line in enumerate(old):
        for x,char in enumerate(line):

            nocc = 0
            for ay in range(y-1,y+2):
                for ax in range(x-1,x+2):
                    try:
                        if (ay,ax) == (y,x): continue
                        if ay < 0 or ax < 0: continue
                        
                        if old[ay][ax] == "#":
                            nocc+=1
                    except: ""
            
            if char == "L" and nocc == 0:
                next[y][x] = "#"
            if char == "#" and nocc >= 4:
                next[y][x] = "L"
    """print("-"*10)
    prnt(state)
    print("\n")
    prnt(next)"""

    if(next == old): break

    old = [list(line) for line in next]

print("\n")
prnt(next)
nSeat = 0
for line in next:
    for c in line:
        if c == "#":
            nSeat+=1
print(nSeat)
