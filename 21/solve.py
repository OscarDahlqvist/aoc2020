import re
import json
import copy 
import itertools 

f = open("input.txt").read()

candidates = {}
allIngredients = []
for line in f.split("\n"):
    [unknown, known] = line.split(" (contains ")

    allerg = known.split(", ")
    allerg[-1] = allerg[-1][:-1]
    
    ingr = unknown.split(" ")
    allIngredients.extend(ingr)

    for alg in allerg:
        if not alg in candidates:
            candidates[alg] = []
        candidates[alg].append(ingr)

ingredientsSet = list(set(allIngredients))
occIngredients = {x:allIngredients.count(x) for x in ingredientsSet}

notAllergenItems = copy.deepcopy(occIngredients)

allergyCandicates = {}

for k,v in candidates.items():
    acc = set(v[0])
    for i in range(1,len(v)):
        acc = set(v[i]).intersection(acc)
    
    for x in acc:
        if x in notAllergenItems:
            del notAllergenItems[x]
        
    allergyCandicates[k] = list(acc)

print(f"part1: {sum(notAllergenItems.values())}")

# part 2

certain = {}
while len(allergyCandicates) > 0:
    allergCopy = copy.deepcopy(allergyCandicates)
    for k,v in allergCopy.items():
        if len(v) == 1:
            get = v[0]
            allergyCandicates.pop(k,None)
            certain[k] = get
            for k,v in allergyCandicates.items():
                if get in v:
                    v.remove(get)

canonical = []
for k in sorted(certain):
    canonical.append(certain[k])
print("part2:")
print(",".join(canonical))
    
                



