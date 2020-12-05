import re
import json

f = open("input.txt","r").read()

rx = re.sub(r"\n", r'","', f)
rx = "[\""+rx+"\"]"

input = json.loads(rx)

def findIndex(inp): #is BBFFBBLLL... string
    rmin = 0
    rmax = 127
    cmin = 0
    cmax = 7
    
    for c in inp:
        if c == "F":
            rmax = (rmin+rmax)//2
        if c == "B":
            rmin = (rmin+rmax)//2
            
        if c == "L":
            cmax = (cmin+cmax)//2
        if c == "R":
            cmin = (cmin+cmax)//2
    return(rmax,cmax)

def seatId(a):
    (row,col) = a
    return row*8+col

plane = [0 for y in range(128*8)]

ret = []
for code in input:
    (col,row) = findIndex(code)
    id = seatId((col,row))
    plane[id] = 1
    ret.append(id)
    
ret.sort(reverse=True)
print(ret)

for index,seat in enumerate(plane):
    if(seat == 0): print(index)
        
