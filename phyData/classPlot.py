import matplotlib.pyplot as plt
import numpy as np


class dataPlot():
    def __init__(self):
        self.ovaScale = 1
        self.xData = []
        self.yData = []
        self.xLim = [0, 10]
        self.yLim = [0, 10]
        self.limBorder = True
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

    def calGamma(self, x = [], y = []):
        if not x: x = self.xData; 
        if not y: y = self.yData
        x = np.array(x); y = np.array(y)
        numerator = (x*y).mean() - x.mean() * y.mean()
        denominator = ((x**2).mean() - (x.mean())**2)
        denominator *= ((y**2).mean() - (y.mean())**2)
        return numerator / np.sqrt(denominator)

    def creatPlot(self, *args):
        if len(self.xData) and len(self.yData):
            self.ax.plot(self.xData, self.yData, *args)

    def addGrid(self, autoFit = True, intense = 1):
        def getDiv(inList):
            listRange = max(inList) - min(inList)
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
            return listRange * 10 ** (counter - 1) * (1.0/intense)
            
        if autoFit:
            self.xStripMaj = getDiv(self.xData)
            self.xStripMin = self.xStripMaj / 10
            self.yStripMaj = getDiv(self.yData)
            self.yStripMin = self.yStripMaj / 10
        
        self.ax.xaxis.set_major_locator(plt.MultipleLocator(self.xStripMaj))
        self.ax.yaxis.set_major_locator(plt.MultipleLocator(self.yStripMaj))
        self.ax.grid(which='major', axis='x', zorder = self.gridLayer,
                     linewidth=self.xStripMajWid * self.ovaScale, 
                linestyle='-', color = self.gridColor, alpha = self.alp)
        self.ax.grid(which='major', axis='y', zorder = self.gridLayer,
                     linewidth=self.yStripMajWid * self.ovaScale, 
                linestyle='-', color = self.gridColor, alpha = self.alp)       
        if self.biStrip:
            self.ax.yaxis.set_minor_locator(plt.MultipleLocator(self.yStripMin))
            self.ax.xaxis.set_minor_locator(plt.MultipleLocator(self.xStripMin))
            self.ax.grid(which='minor', axis='y', zorder = self.gridLayer, 
                         linewidth=self.yStripMinWid * self.ovaScale, 
                         linestyle='-', color = self.gridColor, alpha = self.alp)
            self.ax.grid(which='minor', axis='x', zorder = self.gridLayer,
                         linewidth=self.xStripMinWid * self.ovaScale, 
                         linestyle='-', color = self.gridColor, alpha = self.alp)
        
    def addLegend(self, loc = 'best', rounded=True, alpha=0.75, 
                  enableShadow = False, legTitle = None, colume = 1):
        self.ax.legend(loc = 'best', fancybox = rounded, framealpha = alpha,
                       shadow = enableShadow, title = legTitle, ncol = colume)

    def addScatterPoint(self, x = [], y = [], pointType = 'o', zDepth = 5,
                        faceColor = 'w', edgeColor = 'r', edgeWidth = 1.5,
                        markerSize = 7.5, pLabel = 'DataPoints'):
        if not x : x = self.xData
        if not y: y = self.yData
        self.ax.plot(x, y, pointType, markerfacecolor = faceColor, label = pLabel,
                     markeredgecolor = edgeColor, markeredgewidth = edgeWidth,
                     markersize = markerSize*self.ovaScale, zorder = zDepth)

    def addRegressLine(self, x = [], y = [], times = 1, division = 10, 
                       lineWidth = 1, lineType = 'r-', regLabel = 'regression'):
        if not x : x = self.xData
        if not y: y = self.yData
        para = np.polyfit(x, y, times)
        equ = np.poly1d(para)
        newX = np.linspace(x[0], x[len(x)-1], division)
        self.ax.plot(newX, equ(newX), lineType, linewidth = lineWidth)
        return para

    def addLinearSample(self, sampleList = [], startPoint = None, endPoint = None,
                        samplePoint = [], extend = False, color = 'r', lineWidth = 1):
        if sampleList: 
            startPoint = list(sampleList[samplePoint[0]])
            endPoint = list(sampleList[samplePoint[1]])
            print(startPoint, endPoint)
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

    def addRefLine(self, paraAxis = 'x', value = 0, thick = 1.5, color = 'r',
                   showDigit = True, zDepth = 1):
        dataOne = [value, value]; 
        dataTwo = [self.xLim[0], self.xLim[1]] if paraAxis == 'x' else [self.yLim[0], self.yLim[1]]
        modifier = (self.xLim[1] - self.xLim[0]) / 20 if paraAxis == 'x' else (self.yLim[1] - self.yLim[0]) / 20
        xPos = 0-modifier if paraAxis == 'x' else value
        yPos = value if paraAxis == 'x' else 0-modifier

        if paraAxis == 'y': dataOne, dataTwo = dataTwo, dataOne
        self.ax.plot(dataTwo, dataOne, linestyle = '--', color = color,
                        linewidth = thick, zorder = zDepth)
        self.ax.text(xPos, yPos, str(value))
        return 0
        
    def addTextBox(self, posX = None, posY = None, offsetX = 0, offsetY = 0,
                   content = 'Hello World', opacity = 0.7, Size = 20, zDepth = 10):
        if not posX: posX = (max(self.xData) + min(self.xData)) / 2
        if not posY: posY = (max(self.yData) + min(self.yData)) / 2
        posX += offsetX; posY += offsetY
        boxStyle = dict(facecolor='white', edgecolor='red', 
                        boxstyle='round,pad=1', alpha = opacity)
        self.ax.text(posX, posY, content, bbox = boxStyle, fontsize = Size,
                     zorder = zDepth)
        
    def showPlot(self):
        if self.plotTitle != None:
            plt.title(self.plotTitle, fontsize = self.labelFontSize*1.25*self.ovaScale)
        if self.figureSize != None:
            plt.rcParams["figure.figsize"] = (self.figureSize[0]*self.ovaScale,
                self.figureSize[1]*self.ovaScale)
        plt.yticks(fontsize = self.labelFontSize*0.55*self.ovaScale)
        plt.yticks(fontsize = self.labelFontSize*0.6*self.ovaScale)
        plt.xlabel(self.xLabel, fontsize = self.labelFontSize*self.ovaScale)
        plt.ylabel(self.yLabel, fontsize = self.labelFontSize*self.ovaScale)
        if self.limBorder:
            plt.xlim(self.xLim[0], self.xLim[1])
            plt.ylim(self.yLim[0], self.yLim[1])
        plt.show()
        
