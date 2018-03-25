import numpy as np
import matplotlib.pyplot as plt
import cv2

def generate(fftRes, precision = 1., loops=1):

    length = len(fftRes) * loops
    stop = int(len(fftRes) * precision)
    if stop < 1: stop = 1
    X = loops * np.arange(0, length, 1.0) / length * (2 * np.pi)
    index = np.arange(0, stop, 1)
    real = fftRes.real; imag = fftRes.imag
    
    Y = np.multiply(real, np.cos(np.outer(index, X)))
    Y -= np.multiply(imag, np.sin(np.outer(index, X)))
    Y = np.sum(Y, axis = 1)
    
    return X, Y
def maintainOffset(X, Y, oriX, oriY):
    
    X *= ((np.max(oriX) - np.min(oriX)) / (np.max(X) - np.min(X)))
    X -= (X[0] - oriX[0])
    Y *= ((np.max(oriY) - np.min(oriY)) / (np.max(Y) - np.min(Y)))
    Y -= (Y[0] - oriY[0])
    return X, Y


def readImage(imageName, maxResolution = 512):
    img = cv2.imread(imageName)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = img.shape
    while height > maxResolution or width > maxResolution:
        img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
        height /= 2; width /= 2
    return img
def detectEdgeImg(img, lowerBound = 30, upperBound = 100, 
                  autoBound = True, showImg = False):

    if autoBound:
        upperBound, thresh_im = cv2.threshold(img, 0, 255, 
             cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        lowerBound = 0.5 * upperBound
    canny = cv2.Canny(img, lowerBound, upperBound)

    if showImg:
        cv2.imshow('img', canny)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return canny

def constructLines(binaryImgMatrix, valueForTrue = 255):

    locX, locY = np.where(binaryImgMatrix == valueForTrue)
    print(locX)
    pointList = np.ones((len(binaryImgMatrix), len(binaryImgMatrix[0]))) * np.inf 
    print('Shape of image: {}'.format(pointList.shape))
    for x, y in zip(locX, locY):
        pointList[x][y] = 1

    print('Finished Shape of image: {}'.format(pointList.shape))
    exploredMarker = pointList.copy() - 1

    exploredMarker = pointList.copy() - 1

    print(exploredMarker)
    print(pointList)

def stream():
    imgList = ['twilight.png', 'canT.jpg']
    img = readImage(imgList[1])
    edgeImg = detectEdgeImg(img, showImg = False)

    constructLines(edgeImg)
    print('Img Shape: {}'.format(edgeImg.shape))

def toCoord(picture, recordedValue = 255):
    '''Convert binary image into coordinates'''
    picture = np.squeeze(picture)
    x, y = np.where(picture == recordedValue)
    return x, y

def main():
    import timeit
    try:
        start = timeit.default_timer()
        #-----------------------------------------------------

        stream()

        #-----------------------------------------------------
        end = timeit.default_timer()
        total = end - start
        print('Time costed:',total)

    except () as err:
        print('Error!',err)
    finally:
        print('----------END----------')
    return 0;

if __name__ == '__main__':
    main()
