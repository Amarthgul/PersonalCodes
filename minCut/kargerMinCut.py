import random
import copy
import numpy as np

'''This implementation is extremly slow, 
   about 0.09s for a graph with 200 vertices,
   that is to say, it'll take 18s to iterate 200 times...
   '''

def randomContraction(inList):
    if isinstance(inList, list):
        nodes = {}; num = []
        inList = np.array(inList)
        for i in inList:
            nodes[i[0]] = i[1:]
    elif isinstance(inList, dict):
        nodes = copy.deepcopy(inList)

    while len(nodes) > 2:
        vOne = random.choice(list(nodes.keys()))
        vTwo = random.choice(list(nodes[vOne]))
        nodes[vOne].extend(nodes[vTwo])

        for i in nodes[vTwo]:
            nodes[i].remove(vTwo)
            nodes[i].append(vOne)
        while vOne in nodes[vOne]: nodes[vOne].remove(vOne)
        del nodes[vTwo]
        
    return len(list(nodes.values())[0])

'''
input "inList" can either be a dict like:
{ 1: [2, 3, 6],
  2: [1, 8, 7],
  3: [1, 7, 5],
  ... }
or a list like:
[[1, 2, 3, 6],
 [2, 1, 8, 7],
 [3, 1, 7, 5],
 ...]
'''
