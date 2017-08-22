'''Set the first element as pivot'''

counter = 0

def quickSortOri(inList):
    global counter; 
    if not inList:
        return []
    else:
        #counter += len(inList) - 1
        pivot = 0
        pivotValue = inList[pivot]
        print('inList: {}'.format(inList)) #------+
        print('Pivot sub:{} with value:{}'.format(pivot, pivotValue)) #------+
        smaller = []; bigger = []
        for i in range(len(inList)):
            if i == pivot: pass
            elif inList[i] <= pivotValue: 
                smaller.append(inList[i]); counter += 1
            else: 
                bigger.append(inList[i]); counter += 1
        print('final list{} and comparison {}'.format(\
            (smaller+[pivotValue]+bigger), counter)) #------+
        print('partition: {} and {}\n'.format(smaller, bigger)) #------+
        lesser = quickSortOri(smaller)
        greater = quickSortOri(bigger)
        return lesser + [pivotValue] + greater

def quickSortImp(inList): #correct
    global counter; 
    length = len(inList); 
    if not inList: return []

    #counter += length - 1
    pivot = 0
    P = inList[pivot]
    print('inList: {}'.format(inList)) #------+
    print('Pivot sub:{} with value:{}'.format(pivot, P)) #------+
    i = pivot + 1
    for j in range(pivot+1, length):
        counter += 1 #correct
        if inList[j] < P:
            inList[j], inList[i] = inList[i], inList[j]
            i += 1; 
    inList[pivot], inList[i-1] = inList[i-1], inList[pivot]
    print('final list{} and comparison {}'.format(inList, counter)) #------+
    print('partition: {} and {} \n'.format(inList[:i-1], inList[i :])) #------+
    return quickSortImp(inList[:i-1]) + [P] + quickSortImp(inList[i :])

def dataReadAndCal():
    numbers = []
    with open('data.txt', 'r') as f:
        for num in f:
            numbers.append(int(num))
    print(numbers)
    sortedArray = quickSortV2(numbers)
    print(sortedArray)
    print('ori array len {}, comparison {}'.format(len(numbers), counter))

def main():
    import timeit
    try:
        start = timeit.default_timer()
        '''-----------'''#------------------------

        print(quickSortImp([1, 53, 9, 3, 8, 36, 7, 4]), \
            counter)


        '''-----------'''#------------------------
        end = timeit.default_timer()
        total = end - start
        print('Time costed:',total)

    except () as err:
        print('Error!',err)
    finally:
        print('----------END----------')

if __name__ == '__main__':
    main()

# result see outputOne.py    
