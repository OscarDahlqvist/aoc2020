import re
import json
import copy 
import llist as ls


# Node class 
class LL: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null

    def nodes(self): 
        acc = []
        temp = self 
        while temp: 
            acc.append(temp)
            temp = temp.next
            if temp == self: 
                acc.append(LL("...Infinite"))
                break
        return acc

    def insert(self,node):
        node.next = self.next
        self.next = node
        return node

    def values(self):
        return [x.data for x in self.nodes()]

    def __str__(self):
        return str(self.values())

f = open("input.txt").read()
ints = [int(x) for x in f]
ints.extend(list(range(max(ints)+1,1000001)))

nCups = len(ints)

nodeTable = [() for x in range(nCups+1)]

print("creating node table")

curr = LL(0)
for x in ints[0:]:
    nodeTable[x] = LL(x)
    curr.next = nodeTable[x]
    curr = curr.next

curr = nodeTable[ints[0]]
nodeTable[ints[-1]].next = curr

print("start iterating")
for i in range(10000000):
    if i % 100000 == 0:
        print(i)

    take = []
    for _ in range(3):
        take.append(curr.next)
        curr.next = curr.next.next
    takeVals = [x.data for x in take]

    destCupValue = ((curr.data-2) % nCups) + 1

    while destCupValue in takeVals:
        destCupValue = ((destCupValue-2) % nCups) + 1
    
    destCup = nodeTable[destCupValue]

    #print(f"picks: {takeVals}") 
    #print(f"dest: {destCupValue}") 
    #print()

    curr = curr.next

    take.reverse()
    for x in take:
        destCup.insert(x)
        
    #print(f"-- move {i+2} --")
    #print(f"cups: {curr.values()}") 
    
node1 = nodeTable[1]
#print("node1:",node1)
d1 = node1.next.data
d2 = node1.next.next.data

#part1
#print("part1","".join([str(x) for x in node1.next.values()[:-2]]))

#part2
print("part2:",d1*d2,d1,d2)