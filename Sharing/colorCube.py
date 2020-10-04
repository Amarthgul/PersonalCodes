def colorCube(step = 8, mode = 'rgb', pointSize = 150):
    ''' plot a 3D color cube
step: sample rate, higher value requires more timr to sample;
mode: either rgb or hsv;
    '''
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.colors as cls
    from mpl_toolkits.mplot3d import Axes3D

    
    plotSize = 6.5 
    fontSize = 15

    plt.figure(figsize = (plotSize, plotSize))
    ax3D = plt.axes([0.05, 0.05, 0.9, 0.9], projection = '3d')

    #=======================================================
    if mode is 'rgb':
        start = 0;
        end = 255;

        for zValue in np.linspace(start, end, step):
            for xValue in np.linspace(start, end, step):
                for yValue in np.linspace(start, end, step):
                    color = '#%02x%02x%02x' % (int(xValue), int(yValue), int(zValue));
                    ax3D.scatter(xValue, yValue, zValue, c = color, s = pointSize)

        ax3D.set_xlabel('$Red$', fontsize = fontSize)    
        ax3D.set_ylabel('$Green$', fontsize = fontSize)    
        ax3D.set_zlabel('$Blue$', fontsize = fontSize)  
    #=======================================================

    elif mode is 'hsv':
        for hue in np.linspace(0, 360, step):
            for sat in np.linspace(0, 1, step):
                for val in np.linspace(0, 1, step):
                    color = cls.hsv_to_rgb([hue / 360.0, sat, val]).reshape(1,-1)
                    ax3D.scatter(hue, sat, val, c = color, s = pointSize)

        ax3D.set_xlabel('$Hue$', fontsize = fontSize)    
        ax3D.set_ylabel('$Saturation$', fontsize = fontSize)    
        ax3D.set_zlabel('$Value$', fontsize = fontSize)
    #=======================================================
    else:
        raise ValueError("Invalid mode")

    plt.show()
    
    

def main():
    colorCube(step = 10, mode = 'hsv')

if __name__ == '__main__':
    main()
