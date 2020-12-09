import re
import json
import itertools

f = open("input.txt","r").read()

rx = re.sub(r"\n", r',\n', f)
rx = '[\n'+rx+'\n]'

d = json.loads(rx)

pa = 25

for index,val in enumerate(d):
    if index <= pa: continue

    prev = d[index-pa-1:index]
    
    sumExists = False
    for (x,y) in itertools.combinations(prev, 2):
        #print(f"{(x,y)} for {index}:{val} \t-> diff {x+y - val}")
        if x+y == val:
            sumExists = True
            #print(f"{(x,y)} = {val} for {prev}")
            break
    if sumExists == False:
        print(f"FAILED at d[{index}] ({val})")
        print(f"nothing equals = {val} for {prev}")
        print()

        for scope in range(2,index):
            for bot in range(0,index-scope):
                top = bot+scope
                section = d[bot:top]
                if(sum(section) == val):
                    print(f"{val} = sum({section})")
                    maxv = max(section)
                    minv = min(section)
                    print(f"max = {maxv} min = {minv}")
                    print(f"max+min = {maxv+minv}")
                    break
            else: continue
            break
            
        break
