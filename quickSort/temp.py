def depthFirstSearch(problem):
    '''
    Writing in the provided logic without any API is completely bullshit
    '''
    closedset = set()
    startPoint = problem.getStartState()
    openset = [startPoint] # openset starts with starting state
    parents = dict({})

    while len(openset) > 0:
        state = openset.pop() # get most-recently-added element from openset
        closedset.add(state)
        # ...
        if problem.isGoalState(state) :
            actions = []

            while state != startPoint:
                for i in parents: 
                    if state in parents[i]: 
                        parent = i
                for (next_state, action, cost) in problem.getSuccessors(parent):
                    if next_state == state:
                        actions.append(action)
                state = parent
            actions.reverse()
            return actions
        else:
            if problem.getSuccessors(state): parents[state] = []

            for (next_state, action, cost) in problem.getSuccessors(state):
                if next_state not in closedset:
                    openset.append(next_state)
                    parents[state].append(next_state)
