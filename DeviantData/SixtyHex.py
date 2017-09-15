import re
class babs():
    def __init__(self, input = [0, 0, 0]):
        self.maxBit = 3
        self._value = []

    @property
    def value(self): return self._value

    def _add(self, babsOne, babsTwo):
        return (babsOne + babsTwo) % 60, (babsOne + babsTwo) // 60

    def decToBabs(self, decNum): return [decNum//60, decNum%60]
    def babsToDec(self, babsNum): 
        '''Input can either be list or str
        But have to be in form like [12, 34, ...] for list
        And "12 34 ..."(seperated by non-num characters) for str '''
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
        out = [0]

        # 1.) classify data input:
        listNum = []; strNum = []; decNum = 0 
        for var in args:
            if isinstance(var, list): listNum.append(var)
            elif isinstance(var, str): strNum = var
            elif isinstance(var, int): decNum += var
            else: raise ValueError
        # 2.) modify str data:
        if strNum:
            strNum = eval(strNum)
            if isinstance(strNum, list): listNum.extend(var)
            elif isinstance(strNum, int): decNum += var
            elif isinstance(strNum, tuple): decNum += sum(strNum)
            else: raise ValueError

        #print(listNum, strNum, decNum)

        while True:
            higher, lower = self.decToBabs(decNum)
            out[0] = lower; out.insert(0, higher)
            if len(out) >= self.maxBit:
                break
            decNum = higher

        #print(out)
