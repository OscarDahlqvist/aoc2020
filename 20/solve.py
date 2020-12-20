import re
import json
import copy 
import itertools 
import math  
import numpy as np

f = open("input.txt").read()

bricks = {}

for headeredBrick in f.split("\n\n"):
    lines = headeredBrick.split("\n")
    lines.reverse()
    header = lines.pop()
    header = header.split(" ")[1].split(":")[0]
    header = int(header)
    lines.reverse()

    bricks[header] = [list(x) for x in lines]

del lines
del header

nBricks = len(bricks)
outputSize = int(math.sqrt(nBricks))
if nBricks != outputSize**2:
    exit()

print(f"worldsize:{outputSize}")

brickH = len(list(bricks.values())[0])
brickW = len(list(bricks.values())[0][0])
maxH = brickH-1
maxW = brickW-1

def worksNoRotateFlip(b1, b2):
    retset = []

    #left edge (left edge of b1 matches b2)
    for h in range(brickH):
        if b1[h][0] != b2[h][maxW]: break
    else: retset.append("left")

    #right edge (right edge of b1 matches b2)
    for h in range(brickH):
        if b1[h][maxW] != b2[h][0]: break
    else: retset.append("right")
    
    #top edge (top edge of b1 matches b2)
    for w in range(brickW):
        if b1[0][w] != b2[maxH][w]: break
    else: retset.append("top")
    
    #bottom edge (bottom edge of b1 matches b2)
    for w in range(brickW):
        if b1[maxH][w] != b2[0][w]: break
    else: retset.append("bottom")

    return retset

rbricks = {}
for k,v in bricks.items():
    #print(v)
    rbricks[k] = {}
    rbricks[k]["r0"] = np.array(v)
    rbricks[k]["r90"] = np.rot90(v)
    rbricks[k]["r180"] = np.rot90(rbricks[k]["r90"])
    rbricks[k]["r270"] = np.rot90(rbricks[k]["r180"])    
    rbricks[k]["f0"] = np.flipud(rbricks[k]["r0"])
    rbricks[k]["f90"] = np.flipud(rbricks[k]["r90"])
    rbricks[k]["f180"] = np.flipud(rbricks[k]["r180"])
    rbricks[k]["f270"] = np.flipud(rbricks[k]["r270"])

brickNames = list(rbricks.keys())
keylist = list(rbricks[brickNames[0]].keys())

def works(k1,k2):
    rb1 = rbricks[k1]
    rb2 = rbricks[k2]

    keys = list(itertools.product(keylist, repeat=2))

    retset = []
    for axis1, axis2 in keys:
        for side in worksNoRotateFlip(rb1[axis1],rb2[axis2]):
            retset.append((axis1,axis2,side))

    return retset

conditions = {}

for (b1,b2) in itertools.permutations(brickNames, r=2):
    for (b1axis, b2axis, side) in works(b1,b2):
        if not (b1,b1axis) in conditions:
            conditions[(b1,b1axis)] = []
        conditions[(b1,b1axis)].append((side,b2,b2axis))  

allAxis = list(conditions.keys())

def cpy(x):
    return copy.deepcopy(x)

hackyBadRetVal = []

def mx(grid, remaning, index):
    x = index%outputSize
    y = index//outputSize

    validNextBricks = []
    if index == nBricks:
        
        global hackyBadRetVal
        hackyBadRetVal = grid
        x = (1/0) #crashes and exits

    elif x == 0:
        above = grid[y-1][x]
        for (side,brick,brickAxis) in conditions[above]:
            if side == "bottom":
                validNextBricks.append((brick,brickAxis))

    elif index < outputSize:
        left = grid[y][x-1]
        for (side,brick,brickAxis) in conditions[left]:
            if side == "right":
                validNextBricks.append((brick,brickAxis))

    elif index >= outputSize:
        above = grid[y-1][x]
        left = grid[y][x-1]
        for (side,brick,brickAxis) in conditions[left]:
            if side == "right":
                for (side2,brick2,brickAxis2) in conditions[above]:
                    if side2 == "bottom":
                        if brick2 == brick and brickAxis == brickAxis2:
                            validNextBricks.append((brick,brickAxis))
    
    for nextBrick in validNextBricks:
        newRemaning = cpy(remaning)
        newRemaning.remove(nextBrick)
        newGrid = cpy(grid)
        newGrid[y][x] = nextBrick

        mx(newGrid, newRemaning, index+1)

orgGrid = [[0 for x in range(outputSize)] for x in range(outputSize)]

print("preproccessing done")
for idx,tup in enumerate(allAxis):
    remainingBricks = cpy(allAxis)
    remainingBricks.remove(tup)

    newGrid = cpy(orgGrid)
    newGrid[0][0] = tup

    try:
        ret = mx(newGrid, remainingBricks, 1)
    except:
        break
else:
    print("No Value found")
    exit()

print("Grid found")

X = outputSize-1
(a,_) = hackyBadRetVal[0][0]
(b,_) = hackyBadRetVal[0][X]
(c,_) = hackyBadRetVal[X][0]
(d,_) = hackyBadRetVal[X][X]
print(f"part 1: {a*b*c*d}")

# Part 2

imageSize = (brickH-2)*outputSize
imageGrid = [[" " for x in range(imageSize)] for x in range(imageSize)]

for y,row in enumerate(hackyBadRetVal):
    for x,(brickNum, brickAxis) in enumerate(row):
        rbrickWithEdges = rbricks[brickNum][brickAxis]

        rbrick = rbrickWithEdges[1:-1]
        rbrick = [x[1:-1] for x in rbrick]

        for y2, row in enumerate(rbrick):
            for x2, char in enumerate(row):
                imageGrid[y2+(brickH-2)*y][x2+(brickH-2)*x] = char

#this does absolutely nothing important, just for verifying the example
imageGrid = np.flipud(imageGrid)
imageGrid = np.fliplr(imageGrid)
imageGrid = np.rot90(imageGrid)
imageGrid = np.rot90(imageGrid)

snake = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]
snakeHeight = len(snake)
snakeWidth = len(snake[0])

snakeLocList = []
for y in range(snakeHeight):
    for x in range(snakeWidth):
        if snake[y][x] == "#":
            snakeLocList.append((y,x))

def getOverlaps(sea):
    overLapsPos = []
    for orgY in range(imageSize-snakeHeight):
        for orgX in range(imageSize-snakeWidth):
            for (dy,dx) in snakeLocList:
                if sea[orgY+dy][orgX+dx] != "#":
                    break
            else:
                temp = [(orgY+y,orgX+x) for (y,x) in snakeLocList]
                overLapsPos.extend(temp)
                continue
            
    for (y,x) in overLapsPos:
        sea[y][x] = "O"

    return sea

def r(x):
    return np.rot90(x)
def getFlipOverlap(x):
    return np.flipud(getOverlaps(np.flipud(x)))
def allRotOverlaps(sea):
    sea0    = getOverlaps(sea)
    sea90   = r(r(r(getOverlaps(r(sea)))))
    sea180  = r(r(getOverlaps(r(r(sea)))))
    sea270  = r(getOverlaps(r(r(r(sea)))))

    Fsea0   = getFlipOverlap(sea)
    Fsea90  = r(r(r(getFlipOverlap(r(sea)))))
    Fsea180 = r(r(getFlipOverlap(r(r(sea)))))
    Fsea270 = r(getFlipOverlap(r(r(r(sea)))))

    xset = set()
    for t in [sea0, sea90, sea180, sea270, Fsea0, Fsea90, Fsea180, Fsea270]:
        for y in range(imageSize):
            for x in range(imageSize):
                if(t[y][x] == "O"):
                    xset.add((y,x))
    return list(xset)

nHash = 0
for line in imageGrid:
    for char in line:
        if char == "#":
            nHash += 1
    
snakeTiles = allRotOverlaps(imageGrid)
print(f"part 2: {nHash-len(snakeTiles)}")
            