def depthFirstSearch(problem):
    '''
    Writing in the provided logic without any API is completely bullshit
    '''
    closedset = set()
    startPoint = problem.getStartState()
    openset = [startPoint] # openset starts with starting state
    parents = dict({})

