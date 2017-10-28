
import matplotlib.pyplot as plt
import numpy as np

class dataPlot():
    def __init__(self):
        self.xData = []
        self.yData = []
        self.xLabel = 'X'
        self.yLabel = 'Y'
        self.type = 'o' 
        self.mainPlotColor = 'red'
        self.gridColor = 'r'
        self.alp = 0.5
        self.xStripMaj = 1
        self.xStripMin = 1
        self.yStripMaj = 0.1
        self.yStripMin = 0.1
        self.xStripMajWid = 1
        self.xStripMinWid = 1
        self.yStripMajWid = 0.1
        self.yStripMinWid = 0.1

    def creatPlot(self, *args):
        fig = plt.figure(figsize = (10, 10))
        ax = plt.axes()
        if self.xData and self.yData:
            ax.plot(xData, yData, *args)

    def addPlot(self, x, y, plotType = None, addLabel = 'Sample'):
        if not plotType:
            ax.plot(x, y, addLabel)
        else:
            ax.plot(x, y, plotType, addLabel)

    def addGrid(self):
        ax.xaxis.set_major_locator(plt.MultipleLocator(self.xStripMaj))
        ax.xaxis.set_minor_locator(plt.MultipleLocator(self.xStripMin))
        ax.yaxis.set_major_locator(plt.MultipleLocator(self.yStripMaj))
        ax.yaxis.set_minor_locator(plt.MultipleLocator(self.yStripMin))
        ax.grid(which='major', axis='x', linewidth=self.xStripMajWid, 
                linestyle='-', color = self.gridColor, alpha = self.alp)
        ax.grid(which='minor', axis='x', linewidth=self.xStripMinWid, 
                linestyle='-', color = self.gridColor, alpha = self.alp)
        ax.grid(which='major', axis='y', linewidth=self.yStripMajWid, 
                linestyle='-', color = self.gridColor, alpha = self.alp)
        ax.grid(which='minor', axis='y', linewidth=self.yStripMinWid, 
                linestyle='-', color = self.gridColor, alpha = self.alp)

    def showPlot(self):
        plt.show()


def plotSam():
    fig = dataPlot()


plotSam()

def phy17_9_25_():
    grid = True; gridColor = 'r'; alp = 0.5; scalar = 1.5
    deltaTemp = np.array([0, 5, 10, 15, 20, 25, 30])
    deltalength = np.array([0, 0.0187, 0.0407, 0.0598, 0.0766, 0.0925, 0.1066])

    fig = plt.figure()
    ax = plt.axes()
    regValue = np.polyfit(deltaTemp, deltalength, 1); print(regValue)
    regress = np.poly1d(regValue)
    texts = r'$Slope$'+' =      '+str(regValue[0])+'\n'+\
            r'$intercept$'+' = '+str(regValue[1])+'\n'+\
            r'$\gamma$'+' =            0.997534736343'
    if grid:
        ax.yaxis.set_major_locator(plt.MultipleLocator(0.01))
        ax.yaxis.set_minor_locator(plt.MultipleLocator(0.001))
        ax.xaxis.set_major_locator(plt.MultipleLocator(3))
        ax.xaxis.set_minor_locator(plt.MultipleLocator(0.3))
        ax.grid(which='major', axis='y', linewidth=1.5*scalar, linestyle='-', color = gridColor, alpha = alp)
        ax.grid(which='minor', axis='y', linewidth=0.75*scalar, linestyle='-', color = gridColor, alpha = alp)
        ax.grid(which='major', axis='x', linewidth=1.5*scalar, linestyle='-', color = gridColor, alpha = alp)
        ax.grid(which='minor', axis='x', linewidth=0.75*scalar, linestyle='-', color = gridColor, alpha = alp)
    ax.plot(deltaTemp, regress(deltaTemp), '-k', 
            linewidth = 2*scalar)
    ax.plot(deltaTemp, deltalength, 'rx', markersize = 20, 
            markeredgewidth = 4)
    ax.text(0.05, 0.95, texts, transform=ax.transAxes, 
            fontsize = 20, verticalalignment='top',
            bbox = dict(boxstyle='round', facecolor='white', alpha=0.9))
    plt.xlabel(r'$\Delta t_{i1} / ^{\circ}{\rm C}$', fontsize = 30)
    plt.ylabel(r'$\Delta L{i1} / mm$', fontsize = 30)
    plt.show()
    
    return 0
