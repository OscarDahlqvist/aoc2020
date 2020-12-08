import re
import json
import ast

f = open("input.txt","r").read()

rx = f.split('\n')

def asCode(inp):
    inp = inp.split(" ")
    return(inp[0],int(inp[1]))

rx = [asCode(x) for x in rx]
print(str(rx)+"\n")

acc = 0
adr = 0
hasVisited = []

versions = []
for index,(op,arg) in enumerate(rx):
    if(op == "jmp"):
        x = rx.copy()
        x[index]= ("nop",arg)
        versions.append(x)
    
    if(op == "nop"):
        x = rx.copy()
        x[index]= ("jmp",arg)
        versions.append(x)
        
for index,x in enumerate(versions):
    acc = 0
    adr = 0
    hasVisited = []
    try:
        while True:
            hasVisited.append(adr)
            (op,arg) = x[adr]
            #print(f"{adr} {x[adr]}")

            if op == "nop":
                adr += 1
            if op == "acc":
                acc += arg
                adr += 1
            if op == "jmp":
                adr += arg
            if adr in hasVisited:
                break
        print(f"version {index} failed")
    except:
        for index,var in enumerate(x):
            if var != rx[index]:
                print(f"version {index} sucess")
                print(f"..\n{index} {rx[index]} changed to {var} success\n..")
                print(f"acc = {acc}")
                break
            
        
        break

"""  
while True:
    hasVisited.append(adr)
    (op,arg) = rx[adr]
    print(f"{adr} {rx[adr]}")

    if op == "nop":
        adr += 1
    if op == "acc":
        acc += arg
        adr += 1
    if op == "jmp":
        adr += arg
        if adr in hasVisited:
            break
print(acc)
"""
    
