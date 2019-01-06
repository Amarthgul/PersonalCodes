def colorCube(step = 32):
    ''' plot a 3D RGB color cube
step: sample rate between 0 to 255. By default, this value is set to 32 for a moderate amount of calculation
    '''
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    start = 0;
    end = 255;
    fontSize = 15
    plotSize = 6.5
    pointSize = 30

    plt.figure(figsize = (plotSize, plotSize))
    ax3D = plt.axes([0.05, 0.05, 0.9, 0.9], projection = '3d')
    for zValue in range(start, end, step):
        for xValue in range(start, end, step):
            for yValue in range(start, end, step):
                RGB = '#%02x%02x%02x' % (xValue, yValue, zValue);
                ax3D.scatter(xValue, yValue, zValue, c = RGB, s = pointSize)

    ax3D.set_xlabel('$Red Value$', fontsize = fontSize)    
    ax3D.set_ylabel('$Blue Value$', fontsize = fontSize)    
    ax3D.set_zlabel('$Green Value$', fontsize = fontSize)  
      
    plt.show()
    

def main():
    colorCube()

if __name__ == '__main__':
    main()
