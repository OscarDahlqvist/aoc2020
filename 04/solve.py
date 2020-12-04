import re
import json

f = open("input.txt","r").read()

rx = re.sub(r"\n\n", r"},{", f)
rx = re.sub(r"\n", r" ", rx)
rx = re.sub(r"},{", r"},\n{", rx)
rx = "[{"+rx+"}]"

rx = re.sub(r"(\w+)(?=:)", r'"\1"', rx)
rx = re.sub(r"(?<=:)([a-zA-Z0-9#]+)", r'"\1"', rx)
rx = re.sub(r" ", r", ", rx)

d = json.loads(rx)

def isValidHeight(inp):
    if "cm" in inp:
        match = re.search(r"\d+(?=cm)",inp).group(0)
        if 150 <= int(match) <= 193: return True
        
    if "in" in inp:
        match = re.search(r"\d+(?=in)",inp).group(0)
        if 59 <= int(match) <= 76: return True
        
    print(str(inp)+" is invalid")
    return False

def isValidHair(inp):
    if re.search(r"(^#[0-9a-f]{6}$)",inp): return True
    
    print(str(inp)+" is invalid")
    return False

def isValidEye(inp):
    if inp in ["amb","blu","brn","gry","grn","hzl","oth"]: return True
    
    print(str(inp)+" is invalid")
    return False

def isValidPassId(inp):
    if re.search(r"(^\d{9}$)",inp): return True
    
    print(str(inp)+" is invalid")
    return False


requierd = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
correct = []
for index, item in enumerate(d):
    #print(item)
    if len([req for req in requierd if req in item])>=len(requierd):
        item.update({"zi":index})

        if not(1920 <= int(item["byr"]) <= 2002): continue
        if not(2010 <= int(item["iyr"]) <= 2020): continue
        if not(2020 <= int(item["eyr"]) <= 2030): continue
        if not isValidHeight(item["hgt"]): continue
        if not isValidHair(item["hcl"]): continue
        if not isValidEye(item["ecl"]): continue
        if not isValidPassId(item["pid"]): continue
        
        correct.append(item)
        
for index, item in enumerate(correct):
    print(str(item["zi"])+":"+str(item))

print(len(correct))
