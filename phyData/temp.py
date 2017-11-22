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
        
#=======================================================================        
'''=================================================================='''  
def horPlot():
    I_S = np.arange(0.1, 0.85, 0.1)
    U_1_0 = np.array([7.1, 9.8, 12.4, 15, 17.6, 20.2, 22.8, 25.4])
    U_1_1 = np.array([-2.3, 0.2, 2.8, 5.4, 7.9, 10.5, 13.1, 15.6])

    dataGram = dataPlot()
    dataGram.limBorder = True
    dataGram.xLim = [0, 0.9]; dataGram.yLim = [-3, 26]
    dataGram.xStripMaj = 0.2; dataGram.xStripMin = 0.02
    dataGram.yStripMaj = 5; dataGram.yStripMin = 0.5
    dataGram.addGrid()
    dataGram.ax.plot(I_S, U_1_0, 'o', markerfacecolor = 'w', zorder = 5,
                     markeredgecolor = 'r', markeredgewidth = 1.5)
    #dataGram.ax.plot(I_S, U_1_0, 'b-', zorder = 4)
    dataGram.ax.plot(I_S, U_1_1, 'o', markerfacecolor = 'w', zorder = 5,
                     markeredgecolor = 'r', markeredgewidth = 1.5)
    dataGram.addRefLine(paraAxis = 'x', value = 0.5)
    slo1, int1 = dataGram.addLinearSample(sampleList = list(zip(I_S, U_1_0)), 
                             samplePoint = [0, len(I_S)-1], color = 'b')
    slo2, int2 = dataGram.addLinearSample(sampleList = list(zip(I_S, U_1_1)), 
                             samplePoint = [0, len(I_S)-1], color = 'm')
    dataGram.showPlot()

#=======================================================================        
'''=================================================================='''      
def phyExp():
    f = np.array([1122, 1322, 1522, 1552, 1582, 1612, 1642, 1672, 1702, 1902, 2102])
    U_R = np.array([0.88, 1.52, 3.2, 4, 4.16, 4.2, 4.14, 3.72, 3.18, 1.6, 1])
    I = (U_R / 2) / 20; I *= 1000
    print(I)
    print(len(f), len(I))
    plotSam = dataPlot()
    plotSam.xData = f
    plotSam.yData = I
    plotSam.figureSize = [6, 4.5]; plotSam.ovaScale = 1.5
    plotSam.xLim = [1000, 2200]; plotSam.yLim = [0, 110]
    plotSam.xStripMaj = 200; plotSam.xStripMin = 20
    plotSam.yStripMaj = 20; plotSam.yStripMin = 2
    plotSam.xLabel = r'$f/Hz$'; plotSam.yLabel = r'$I/mA$'
    plotSam.creatPlot('-k')
    plotSam.addGrid()
    plotSam.ax.plot(f, I, 'o', markerfacecolor = 'w', markeredgecolor = 'r',
                    zorder = 10, markeredgewidth = 1.5)
    plotSam.ax.plot(np.repeat(1522, 10) ,np.linspace(0, I[2], 10), '--r',
                    linewidth = 1.5, zorder = 5)
    plotSam.ax.plot(np.repeat(1702, 10) ,np.linspace(0, I[8], 10), '--r',
                    linewidth = 1.5, zorder = 5)
    plotSam.ax.plot(np.repeat(1612, 10) ,np.linspace(0, I[5], 10), '--r',
                    linewidth = 1.5, zorder = 5)
    #for spine in plotSam.ax.spines.values(): 
        #spine.set_edgecolor('r')
    #plotSam.ax.tick_params(axis = 'x', color = 'r')
    plotSam.showPlot()
def lagInt():
    import scipy.interpolate as inte
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([1, 2, 3, 4, 5])
    plo = inte.lagrange(x, y)
    fun = np.poly1d(plo)
    xnew = np.linspace(1, 5, 100)
    
    plotSam = dataPlot()
    plotSam.xData = xnew
    plotSam.alp = 0.25
    plotSam.yData = fun(xnew)
    plotSam.figureSize = [5, 4]; plotSam.ovaScale = 1.5
    plotSam.limBorder = True
    plotSam.xLim = [0.5, 5.5]; plotSam.yLim = [0, 20]
    plotSam.xStripMaj = 1; plotSam.xStripMin = 0.1
    plotSam.yStripMaj = 2; plotSam.yStripMin = 0.2
    plotSam.creatPlot('-k')
    plotSam.addGrid()
    
    plotSam.ax.plot(x, y, 'o', markerfacecolor = 'w', markeredgecolor = 'r',
                    zorder = 5, markeredgewidth = 1.5)
                    
    with open('data.txt', 'a+') as f:
        for i in range(5):
            y[4] += i**2
            para = inte.lagrange(x, y)
            fun = np.poly1d(para)
            plotSam.ax.plot(xnew, fun(xnew), label = '$x_{5}=$'+str(y[4]))    
            plotSam.ax.plot(x[4], fun(x[4]), 'o', markerfacecolor = 'w', 
                            markeredgecolor = 'r', zorder = 5, markeredgewidth = 1.5)
            f.write(str(inte.lagrange(x, y)) + '\n')
            f.write('X[4]=' + str(y[4]) + '\n\n')
    plotSam.addLegend()
    plotSam.showPlot()
    #print(1.208 - 12.08 + 42.29 - 59.42 + 29)
    print(plo)
    

if __name__ == '__main__':
    horPlot()
