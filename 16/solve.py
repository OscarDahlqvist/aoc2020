import re
import json

f = open("input.txt","r").read()

[rulestr,yourstr,otherstr] = f.split("\n\n")
otherstr = re.sub("nearby tickets:\n","",otherstr)
yourstr = re.sub("your ticket:\n","",yourstr)


rules = {}
allvalid = []
for line in rulestr.split("\n"):
    [paramname, args] = line.split(":")
    [lo,hi] = args.split(" or ")
    [lolo, lohi] = [int(x) for x in lo.split("-")]
    [hilo, hihi] = [int(x) for x in hi.split("-")]

    allvalid.extend(range(lolo,lohi+1))
    allvalid.extend(range(hilo,hihi+1))

    r = list(range(lolo,lohi+1))
    r.extend(range(hilo,hihi+1))
    rules[paramname] = r

invalid = []
validTickets = []
for linenum, line in enumerate(otherstr.split("\n")):
    foundInvalidValue = False
    for numstr in line.split(","):
        try:
            num = int(numstr)
        except:
            continue

        if not num in allvalid:
            invalid.append(num)
            foundInvalidValue = True
    
    if not foundInvalidValue:
        validTickets.append(line)

print(sum(invalid))

rulenames = [x.split(":")[0] for x in rulestr.split("\n")]
nargs = len(yourstr.split(","))
candidates = [rulenames.copy() for _ in range(nargs)]

for line in validTickets:    
    for idx, numstr in enumerate(line.split(",")):
        num = int(numstr)
        for (k,v) in rules.items():
            if not num in v:
                candidates[idx].remove(k)
                print(f"removed {k} from index {idx}")
                
finalMeaning = ["" for x in range(nargs)]
nFound = 0

while True:

    for idx, val in enumerate(candidates):
        if len(val) == 1:
            get = val[0]
            nFound += 1
            finalMeaning[idx] = get
            for x in candidates:
                if(get in x):
                    x.remove(get)
            
    if nFound == nargs:
        break
print(finalMeaning)

prod = 1
yourlst = yourstr.split(",")
for idx, val in enumerate(finalMeaning):
    if "departure" in val:
        get = yourlst[idx]
        prod *= int(get)
print(prod)