import numpy as np
import pickle

import sys
#resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)


def creatMarkDict(numberOfNodes, initValue = False):
    markerDict = {}
    for i in np.arange(1, numberOfNodes+1):
        markerDict[i] = initValue
    return markerDict

def DFS(graph, startNode = 0):
    print('\ndealing node {}'.format(startNode))
    global nodesProcessed
    global explored
    global finishingTime
    explored[startNode] = True
    currentLeader = startNode

    #if startNode in graph:
    #    for neighbor in graph[startNode]:
    #        print('{}: {}'.format(neighbor, explored[neighbor]), end = '--')
    #print('')

    if startNode in graph:
        for neighbor in graph[startNode]:
            if not explored[neighbor]:
                print('Node {} of {}'.format(neighbor, startNode))
                DFS(graph, neighbor)
                print('finished {}'.format(neighbor))
    else: return currentLeader
    
    nodesProcessed += 1
    finishingTime[startNode] = nodesProcessed
    print('Return checkpoint')
    return currentLeader

def DFS_Loop(graph, order = []):
    global nodesProcessed
    global explored
    global finishingTime
    leaders = []; nodesProcessed = 0
    for index in order:
        if index not in explored: pass
        if not explored[index]:
            leaders.append(DFS(graph, index))
    return leaders


#====================================================
'''==============================================='''
#====================================================


print('Reading file...')
with open('graphRev', 'rb') as f:
    graphRev = pickle.load(f)
numberOfNodes = 875714 #already know that
print('File read: {}\n{} Nodes'.format(graphRev, numberOfNodes))



print('\n\nReverse looping...')
explored = creatMarkDict(numberOfNodes, False)
finishingTime = creatMarkDict(numberOfNodes, 0)
nodesProcessed = 0
DFS_Loop(graphRev, np.arange(numberOfNodes, 0, -1))
print('ReverseLoop finishingTime: \n{}'.format(finishingTime))

