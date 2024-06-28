
import re 
import math
import random
import numpy as np
import functools
from enum import Enum

sign = functools.partial(math.copysign, 1)

class Operator (Enum):
    NULL = 0
    ADD = 1
    SUB = 2
    MULTI = 3
    DIV = 4
    POW = 5


class NumericalDecompositorRec:

    def __init__(self, input, depth):
        self.baseNumber = input
        self.depth = depth # Maximum depth of recursion
        self.leftOperand = 0
        self.rightOperand = 0
        self.remainder = 0
        self.operator = Operator.NULL
        self.result = ""
        self.maxRandAttempt = 50 # Set a bound when trying to generate random numbers
        self.DEBUG = False

        self.Run()

    def Run(self):
        self.leftOperand = self.baseNumber

        # When depth is not reaching the bottom, keep recursion
        if (self.depth > 0):
            # Choose an operator and split the number into two
            self._SelectOperator()
            self._Decompose()

            # When there is 0, set right to zero and keep recursion
            if (self.rightOperand == 0):
                self.operator = Operator.NULL
            elif (self.leftOperand == 0):
                self.leftOperand = self.rightOperand
                self.rightOperand = 0
                self.operator = Operator.NULL
            else:
                self.rightOperand = NumericalDecompositorRec(self.rightOperand, self.depth - 1)

            # Left will also be recursed
            self.leftOperand = NumericalDecompositorRec(self.leftOperand, self.depth - 1)

            # Non zero remainder also get to enter the recursion
            if (self.remainder != 0):
                self.remainder = NumericalDecompositorRec(self.remainder, self.depth - 1)


    def _SelectOperator(self):
        self.operator = Operator(random.randrange(1, 6))

        # Overwrite 1 with subtraction to reduce them populating downstream
        if(abs(self.leftOperand) == 1):
            self.operator = Operator.SUB


    def _Decompose(self):
        splitSeed = random.random()
        leftSign = sign(self.leftOperand)

        # ======================================================================
        # Addition, divide the right and then subtract it from the base to get left
        if(self.operator == Operator.ADD):
            self.rightOperand = int(self.leftOperand * splitSeed)
            self.leftOperand = self.baseNumber - self.rightOperand
            # Repeat to avoid 0 addition
            while (self.rightOperand == 0 and self.leftOperand > 1):
                splitSeed = random.random()
                self.rightOperand = int(self.leftOperand * splitSeed)
                self.leftOperand = self.baseNumber - self.rightOperand
        # ======================================================================
        # Subtraction, make right bigger and then subtract base to get left
        elif(self.operator == Operator.SUB):
            self.leftOperand = int(self.baseNumber / splitSeed)
            self.rightOperand = self.leftOperand - self.baseNumber
            while (self.leftOperand == 1 or self.rightOperand == 1):
                splitSeed = random.random()
                self.leftOperand = int(self.baseNumber / splitSeed)
                self.rightOperand = self.leftOperand - self.baseNumber
        # ======================================================================
        # Multiplication, reduce left and find a right that matches, may result in remainder
        elif(self.operator == Operator.MULTI):
            self.leftOperand = int(self.leftOperand * splitSeed) + 1 * leftSign
            self.rightOperand = int(self.baseNumber / self.leftOperand)
            # Radomize and reduce multiplication by 1
            currentAttempt = 1
            while((self.leftOperand == 1 or self.rightOperand == 1)
                and currentAttempt < self.maxRandAttempt):
                splitSeed = random.random()
                self.leftOperand = int(self.leftOperand * splitSeed) + 1 * leftSign
                self.rightOperand = int(self.baseNumber / self.leftOperand)
                currentAttempt += 1

            self.remainder = self.baseNumber - self.leftOperand * self.rightOperand
        # ======================================================================
        # Division, multiply left with a number and use that number as the right
        elif(self.operator == Operator.DIV):
            maxDivider = 100.0
            self.leftOperand = abs(self.leftOperand)
            self.leftOperand = int(self.leftOperand * int(1.0/splitSeed))
            self.rightOperand = int(self.leftOperand / self.baseNumber)
            # Radomize and reduce division by 1
            currentAttempt = 1
            while((self.rightOperand == 1 or self.leftOperand == 1) and
                  currentAttempt < self.maxRandAttempt):
                splitSeed = random.random()
                self.leftOperand = int(self.baseNumber * int(1.0 / splitSeed ))
                self.rightOperand = int(self.leftOperand / self.baseNumber) # Is 1.0 / splitSeed
                currentAttempt += 1

        # ======================================================================
        # Power, starting from square and go up, likely to produce remainder
        # TODO: modify algorithm to reduce power of 1
        elif(self.operator == Operator.POW):
            currentRoot = 2.0
            self.leftOperand = leftSign * int(abs(self.baseNumber) ** (1. / currentRoot))
            self.rightOperand = currentRoot
            self.remainder = self.baseNumber - self.leftOperand ** self.rightOperand

            currentAttempt = 1
            while(abs(self.remainder) < abs(self.leftOperand) and currentAttempt < self.maxRandAttempt):
                currentRoot += 1
                self.leftOperand = leftSign *int(abs(self.baseNumber) ** (1. / currentRoot))
                self.rightOperand = currentRoot
                self.remainder = self.baseNumber - self.leftOperand ** self.rightOperand
                currentAttempt += 1

        if(self.DEBUG):
            print("Left operand: ", self.leftOperand)
            print("Right operand: ", self.rightOperand)
            print("Remainder: ", self.remainder)
            print("Operator: ", self._OperatorToString())



    def _IsOperator(self, oType):
        if(oType == -1 or self.remainder != 0): # is any non null operator
            return self.operator != Operator.NULL
        else:
            return self.operator == oType

    # If any of the child contains certain operator
    def _ChildContainOperator(self, oType):
        if (self.depth == 0): # Leaf node
            return False
        elif (self._IsOperator(oType)): # this node alread contains the operator
            return True
        else:  # inqury the children
            result = self.leftOperand._ChildContainOperator(oType)
            if (isinstance(self.rightOperand, NumericalDecompositorRec)):
                result = result or self.rightOperand._ChildContainOperator(oType)
            if (isinstance(self.remainder, NumericalDecompositorRec)):
                result = result or self.remainder._ChildContainOperator(oType)
        return result


    def _OperatorToString(self):
        if (self.operator == Operator.ADD):
            return "+"
        elif (self.operator == Operator.SUB):
            return "-"
        elif (self.operator == Operator.MULTI):
            return "*"
        elif (self.operator == Operator.DIV):
            return "/"
        elif (self.operator == Operator.POW):
            return "^"

    def _LeftToString(self):
        if (self.depth == 0):
            result = str(int(self.leftOperand))
        else:
            result = self.leftOperand.ToString()
        return result

    def _RightToString(self):
        if (self.depth == 0):
            return str(int(self.leftOperand))
        if (self.operator == Operator.SUB and self.rightOperand._ChildContainOperator(-1)):
            return "(" + self.rightOperand.ToString() + ")"
        else:
            return self.rightOperand.ToString()

    def _RemainderToString(self):
        if (isinstance(self.remainder, NumericalDecompositorRec)):
            result = self.remainder.ToString()
            if(self.remainder._IsOperator(-1)):
                return "+(" + result + ")"
            elif (result[0] == "-"):
                return result
            else:
                return "+" + result
        return ""

    def ToString(self):
        self.result = ""
        if (self.depth == 0):
            self.result = str(int(self.leftOperand))
        elif(self.operator == Operator.NULL):
            self.result = self._LeftToString()
        # Multiplication 
        elif(self.operator == Operator.MULTI):
            if (self.leftOperand._ChildContainOperator(Operator.ADD) or self.leftOperand._ChildContainOperator(Operator.SUB)):
                self.result = "("+ self._LeftToString() + ")"
            else:
                self.result = self._LeftToString()
            if (self.rightOperand._ChildContainOperator(Operator.ADD) or self.rightOperand._ChildContainOperator(Operator.SUB)):
                self.result += self._OperatorToString() + "(" + self._RightToString() + ")"  + self._RemainderToString()
            else:
                self.result += self._OperatorToString() + self._RightToString()  + self._RemainderToString()
        # Division 
        elif(self.operator == Operator.DIV):
            if (self.leftOperand._ChildContainOperator(-1)):
                self.result = "("+ self._LeftToString() + ")"
            else:
                self.result = self._LeftToString()
            if (self.rightOperand._ChildContainOperator(-1)):
                self.result += self._OperatorToString() + "(" + self._RightToString() + ")"  + self._RemainderToString()
            else:
                self.result += self._OperatorToString() + self._RightToString()  + self._RemainderToString()
        # Power 
        elif(self.operator == Operator.POW):
           # if (self.leftOperand._ChildContainOperator(-1) and eval(self._LeftToString().replace("^", "**")) == 1):
                #self.result = "1" + self._RemainderToString()
            #el
            if (self.rightOperand._ChildContainOperator(-1)):
                self.result = "("+ self._LeftToString() + ")" + self._OperatorToString() + "(" + self._RightToString() + ")"  + self._RemainderToString()
            else:
                self.result += "("+ self._LeftToString() + ")" + self._OperatorToString() + self._RightToString()  + self._RemainderToString()
        else:
            self.result = self._LeftToString() + self._OperatorToString() + self._RightToString() + self._RemainderToString()

        return self.result

    #def ApplyPostFilterIte(self, input, pattern, replacementDict):
        #return re.sub(pattern, replacementDict, input)

    def ApplyPostFilter(self):
        replacementDict = {
            "(1)": "cos(2*π)"
        }
        result = self.ToString()
        for (key, value) in replacementDict.items():
            result = result.replace(key, value)
        return result

    def PrintCheck(self):
        temp = self.ToString()
        print("Raw content type: ", type(temp))
        print("Content     : ", temp)
        print("Replacment 1: ", self.ApplyPostFilter()) # This variable is only for use in debuger
        if (eval(temp.replace("^", "**")) == self.baseNumber):
            print(">>>Value check passed<<<")
        #print(temp)


test = NumericalDecompositorRec(162, 14)
print("===============")
test.PrintCheck()
