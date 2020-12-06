import re
import json
import string

f = open("input.txt","r").read()

rx = re.sub(r"\n\n", r'"],["', f)
rx = re.sub(r"\n", r'","', rx)
rx = re.sub(r'"\],\["', r'"],\n["', rx)
rx = '[\n[\"'+rx+'\"]\n]'

input = json.loads(rx)

someone = 0
everyone = 0
for group in input:
    exist = {}
    for person in group:
        for c in string.ascii_lowercase:
            if c in person:
                if c in exist:
                    exist[c] += 1
                else:
                    exist[c] = 1

    for (c,occ) in exist.items():
        if occ == len(group):
            everyone += 1
            
    someone += len(exist)
print(someone)
print(everyone)
