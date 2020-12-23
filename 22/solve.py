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

iter = 0

def combat(p1,p2,depth=0):
    deckHistory = {}
    winner = 0

    while len(p2) > 0 and len(p1) > 0:
        
        global iter
        iter+=1
        if iter % 1000000 == 0:
            print(iter)

        exS = " "*depth

        c1 = p1.pop(0)
        c2 = p2.pop(0)

        pflat = "".join([chr(x+33) for x in p1]) + "".join([chr(x+33) for x in p2])

        if pflat in deckHistory:
            winner = 1
        else:
            deckHistory[pflat] = 1

            if c1 > len(p1) or c2 > len(p2):
                if c1 > c2:
                    winner = 1
                elif c2 > c1:
                    winner = 2
            else:
                #print(f"{exS}recurses {p1},{p2}")
                cp1 = copy.deepcopy(p1)
                cp2 = copy.deepcopy(p2)
                (x,_,_) = combat(cp1[:c1],cp2[:c2], depth=(depth+1))
                winner = x

        if winner == 1:
            p1.append(c1)
            p1.append(c2)    
            #print(f"{exS}p1 wins {p1},{p2}")
        if winner == 2:
            p2.append(c2)
            p2.append(c1) 
            #print(f"{exS}p2 wins {p1},{p2}")

    winnerdeck = []
    looserdeck = []
    if winner == 1: 
        winnerdeck=p1
        looserdeck=p2
    if winner == 2:
        winnerdeck=p2
        looserdeck=p1
    
    #print(f"p{winner} wins round:{depth} {p1},{p2}")

    return (winner,winnerdeck,looserdeck)

(winner,winnerdeck,_) = combat(ply1,ply2)

ret = 0
for index,x in enumerate(winnerdeck):
    ret += x*(len(winnerdeck)-index)

print(f"part2: {ret}")
print(winnerdeck)

    