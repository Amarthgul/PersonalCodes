pool = ["TATACAT",
        "AGCTGTTTTCGTT",
        "CACTCCATTTTA",
        "CATTTTAGCTGTT",
        "TTTCGTTATACAT",
        "CTGTTTTCGTTA"]

class genome:
    def __init__(self, inStr):
        self.sequence = inStr
        
    def firstN(self, n):
        return self.sequence[:n]
    def lastN(self, n):
        return self.sequence[len(self.sequence) - n :]
    def concatenate(self, new, n, targeting = "head"):
        if targeting == "head":
            self.sequence = self.sequence + new[n :];
        elif targeting == "tail":
            self.sequence = new + self.sequence[n :]
    
class genomeSoup:
    def __init__(self, inStrList):
        self.genomes = self.__generate(inStrList)
        
    def __deleteGen(self, inStr):
        for gen in self.genomes:
            if gen.sequence == inStr:
                self.genomes.remove(gen)
    def __findBest(self, inGen, targeting = "head"):
        bestfit = "null";
        fitLength = 0;
        for gen in self.genomes:
            if inGen.sequence == gen.sequence: pass
            else:
                if targeting == "head":
                    for i in range(1, len(gen.sequence)):
                        if inGen.lastN(i) == gen.firstN(i):
                            if i > fitLength:
                                fitLength = i;
                                bestfit = gen.sequence;
                elif targeting == "tail":
                    for i in range(1, len(gen.sequence)):
                        if inGen.firstN(i) == gen.lastN(i):
                            if i > fitLength:
                                fitLength = i;
                                bestfit = gen.sequence;
        return [bestfit, fitLength];                        
    def __generate(self, inStrList):
        result = [];
        for gen in pool:
            result.append(genome(gen))
        return result

    def disp(self, printLine = True, additionalMessage = None):
        if printLine: print("============" 
                            + ("====" if additionalMessage == None else additionalMessage)
                            + "=============") 
        for gen in self.genomes : print(gen.sequence) 
        if printLine: print("=============================") 
    def combine(self):
        self.disp(additionalMessage = "before iteration")
        while (True):
            bestGuess = ["null", 0]; bestIndex = 0;
            
            for i in range(len(self.genomes)):
                tempGuess = self.__findBest(self.genomes[i], "head")
                
                if tempGuess[1] > bestGuess[1]: 
                    bestIndex = i;
                    bestGuess = tempGuess;

            print(self.genomes[bestIndex].sequence, "'s best head best: ", bestGuess)
            self.genomes[bestIndex].concatenate(bestGuess[0], bestGuess[1], targeting = "head")
            self.__deleteGen(bestGuess[0])
            self.disp(additionalMessage = "after iteration")
            if len(self.genomes) == 1 or bestGuess[0] == "null": break
            
            
soup = genomeSoup(pool)
soup.combine()
soup.disp(additionalMessage = "result")
