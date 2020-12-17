import re
import json
import copy 

f = open("input.txt","r").read()

centerSlice = 10
worldSize = centerSlice*2+1

tempLine = ['.' for x in range(worldSize)]
tempPlane = [copy.deepcopy(tempLine) for x in range(worldSize)]
tempWorld = [copy.deepcopy(tempPlane) for x in range(worldSize)]
hyperworld = [copy.deepcopy(tempWorld) for x in range(worldSize)]

def set(arr,x,y,z,w,val):
    rx = x+centerSlice
    ry = y+centerSlice
    rz = z+centerSlice
    rw = w+centerSlice

    l = worldSize
    if rx < 0 or ry < 0 or rz < 0 or rw < 0:
        return
    if rx >= l or ry >= l or rz >= l or rw >= l:
        return

    arr[rw][rz][ry][rx] = val
    return
def get(arr,x,y,z,w):
    rx = x+centerSlice
    ry = y+centerSlice
    rz = z+centerSlice
    rw = w+centerSlice

    l = worldSize
    if rx < 0 or ry < 0 or rz < 0 or rw < 0:
        return "."
    if rx >= l or ry >= l or rz >= l or rw >= l:
        return "."

    return arr[rw][rz][ry][rx]

def prnt():
    for windex, world in enumerate(hyperworld):
        for zindex, plane in enumerate(world):
            rw = windex-centerSlice
            rz = zindex-centerSlice
            print(f"z={rz}, w={rw}")
            for line in plane:
                print("".join(line))

def neighbors(arr,x,y,z,w):
    n = 0
    for tw in range(w-1,w+2):
        for tz in range(z-1,z+2):
            for ty in range(y-1,y+2):
                for tx in range(x-1,x+2):
                    if (tw,tz,ty,tx) == (w,z,y,x): continue
                    if get(arr,tx,ty,tz,tw) == "#":
                        n+=1
    return n

def step():
    global hyperworld
    newhyperworld = copy.deepcopy(hyperworld)
    for x in range(-centerSlice, centerSlice+1):
        for y in range(-centerSlice, centerSlice+1):
            for z in range(-centerSlice, centerSlice+1):
                for w in range(-centerSlice, centerSlice+1):
                    val = get(hyperworld,x,y,z,w)
                    neigh = neighbors(hyperworld,x,y,z,w)

                    if val == "." and neigh == 3:
                        set(newhyperworld,x,y,z,w,"#")

                    if val == "#" and (neigh < 2 or neigh > 3):
                        set(newhyperworld,x,y,z,w,".")

    hyperworld = copy.deepcopy(newhyperworld)

d = len(f.split("\n"))
for y,line in enumerate(f.split("\n")):
    for x,c in enumerate(line):
        rx = x-(d//2)
        ry = y-(d//2)
        set(hyperworld,rx,ry,0,0,c)

prnt()
step()
print(f"step:1")
step()
print(f"step:2")
step()
print(f"step:3")
step()
print(f"step:4")
step()
print(f"step:5")
step()
print(f"step:6")
prnt()

n = 0
for world in hyperworld:
    for plane in world:
        for line in plane:
            for char in line:
                if char == "#":
                    n+=1
print(n)