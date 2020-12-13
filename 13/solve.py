import re
import json

f = open("input.txt","r").read()

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

def works(arr, time, num):
    offset = arr.index(num)
    if(time+offset) % num == 0:
        return True
    return False

temp = []
busNums = []
for x in lines:
    if x == "x":
        temp.append(x)
    else:
        temp.append(int(x))
        busNums.append(int(x))
lines = temp

worksOffset = 0 #o
worksSize = 1   #s
nCorrect = 0

while True:
    i += worksSize

    get = lines[nCorrect]

    if get == "x":
        nCorrect+=1
    
    elif works(lines, i, get):
        oldSize = worksSize
        worksSize *= get
        if nCorrect > 0:
            of = worksOffset
            for x in range(0,get):
                
                if works(lines, of, get):
                    if of%oldSize == worksOffset:
                        worksOffset = of
                        break
                of += oldSize
            else:
                print("found nothing")

        nCorrect+=1
        i = worksOffset
        print(f"{worksSize}n + {worksOffset} works for {lines[:nCorrect]}")

        if(nCorrect >= len(lines)):
            break
    
for i in range(worksOffset,worksOffset+len(lines)):
    print(departs(lines,i))
        
""" 
b,c,d,e,f,g,h,i,j = symbols("b,c,d,e,f,g,h,i,j", integer=True)
syms = [b,c,d,e,f,g,h,i,j]
a = symbols("a", integer=True)

nvar = 0
sumeq = 0
for index,x in enumerate(lines):
    if(x == "x"): continue
    val = int(x)
    
    eq = -(a+index)+val*syms[nvar]
    sumeq+=eq
    print(eq)
    nvar += 1

print(sumeq)
#cof = sumeq.coeff(n)
#sumeq = solve(sumeq,n*cof)[0]
#print(f"{sumeq} = {cof}n")
dio = diop_solve(sumeq)
print(dio)
for index,val in enumerate(dio.free_symbols):
    print(val)
"""
