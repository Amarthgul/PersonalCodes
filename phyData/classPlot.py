import matplotlib.pyplot as plt
import numpy as np

class dataPlot():
    def __init__(self):
        self.xData = []
        self.yData = []
        self.xLabel = 'X'
        self.yLabel = 'Y'
        self.limBorder = True
        self.xLim = [0, 10]
        self.yLim = [0, 10]
        self.figureSize = None
        self.axesPara = None
        self.labelFontSize = 15
        self.type = 'o'
        self.gridColor = 'r'
        self.alp = 0.5
        self.biStrip = True
        self.xStripMaj = 1
        self.xStripMin = 0.1
        self.yStripMaj = 1
        self.yStripMin = 0.1
        self.xStripMajWid = 1
        self.xStripMinWid = 0.25
        self.yStripMajWid = 1
        self.yStripMinWid = 0.25
        
        self.fig = plt.figure(self.figureSize)
        self.ax = plt.axes() if not self.axesPara else plt.axes(self.axesPara)
		
    def creatPlot(self, *args):
        if len(self.xData) and len(self.yData):
            self.ax.plot(self.xData, self.yData, *args)

    def addGrid(self):
        self.ax.xaxis.set_major_locator(plt.MultipleLocator(self.xStripMaj))
        self.ax.yaxis.set_major_locator(plt.MultipleLocator(self.yStripMaj))
        self.ax.grid(which='major', axis='x', linewidth=self.xStripMajWid, 
                linestyle='-', color = self.gridColor, alpha = self.alp)
        self.ax.grid(which='major', axis='y', linewidth=self.yStripMajWid, 
                linestyle='-', color = self.gridColor, alpha = self.alp)       
        if self.biStrip:
            self.ax.yaxis.set_minor_locator(plt.MultipleLocator(self.yStripMin))
            self.ax.xaxis.set_minor_locator(plt.MultipleLocator(self.xStripMin))
            self.ax.grid(which='minor', axis='y', linewidth=self.yStripMinWid, 
                linestyle='-', color = self.gridColor, alpha = self.alp)
            self.ax.grid(which='minor', axis='x', linewidth=self.xStripMinWid, 
                linestyle='-', color = self.gridColor, alpha = self.alp)
        
    def showPlot(self):
        plt.xlabel(self.xLabel, fontsize = self.labelFontSize)
        plt.ylabel(self.yLabel, fontsize = self.labelFontSize)
        if self.limBorder:
            plt.xlim(self.xLim[0], self.xLim[1])
            plt.ylim(self.yLim[0], self.yLim[1])
        plt.show()
