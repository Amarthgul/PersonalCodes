def timeCalcul():
    import re
    class babs():
        def __init__(self, input = [0, 0, 0]):
            self._hour = input[0] #also degree
            self._min = input[1]
            self._sec = input[2]

        @property
        def hour(self): return self._hour
        @property
        def min(self): return self._min
        @property
        def sec(self): return self._sec
        @property
        def value(self): return [self._hour, self._min, self._sec]

        def _add(self, babsOne, babsTwo):
            return (babsOne + babsTwo) % 60, (babsOne + babsTwo) // 60

        def decToBabs(self, decNum): return [decNum//60, decNum%60]
        def babsToDec(self, babsNum): 
            if isinstance(babsNum, list): babsList = babsNum
            if isinstance(babsNum, str):
                babsList = re.findall(r'(\d+)', babsNum)
                babsList = list(map(int, babsList))
            decNum = 0

            for i in range(len(babsList)-1, 0, -1):
                if babsList[i] >= 60: raise ValueError
                decNum = (babsList[i]+decNum) / 60
            decNum += babsList[0]
            return decNum

        def add(self, *args):
            scaler = []; babsNum = []; 

            for var in args:
                if isinstance(var, list): babsNum.append(var)
                #elif isinstance(var, str): single = var
                else: scaler.append(var)

            print(babsNum, scaler)

    a = babs()
    #a.add([12, 23, 34], 45)
    print(a.babsToDec('12, 34, 50'))
    return 0
