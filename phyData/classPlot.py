import matplotlib.pyplot as plt
import numpy as np
import math
import re


'''=================================================='''
#=======================================================

class phydata():
    def __init__(self, value, delta = 0.1, C = 1.46):
        self.value = np.array(value)
        self._delta = delta
        self._C = C
        self.summing = np.sum(self.value)
        self.average = np.mean(self.value)
        self.biggest = np.max(self.value)
        self.smallest = np.min(self.value)
        self.length = len(self.value)
        self.unity = 'cm'

    @property
    def C(self): return self._C
    @property
    def delta(self): return self._delta
    @property
    def uncerB(self): return self.delta / self.C
    @property
    def uncerA(self):
        if len(self.value) == 1: return 0
        else:
            return np.sqrt(np.sum((self.value - self.average)**2) 
                           / (self.length * (self.length - 1)))

    @property
    def uncertainty(self):
        return np.sqrt(self.uncerA**2 + self.uncerB**2)
    @property
    def relativeUncertainty(self): 
        '''That's percentage'''
        return 100 * self.uncertainty / self.average

    def getPara(self, *args):
        '''args: unwanted parameters'''
        parameters = {
            'value': self.value,
            'delta': self.delta,
            'c': self.C,
            'sum': self.summing,
            'average': self.average,
            'biggest': self.biggest,
            'smallest': self.smallest,
            'uncertainty a': self.uncerA,
            'uncertainty b': self.uncerB,
            'uncertainty': self.uncertainty,
            'relative uncertainty':self.relativeUncertainty}
        for _ in args:
            try: _ = _.lower()
            except TypeError as err: print(err)
            if _ in parameters: del parameters[_]
        return parameters
    def strPara(self, inDict, addUnity = True):
        '''I strongly suggest you to use getPara() as input'''
        order = ['value', 'delta', 'c', 'sum', 'average', 'biggest', 'smallest', 
                 'uncertainty a', 'uncertainty b', 'uncertainty', 'relative uncertainty']
        unity = [self.unity, self.unity, '', self.unity,self.unity, self.unity, self.unity,
                 self.unity, self.unity, self.unity, '%']
        outStr = ''
        for item in inDict.items():
            if item[0] in order:
                order[order.index(item[0])] = '{}{}:{} {}\n'.format(item[0],
                    ' '*((15 - len(item[0])) if len(item[0])<15 else 0), item[1],
                    unity[order.index(item[0])] if addUnity else '')
        for _ in order:
            if ':' not in _: del order[order.index(_)]
            else: outStr += _
        return outStr
    def stdResult(self):
        '''Unfinished'''
        return '''
\left\{\begin{matrix}
{}
\\ 
{}
\end{matrix}\right.
        '''.format()        
#=======================================================================        
'''=================================================================='''  
class dataPlot():
    def __init__(self, inputX = [], inputY = []):
        self.ovaScale = 1
        self._xData = inputX
        self._yData = inputY
        self.xLim = [0, 10]
        self.yLim = [0, 10]
        self.limBorder = False
        self.xLabel = 'X'
        self.yLabel = 'Y'
        self.plotTitle = None
        self.figureSize = None
        self.axesPara = None
        self.labelFontSize = 15
        self.type = 'o'
        self.gridColor = 'r'
        self.gridLayer = 0
        self.alp = 0.5
        self.biStrip = True
        self.xStripMaj = 1
        self.xStripMin = 0.1
        self.yStripMaj = 1
        self.yStripMin = 0.1
        self.xStripMajWid = 1
        self.xStripMinWid = 0.5
        self.yStripMajWid = 1
        self.yStripMinWid = 0.5
        
        #self.fig = plt.figure(figsize = self.figureSize)
        self.ax = plt.axes() if not self.axesPara else plt.axes(self.axesPara)

    @property
    def xData(self):
        return np.squeeze(self._xData)
    @property 
    def yData(self):
        return np.squeeze(self._yData)

    def _getDiv(self, inList):
        listRange = max(inList) - min(inList)
        #print(listRange)#=============================
        counter = 0
        while True:
            if listRange > 10:
                listRange /= 10.0; counter += 1
            elif listRange <1:
                listRange *= 10.0; counter -= 1
            else: 
                listRange = 10
                break
        listRange = round(listRange)
        return listRange * 10 ** (counter - 1)

    def calGamma(self, x = [], y = []):
        '''Linear dependence of 2 sets'''
        if not len(x): x = self.xData 
        if not len(y): y = self.yData
        x = np.array(x); y = np.array(y)
        numerator = (x*y).mean() - x.mean() * y.mean()
        denominator = ((x**2).mean() - (x.mean())**2)
        denominator *= ((y**2).mean() - (y.mean())**2)
        return numerator / np.sqrt(denominator)    
    def sciFormat(self, num, precision = 4, upperBound = 1000, lowerBound = 0.01):
        '''Convert to Scitific format if necessary'''
        sci = '{:.'+str(precision)+'e}'
        norm = '{:.'+str(precision)+'f}'
        if num > upperBound or num < lowerBound: return sci.format(num)
        return norm.format(num)    
    def creatPlot(self, *args):
        '''Literally Useless'''
        if len(self.xData) and len(self.yData):
            self.ax.plot(self.xData, self.yData, *args)

    def addGrid(self, autoFit = True, xIntense = 1, yIntense = 1, lineWidthMult = 1):
        '''add grid to the background
        xIntense: scaler to modify how dense the grid is
        yIntense: same as xIntense, but in y axis
        '''   
        if autoFit:
            if len(self.xData) == 0: self._xData = [0, 10]; self._yData = [0, 10]
            self.xStripMaj = self._getDiv(self.xData) * xIntense
            self.xStripMin = self.xStripMaj / 10
            self.yStripMaj = self._getDiv(self.yData) * yIntense
            self.yStripMin = self.yStripMaj / 10
            #self.xLim = [min(self.xData) - self.xStripMaj/2, max(self.xData) + self.xStripMaj/2]
            #self.yLim = [min(self.yData) - self.yStripMaj/2, max(self.yData) + self.yStripMaj/2]
            #print(self.xLim, self.yLim)

        self.ax.xaxis.set_major_locator(plt.MultipleLocator(self.xStripMaj))
        self.ax.yaxis.set_major_locator(plt.MultipleLocator(self.yStripMaj))
        self.ax.grid(which='major', axis='x', zorder = self.gridLayer,
                     linewidth=self.xStripMajWid * self.ovaScale * lineWidthMult, 
                linestyle='-', color = self.gridColor, alpha = self.alp)
        self.ax.grid(which='major', axis='y', zorder = self.gridLayer,
                     linewidth=self.yStripMajWid * self.ovaScale * lineWidthMult, 
                linestyle='-', color = self.gridColor, alpha = self.alp)       
        if self.biStrip:
            self.ax.yaxis.set_minor_locator(plt.MultipleLocator(self.yStripMin))
            self.ax.xaxis.set_minor_locator(plt.MultipleLocator(self.xStripMin))
            self.ax.grid(which='minor', axis='y', zorder = self.gridLayer, 
                         linewidth=self.yStripMinWid * self.ovaScale * lineWidthMult, 
                         linestyle='-', color = self.gridColor, alpha = self.alp)
            self.ax.grid(which='minor', axis='x', zorder = self.gridLayer,
                         linewidth=self.xStripMinWid * self.ovaScale * lineWidthMult, 
                         linestyle='-', color = self.gridColor, alpha = self.alp)
        
    def addLegend(self, loc = 'best', rounded=True, alpha=0.75, Size = 15,
                  enableShadow = False, legTitle = None, colume = 1):
        self.ax.legend(loc = 'best', fancybox = rounded, framealpha = alpha,
                       shadow = enableShadow, title = legTitle, ncol = colume,
                       fontsize = Size * self.ovaScale)

    def addScatterPoint(self, x = [], y = [], pointType = 'o', zDepth = 5,
                        faceColor = 'w', edgeColor = 'r', edgeWidth = 1.5,
                        markerSize = 7.5, Label = 'DataPoints', connected = True):
        if not len(x): x = self.xData
        if not len(y): y = self.yData
        self.ax.plot(x, y, pointType, markerfacecolor = faceColor, 
                     markeredgecolor = edgeColor, markeredgewidth = edgeWidth,
                     markersize = markerSize*self.ovaScale, zorder = zDepth,
                     label = Label if not connected else None)
        if connected:
            self.ax.plot(x, y, '-', color = edgeColor, label = Label,
                     linewidth = edgeWidth *self.ovaScale, zorder = zDepth - 1)

                     
    def calRegression(self, x = [], y = [], times = 1):
        if not x : x = self.xData
        if not y: y = self.yData
        return np.polyfit(x, y, times)
      
    def addRegressLine(self, para = [], start = None, end = None, division = 20, 
                       lineWidth = 1, lineType = 'r-', Label = 'regression', 
                       precision = 4):
        if not start: start = self.xData[0]
        if not end: end = self.xData[len(self.xData)-1]
        if not len(para): 
            para = self.calRegression()
            Label = 'Slope:     {}\n'.format(self.sciFormat(para[0], precision)) + \
            'Intercept: {}\n'.format(self.sciFormat(para[1], precision)) + \
            '$\gamma$' + ':             {}'.format(
            self.sciFormat(self.calGamma(self.xData, self.yData), precision))
        equ = np.poly1d(para)
        newX = np.linspace(start, end, division)
        self.ax.plot(newX, equ(newX), lineType, linewidth = lineWidth, label = Label)

    def addLinearSample(self, sampleList = [], startPoint = None, endPoint = None,
                        samplePoint = [], extend = False, color = 'r', lineWidth = 1):
        if sampleList: 
            startPoint = list(sampleList[samplePoint[0]])
            endPoint = list(sampleList[samplePoint[1]])
            #print(startPoint, endPoint)
        if startPoint == None or endPoint == None:
            self.ax.text((max(self.xData) + min(self.xData)) / 2, 
                         (max(self.yData) + min(self.yData)) / 2, 
                         "INVALID SAMPLING")
            return 0, 0
        else:
            slope = (endPoint[1] - startPoint[1])/(endPoint[0] - startPoint[0])
            intercept = startPoint[1] - slope*startPoint[0]
            xRange = [self.xLim[0], self.xLim[0]] if extend else [startPoint[0], endPoint[0]]
            xRange = np.array(xRange)
            yValue = slope * xRange + intercept
            self.ax.plot(xRange, yValue, c = color, linewidth = lineWidth)
        return slope, intercept

    def addRefLine(self, value, start=0, end=10, paraAxis = 'x', thick = 1.5, color = 'r',
                   showDigit = True, zDepth = 1, Label = 'ref'):
        dataOne = [value, value]; 
        dataTwo = [start, end]
        modifier = (self.xLim[1] - self.xLim[0]) / 20 if paraAxis == 'x' else (self.yLim[1] - self.yLim[0]) / 20
        xPos = 0-modifier if paraAxis == 'x' else value
        yPos = value if paraAxis == 'x' else 0-modifier

        if paraAxis == 'y': dataOne, dataTwo = dataTwo, dataOne
        self.ax.plot(dataTwo, dataOne, linestyle = '--', color = color,
                        linewidth = thick, zorder = zDepth, label = Label)
        if showDigit:
            self.ax.text(xPos, yPos, str(value))
        return 0
        
    def addTextBox(self, posX = None, posY = None, offsetX = 0, offsetY = 0,
                   content = 'Hello World', opacity = 0.7, Size = 15, zDepth = 10):
        if not posX: posX = (max(self.xData) + min(self.xData)) / 2
        if not posY: posY = (max(self.yData) + min(self.yData)) / 2
        posX += offsetX; posY += offsetY
        boxStyle = dict(facecolor='white', edgecolor='k', 
                        boxstyle='round,pad=1', alpha = opacity)
        self.ax.text(posX, posY, content, bbox = boxStyle, zorder = zDepth,
                     fontsize = Size * self.ovaScale)
        
    def generatePlot(self):

        if not self.limBorder:
            self.xLim = [min(self.xData) - self._getDiv(self.xData)/2,
                         max(self.xData) + self._getDiv(self.xData)/2]
            self.yLim = [min(self.yData) - self._getDiv(self.yData)/2,
                         max(self.yData) + self._getDiv(self.yData)/2]

        tickFontSizeScaler = 0.75
        if self.plotTitle != None:
            plt.title(self.plotTitle, fontsize = self.labelFontSize*1.25*self.ovaScale)
        if self.figureSize != None:
            plt.rcParams["figure.figsize"] = (self.figureSize[0]*self.ovaScale,
                self.figureSize[1]*self.ovaScale)
        plt.xticks(fontsize = self.labelFontSize * tickFontSizeScaler * self.ovaScale)
        plt.yticks(fontsize = self.labelFontSize * tickFontSizeScaler * self.ovaScale)
        #if the label is None or False, not displayed
        if self.xLabel: plt.xlabel(self.xLabel, fontsize = self.labelFontSize*self.ovaScale) 
        if self.yLabel: plt.ylabel(self.yLabel, fontsize = self.labelFontSize*self.ovaScale)
        plt.xlim(self.xLim[0], self.xLim[1])
        plt.ylim(self.yLim[0], self.yLim[1])
            
    def showPlot(self):
        self.generatePlot()
        plt.show()
    def save(self, name = 'default.png', dpi = 256):
        self.generatePlot()
        plt.savefig(name, dpi = dpi)
#=======================================================================        
'''=================================================================='''  

def helloWorld():
    pass
'''=================================================================='''      

if __name__ == '__main__':
    helloWorld()
