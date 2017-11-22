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

    def creatPlot(self, *args):
        if len(self.xData) and len(self.yData):
            self.ax.plot(self.xData, self.yData, *args)

    def addGrid(self):
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
        
    def addLinearSample(self, sampleList = [], startPoint = None, endPoint = None,
                        samplePoint = [], extend = False, color = 'r', lineWidth = 1):
        if sampleList: 
            startPoint = list(sampleList[samplePoint[0]])
            endPoint = list(sampleList[samplePoint[1]])
            print(startPoint, endPoint)
        if startPoint == None or endPoint == None:
            self.ax.text(0.5, 0.5, "INVALID SAMPLE")
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
                   showDigit = True):
        dataOne = [value, value]; 
        dataTwo = [self.xLim[0], self.xLim[1]] if paraAxis == 'x' else [self.yLim[0], self.yLim[1]]
        modifier = (self.xLim[1] - self.xLim[0]) / 20 if paraAxis == 'x' else (self.yLim[1] - self.yLim[0]) / 20
        xPos = 0-modifier if paraAxis == 'x' else value
        yPos = value if paraAxis == 'x' else 0-modifier

        if paraAxis == 'y': dataOne, dataTwo = dataTwo, dataOne
        self.ax.plot(dataTwo, dataOne, linestyle = '--', color = color,
                        linewidth = thick)
        self.ax.text(xPos, yPos, str(value))
        return 0

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
