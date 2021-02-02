start = problem.getStartState()
    
    nextLayer = []
    visited = []
    visited.append(start)
    nodeWithPath = [(start, [], 0)] 

    while nodeWithPath:
        print("-------------------------> current mdoes ", nodeWithPath)
        for (currentNode, path, layer) in nodeWithPath:
            if problem.isGoalState(currentNode):
                print("-------------------------> result: ", path)
                return path
            
            for (child, action, cost) in problem.getSuccessors(currentNode):
                print("-------------------------> get succ ", child, action, cost)
                if child not in visited:
                    nextLayer.append((child, path + [action], layer + 1))

            visited.append(nodeWithPath.pop()[0])
        
            
        for (child, action, layer) in nextLayer:
            print("-------------------------> translate to nextLayer ", child, action, cost)
            nodeWithPath.append((child, action, layer))
        nextLayer = []
