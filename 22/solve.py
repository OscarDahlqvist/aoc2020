import re
import json
import copy 
import itertools 
import sys

f = open("input.txt").read()

[ply1,ply2] = f.split("\n\n")

ply1 = [int(x) for x in ply1.split("\n")[1:]]
ply2 = [int(x) for x in ply2.split("\n")[1:]]

srcPly1 = copy.deepcopy(ply1)
srcPly2 = copy.deepcopy(ply2)

winner = []

"""
iter = 0
while True:
    c1 = ply1.pop(0)
    c2 = ply2.pop(0)
    if c1 > c2:
        ply1.append(c1)
        ply1.append(c2)    
    elif c2 > c1:
        ply2.append(c2)
        ply2.append(c1)

    if len(ply2) == 0:
        winner = ply1
        break        
    if len(ply1) == 0:
        winner = ply2
        break

ret = 0
for index,x in enumerate(winner):
    ret += x*(len(winner)-index)

print(f"part1: {ret}")"""

# Part 2

ply1 = copy.deepcopy(srcPly1)
ply2 = copy.deepcopy(srcPly2)
winner = []

iter = 0

def combat(p1,p2, setups, depth = 0):
    while True:
        global iter
        iter+=1
        if iter % 10000 == 0:
            print(iter)


        if len(p2) == 0:
            #print(f"{exS}p2 out of cards")
            return (1,p1)
        if len(p1) == 0:
            #print(f"{exS}p1 out of cards")
            return (2,p2)

        c1 = p1.pop(0)
        c2 = p2.pop(0)
        
        exS = " "*depth

        # infinite handling
        p1str = str(p1)
        p2str = str(p2)
        if p1str in setups or p2str in setups:
            #print(f"{exS}Infinite {p1},{p2}")
            p1.append(c1)
            p1.append(c2)
            return (1,p1)

        else:
            setups[p1str] = 1
            setups[p2str] = 1
            # infinite handling

            if len(p1) >= c1 and len(p2) > c2:
                #print(f"{exS}recurses {p1},{p2}")
                cp1 = copy.deepcopy(p1)
                cp2 = copy.deepcopy(p2)
                csetup = copy.deepcopy(setups)
                (winner,_) = combat(cp1,cp2,csetup, depth=(depth+1))

                if winner == 1:
                    p1.append(c1)
                    p1.append(c2)    
                    #print(f"{exS}p1 recwins {p1},{p2}")
                if winner == 2:
                    p2.append(c2)
                    p2.append(c1) 
                    #print(f"{exS}p2 recwins {p1},{p2}")
        
            elif c1 > c2:
                p1.append(c1)
                p1.append(c2)    
                #print(f"{exS}p1 wins {p1},{p2}")
            elif c2 > c1:
                p2.append(c2)
                p2.append(c1)
                #print(f"{exS}p2 wins {p1},{p2}")

(winner,winnerdeck) = combat(ply1,ply2,{})

ret = 0
for index,x in enumerate(winnerdeck):
    ret += x*(len(winnerdeck)-index)

print(f"part2: {ret}")

    