import re
import json
from math import prod

f = open("inputex.txt","r").read()

rx = re.sub(r",", r'","', f)
rx = re.sub(r"\n", r'","', rx)
rx = re.sub(r",", r',\n', rx)
rx = '[\n\"'+rx+'\"\n]'

js = json.loads(rx)
    
start = int(js[0])
lines = js[1:]

print(lines)

for i in range(start,2000000000):
    for dep in lines:
        if dep == "x": continue
        t = int(dep)
        if(i % t == 0):
            print(f"bus {t} departs at {i}*{t} ({i*t})")
            print(f"needed wait {i-start} minutes")
            print(f"solve = {(i-start)*t} for start = {start}")
            break
        
    else: continue
    break

print()

def departs(arr, time):
    return [x for x in arr if x!="x" and time%x == 0]

lines2 = []
for x in lines:
    if x == "x":
        lines2.append(x)
    else:
        lines2.append(int(x))
lines = lines2
print(lines)

minbus = min([x for x in lines if x!="x"])

looki = 0
seq = []
startTime = 0
for i in range(1, 2**32):
    get = lines[looki]
    if(get == "x" or i % get == 0):
            
        looki += 1
        
        if(looki == len(lines)):
            print(f"{startTime} to {i}")
            for z in range(startTime, i+1):
                print(departs(lines,z))
            break
        
        if(i % minbus == 0):
            startTime = i
    else:
        looki = 0
                
                    
