import re
import json
import ast

f = open("input.txt","r").read()

rx = re.sub(r"\n", r'",\n"', f)
rx = '[\n\"'+rx+'\"\n]'
d = ast.literal_eval(rx)
print(d)

rules = {}
colors = {}

def handle(str):
    [src,content] = str.split("bags contain")
    src = src[:-1]
    content = content.split(",")
    content = [x.split(" ") for x in content]

    if src in rules:
        print("UNHANDLED for:"+src)
    rules.update({src:{}})
    colors.update({src:0})
            
    for x in content:
        if x[1] == "no": continue

        name = x[2]+" "+x[3]
        count = int(x[1])

        colors.update({name:0})

        rules[src].update({name:count})

for x in d:
    handle(x)
for (k,v) in rules.items():
    print(str(k)+":\t"+str(v))
print(colors)

def dictMerge(d1,d2):
    ret = {}
    ret.update(d2)
    for (k,v) in d1.items():
        if k in ret:
            ret[k] += v
        else:
            ret.update({k:v})
    return ret
    
def getch(color, depth = 0):
    print((" "*depth)+color+str(rules[color]))
    ret = {color:1}
    if len(rules[color]) == 0:
        return {color:1}
    else:
        for (k,v) in rules[color].items():
            child = {}
            for content,nOcc in getch(k, depth+1).items():
                child.update({content:nOcc*v})
            ret = dictMerge(ret, child)
    return ret
"""
def contains(arr, index, mustContain):
    if mustContain in arr[index]:
        return True
    has = False
    for k,v in rules[index].items():
        has|=contains(arr, k, mustContain)
    return has

nHasGold = 0
for c in colors:
    x = contains(rules, c, "shiny gold")
    if x == True:
        nHasGold+=1
    print({c:x})
print(nHasGold)
"""
x = getch("shiny gold")
print(x)
print(sum(x.values())-1)


    
