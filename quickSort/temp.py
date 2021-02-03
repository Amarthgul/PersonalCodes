
    start = problem.getStartState()
    
    nextLayer = []
    visited = []
    visited.append(start)
    nodeWithPath = [(start, [], 0)] 

    while nodeWithPath:
        #print("-------------------------> current layer ", nodeWithPath, len(nodeWithPath))
        for (currentNode, path, layer) in nodeWithPath:
            print("-------------------------> current node ", currentNode)
            if problem.isGoalState(currentNode):
                print("-------------------------> found it : ")
                return path
            
            for (child, action, cost) in problem.getSuccessors(currentNode):
                print("-------------------------> ---- get Successors ", child)
                if child not in visited:
                    nextLayer.append((child, path + [action], layer + 1))

            visited.append(currentNode)
            nodeWithPath.remove((currentNode, path, layer))
            
        
            
        for (child, action, layer) in nextLayer:
            #print("-------------------------> ---- translate to nextLayer ", child, action, cost)
            nodeWithPath.append((child, action, layer))
        nextLayer = []
