import re
import json
import itertools

f = open("input.txt","r").read()

rx = re.sub(r"\n", r',\n', f)
rx = '[\n'+rx+'\n]'

d = json.loads(rx)
d.sort()

devicemax = max(d)+3

print(d)

n1 = 1 # for zero start
n3 = 1 # for zero start
for index,val in enumerate(d[0:-1]):
    diff = abs(val - d[index+1])
    if diff == 1:
        n1+=1
    if diff == 3:
        n3+=1
print(f"n1:{n1},n3:{n3}, prod:{n1*n3}")

d.append(devicemax)
seq = [0]
seq.extend(d)

print(seq)

def arrangements(arr, start, depth):
    if calculated[start] != -1:
        return calculated[start]

    global iters
    iters += 1
    
    #print(f"arrangements({arr[start:]})")
    if(len(arr)-1 == start):
        #print(f"=>end {arr[start:]}")
        
        calculated[start] = 1
        return 1
    
    fInvalid = len(arr)
    for x in range(start+1, min(start+5,len(arr))):
        if(arr[x]-arr[start] > 3):
            fInvalid = x
            break

    totArrang = 0

    validChildren = range(start+1,fInvalid)
    for i in validChildren:
        totArrang += arrangements(arr, i, depth+1)

    calculated[start] = totArrang
    return totArrang

calculated = [-1 for x in range(0,len(seq))]
iters = 0
solve = arrangements(seq,0,0)
print(solve)
print(iters)
