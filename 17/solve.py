import re
import json
import copy 

f = open("input.txt","r").read()

centerSlice = 9
worldSize = centerSlice*2+1

line = ['.' for x in range(worldSize)]
plane = [copy.deepcopy(line) for x in range(worldSize)]
world = [copy.deepcopy(plane) for x in range(worldSize)]

def set(arr,x,y,z,val):
    rx = x+centerSlice
    ry = y+centerSlice
    rz = z+centerSlice

    l = worldSize
    if rx < 0 or ry < 0 or rz < 0:
        return
    if rx >= l or ry >= l or rz >= l:
        return

    arr[rz][ry][rx] = val
    return
def get(arr,x,y,z):
    rx = x+centerSlice
    ry = y+centerSlice
    rz = z+centerSlice

    l = worldSize
    if rx < 0 or ry < 0 or rz < 0:
        return "."
    if rx >= l or ry >= l or rz >= l:
        return "."

    return arr[rz][ry][rx]

def prnt():
    for index, plane in enumerate(world):
        reindex = index-centerSlice
        print(f"z={reindex}")
        for line in plane:
            print("".join(line))

def neighbors(arr,x,y,z):
    n = 0
    for tz in range(z-1,z+2):
        for ty in range(y-1,y+2):
            for tx in range(x-1,x+2):
                if (tz,ty,tx) == (z,y,x): continue
                if get(arr,tx,ty,tz) == "#":
                    n+=1
    return n

def step():
    global world
    newworld = copy.deepcopy(world)
    nworld = copy.deepcopy(world)
    for x in range(-centerSlice, centerSlice+1):
        for y in range(-centerSlice, centerSlice+1):
            for z in range(-centerSlice, centerSlice+1):
                val = get(world,x,y,z)
                neigh = neighbors(world,x,y,z)
                
                set(nworld,x,y,z,str(neigh))

                if val == "." and neigh == 3:
                    set(newworld,x,y,z,"#")

                if val == "#" and (neigh < 2 or neigh > 3):
                    set(newworld,x,y,z,".")

    world = copy.deepcopy(nworld)
    world = copy.deepcopy(newworld)

d = len(f.split("\n"))
for y,line in enumerate(f.split("\n")):
    for x,c in enumerate(line):
        rx = x-(d//2)
        ry = y-(d//2)
        set(world,rx,ry,0,c)

step()
step()
step()
step()
step()
step()

n = 0
for plane in world:
    for line in plane:
        for char in line:
            if char == "#":
                n+=1
print(n)