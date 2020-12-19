import re
import json
import copy 

tDigit = 1
tOr = 2
tAnd = 3
tOrSmall = 4
tOr3 = 5
tOr5 = 6

def gett(i):
    if i == tDigit:
        return "D"
    if i == tAnd:
        return "&"
    if i == tOr:
        return "|"
    if i == tOrSmall:
        return "i"
    if i == tOr3:
        return "3"
    if i == tOr5:
        return "5"
    else:
        print(i)
        return "X"

f = open("input.txt","r").read()

rx = re.sub("\n","\",\n", f)

sections = f.split("\n\n")
lines = sections[0].split("\n")
mx = []
for x in lines:
    mx.append(int(x.split(":")[0]))

rules = ["" for x in range(max(mx)+1)]
rtype = [0 for x in range(max(mx)+1)]

for x in lines:
    [strnum, strrule] = x.split(": ")
    num = int(strnum)
    
    if strrule[1].isalpha():
        rtype[num] = tDigit

        rules[num] = strrule[1]
    elif "|" in strrule:
        [aor, bor] = strrule.split(" | ")
        ret = [int(x) for x in aor.split(" ")[0:2]]
        ret.extend([int(x) for x in bor.split(" ")[0:2]])

        ln = len(ret)
        if ln == 2:
            rtype[num] = tOrSmall
        elif ln == 4:
            rtype[num] = tOr
        elif ln == 3:
            rtype[num] = tOr3
        elif ln == 5:
            rtype[num] = tOr5

        rules[num] = ret
    else:
        rtype[num] = tAnd
        rules[num] = [int(x) for x in strrule.split(" ")]

del lines
del rx

cached = [{} for x in range(max(mx)+1)]
nloops = 0

def wordworks(str, ri) -> int:
    global nloops

    if str in cached[ri].keys():
        return cached[ri][str]
    nloops+=1

    if len(str) < 1:
        return 0
    
    #print(f"{str}\t for #{ri} = {gett(rtype[ri])} {rules[ri]}")

    get = rtype[ri]
    if get == tDigit:
        if str[0] == rules[ri]:
            cached[ri][str] = 1
            return 1
        return 0

    elif get == tAnd:
        totmatch = 0
        for ri2 in rules[ri]:
            matchlen = wordworks(str[totmatch:],ri2)
            if matchlen == 0:
                #print(f"tAnd for \"{str}\" \t failed for ri = {ri2}")
                return 0

            totmatch += matchlen

        cached[ri][str] = totmatch
        return totmatch

    elif get == tOr:
        [a,b,c,d] = rules[ri]

        matchlen = wordworks(str,a)
        if matchlen != 0:
            matchlen2 = wordworks(str[matchlen:],b)
            if matchlen2 != 0:
                cached[ri][str] = matchlen+matchlen2
                return matchlen+matchlen2

        matchlen = wordworks(str,c)
        if matchlen != 0:
            matchlen2 = wordworks(str[matchlen:],d)
            if matchlen2 != 0:
                cached[ri][str] = matchlen+matchlen2
                return matchlen+matchlen2

        #print(f"tOr  for \"{str}\" \t failed for {a} {b} | {c} {d}")
        return 0
    elif get == tOrSmall:
        [a,b] = rules[ri]
        
        matchlen = wordworks(str,a)
        if matchlen != 0:
            cached[ri][str] = matchlen
            return matchlen

        matchlen = wordworks(str,b)
        if matchlen != 0:
            cached[ri][str] = matchlen
            return matchlen

        return 0
    else:
        print(f"unhandled:{str} for {rtype[ri]}:{rules[ri]}")
        exit()

def wordGood(str, rule):
    try:
        nWork = wordworks(str, rule)
        if len(str) == nWork:
            return nWork
        return 0
    except:
        return 0

nworks = 0
for word in sections[1].split("\n"):
    print(word)
    if wordGood(word,0) != 0:
        nworks+=1

print(nworks)
print(f"loops:{nloops}")
    