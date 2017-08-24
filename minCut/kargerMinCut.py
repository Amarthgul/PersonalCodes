def randomContraction(inList):
    nodes = {}
    inList = np.array(inList)
    for i in inList:
        nodes[i[0]] = i[1:]
    

    while len(nodes) > 2:
        #print(nodes)
        vOne = random.choice(list(nodes.keys()))
        #print('choose {} connect {}'.format(vOne, list(nodes[vOne])))#====
        vTwo = random.choice(list(nodes[vOne]))
        #print('choose {}'.format(vTwo))#====
        nodes[vOne].extend(nodes[vTwo])

        for i in nodes:
            if vTwo in nodes[i]: nodes[i].append(vOne)
            while vTwo in nodes[i]: nodes[i].remove(vTwo)
        while vOne in nodes[vOne]: nodes[vOne].remove(vOne)
        del nodes[vTwo]
        #print(' ')#====

    #print(nodes)
    biNodes = [i for i in nodes]
    return len(nodes[biNodes[0]])+len(nodes[biNodes[1]])
