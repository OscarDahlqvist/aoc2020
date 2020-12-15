import re
import json

f = open("input.txt","r").read()

rx = '['+f+'\n]'

seq = json.loads(rx)

indexs = {}

for i,v in enumerate(seq):
    indexs[v] = [i]

print(indexs)

for i in range(len(seq),30000000):
    if(i%30000 == 0):
        print(i)

    lastSaid = seq[-1]
    lastSaidOccs = indexs[lastSaid]

    #print(f"{lastSaid} occ = {lastSaidOccs}")

    appendval = -1

    if len(lastSaidOccs) < 2:
        appendval = 0
    else:
        diffturns = lastSaidOccs[-1]-lastSaidOccs[-2]
        appendval = diffturns

    seq.append(appendval)
    
    if not appendval in indexs:
        indexs[appendval] = []
    indexs[appendval].append(i)

print(seq[-1])
