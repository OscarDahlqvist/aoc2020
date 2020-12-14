import re
import json

f = open("input.txt","r").read()

rx = re.sub(r"\n", r'",\n"', f)
rx = '[\n\"'+rx+'\"\n]'

js = json.loads(rx)

mem = {}
ormask = 0
andmask = 0

def pin(i):
    print(format(i, "b").zfill(36), f"({i})")

for index,val in enumerate(js):
    if "mask" in val:
        strmask = val.split("= ")[1]
        ormask = int(re.sub("X", "0", strmask), 2)
        andmask = int(re.sub("X", "1", strmask), 2)
    elif "mem" in val:
        [loc,assignment] = val.split("] = ")
        loc = int(re.sub("mem\[","", loc))
        assignment = int(assignment)

        masked = (assignment|ormask)&andmask
        
        mem[f"g{loc}"] = masked
print(sum(mem.values()))
print()

mem = {}
ormask = 0
andmask = 0
xlocs = []
xmask = 0

def intersperse(ins,arr):
    ret = 0
    iter = 0
    for x in arr:
        ret |= (ins>>iter & 1)<<x
        iter +=1
    return ret

for index,val in enumerate(js):
    if "mask" in val:
        strmask = val.split("= ")[1]
        ormask = int(re.sub("X", "0", strmask), 2)
        xlocs = []
        xmask = 0
        for index,xal in enumerate(strmask):
            if xal == "X":
                xlocs.append(35-index)
                xmask |= 1<<(35-index)
        xlocs.sort()
    elif "mem" in val:
        [loc,assignment] = val.split("] = ")
        loc = int(re.sub("mem\[","", loc))
        assignment = int(assignment)

        mx = 0
        locset = []
        #print(xlocs)
        while mx < 2**len(xlocs):
            temp = intersperse(mx, xlocs)
            mx += 1

            mloc = (loc|ormask)&~andmask
            mloc = (mloc &~ xmask)|temp

            mem[f"g{mloc}"] = assignment

            #print(f"mem[{mloc}] = {assignment}")
"""
for kv in mem.items():
    print(kv)"""
print(sum(mem.values()))
    
