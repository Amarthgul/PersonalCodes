
import timeit
import time
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys
#from PythonLearning.Library import cameo 
import sys
sys.path.append(r"WAIT")
import filters
from managers import WindowManager, CaptureManager
import cameo

loc = 'C:\Amarth\Download\openCV\images'
#======================================================
'''================================================='''
def readImg():
    twi = cv2.imread('large.png');
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    #cv2.WINDOW_NORMAL will entitle to resize the window
    cv2.imshow('image', twi)
    while cv2.waitKey(0) != ord('q'):
        pass
    cv2.destroyAllWindows()
    #or use cv2.destroyWindow('WINDOWNAME')
def readAndShowPLT():
    twi = cv2.imread('large.png', 0);
    plt.imshow(twi, cmap = 'gray')
    plt.xticks([]); plt.yticks([])
    plt.show()
def getVideo():# and draw geometry, text
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cap = cv2.VideoCapture(0)
    cap.set(3, 480); cap.set(4, 320); #seems doesn't work
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.line(frame, (0, 0), (int(cap.get(3)), \
            int(cap.get(4))), (0, 0, 255), 1)
        cv2.line(frame, (int(cap.get(3)), 0), (0, \
            int(cap.get(4))), (0, 0, 255), 1) #(b, g, r)
        cv2.circle(frame, (int(cap.get(3)/2), int(cap.get(4)/2)),\
           63, (0, 0, 255), 0 )#The last digit: -1 fill,  0 void
        cv2.putText(frame, 'FuckOpenCV', (10, 50), font,\
           2, (255, 255, 255), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
def recordVideoToAVI():
    cap = cv2.VideoCapture(0)
    fps = 24
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    rec = cv2.VideoWriter('myFucking.avi',\
        cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'),\
        fps, size)
    while True:
        success, frame = cap.read()
        cv2.imshow('frame', frame)
        rec.write(frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release(); cv2.destroyAllWindows()

def cameraCap():
    index = 0; size = 100
    cap = cv2.VideoCapture(0)
    startX = int(cap.get(3)); startY = int(cap.get(4))
    print(startX, startY)
    cap.set(3, 200); cap.set(4, 200); #seems doesn't work
    while True:
        ret, frame = cap.read()
        img = cv2.rectangle(frame, (startY, startY+size), \
            (startX, startX-size), (255, 0, 0), 2)

        cv2.imshow('frame', img)
        
        if cv2.waitKey(1) == ord('q'):
            break
        elif cv2.waitKey(1) == ord('c'):
            cv2.imwrite('photo%s.pgm'%str(index), frame)
            index += 1
    cap.release()
    cv2.destroyAllWindows()

'''======================================================'''
#===========================================================
def videoWithMouseInteract(): #not much success
    global clicked
    clicked = False
    def onMouse(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONUP:
            clicked = True

    cap = cv2.VideoCapture(0)
    cv2.namedWindow('myWindow')
    cv2.setMouseCallback('myWindow', onMouse)
    print('showing camera feed, whatever')
    success = True
    while True:
        success, frame = cap.read()
        cv2.imshow('myWindow', frame)
        if clicked:
            break
    cap.release(); cv2.destroyAllWindows() 
def videoWithMouseInteractversionTwo():
    drawing = False
    mode = True
    ix, iy = -1, -1
    def drawCircle(event, x, y, flags, param):
        global ix, iy, drawing, mode
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing:
                if mode:
                    cv2.rectangle(img, (ix, iy), (x, y),\
                        (0, 255, 0), -1)
                else:
                    cv2.circle(img, (x, y), \
                        5, (0 ,0 ,255), -1)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            if mode:
                cv2.rectangle(img, (x, y), \
                    (0, 255, 0), -1)
'''======================================================'''
#===========================================================

def randImage():
    import os
    randArray = bytearray(os.urandom(120000))
    grayImage = np.array(randArray).reshape(300, 400)
    randArrayLarge = bytearray(os.urandom(360000))
    colorImage = np.array(randArrayLarge).reshape(300, 400, 3)
    cv2.imshow('image', grayImage)
    while cv2.waitKey(0) != ord('q'):
        pass
    cv2.destroyAllWindows()
    cv2.imshow('image', colorImage)
    while cv2.waitKey(0) != ord('q'):
        pass
    cv2.destroyAllWindows()
def brokenTelevision():
    import os
    while True:
        randArrayLarge = bytearray(os.urandom(360000))
        colorImage = np.array(randArrayLarge).reshape(300, 400, 3)
        cv2.imshow('frame', colorImage)
        if cv2.waitKey(2) == ord('q'):
            break
    cv2.destroyAllWindows()
    #set all pixels in one channel: NAME[:, :, CHANNEL] = 0

def highBoostFilterOne():
    from scipy import ndimage
    from scipy import signal
    kernal3 = np.array([[-1, -1, -1],
                        [-1,  8, -1],
                        [-1, -1, -1]])
    kernal5 = np.array([[-1, -1, -1, -1, -1],
                        [-1,  1,  2,  1, -1],
                        [-1,  2,  4,  2, -1],
                        [-1,  1,  2,  1, -1],
                        [-1, -1, -1, -1, -1]])
    img = cv2.imread('large.png', 0)

    k3 = ndimage.convolve(img, kernal3)
    k5 = ndimage.filters.convolve(img, kernal5)
    cv2.imshow('k3' ,k3)
    cv2.imshow('k5', k5)
    blurred = cv2.GaussianBlur(img, (5, 5), 0) 
    #the smaller that argument is,
    #the thinner convloved border will be 
    g_hpf = img - blurred #black tech
    cv2.imshow('img', img)
    cv2.imshow('blur', blurred)
    cv2.imshow('fuck', g_hpf)

    cv2.waitKey()
    cv2.destroyAllWindows()
def convolutionOne():
    kernal = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])
    img = cv2.imread('large.png', 0)
    conv = cv2.filter2D()

def faceDectionOne():
    loc = r'C:\Amarth\Computer_Graphics\Programing\PythonLearning\PythonLearning\SciPy_etc\XMLs'
    locFace = loc + r'\haarcascade_frontalface_alt2.xml'

    faceCascade = cv2.CascadeClassifier(locFace)
    img = cv2.imread('man.jpg')
    img = cv2.resize(img, (500, 500))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('fuckit', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
def faceDectectVidero():
    loc = r'C:\Amarth\Computer_Graphics\Programing\PythonLearning\PythonLearning\SciPy_etc\XMLs'
    locFace = loc + r'\haarcascade_frontalface_alt2.xml'
    locEye = loc + r'\haarcascade_eye.xml'
    faceCascade = cv2.CascadeClassifier(locFace)
    eyeCascade = cv2.CascadeClassifier(locEye)

    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            img = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roiGrey = gray[y: y+h, x: x+w]

            eyes = eyeCascade.detectMultiScale(roiGrey, \
                1.03, 5, 0, (40, 40))
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(img, (ex+x, ey+y), (ex+ew+x, ey+eh+y), \
                    (0, 255, 0), 2)

        cv2.imshow('FUCKING', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    camera.release(); cv2.destroyAllWindows()

def detectBoderPri():
    img = np.zeros((200, 200), dtype = np.uint8)
    img[50:150, 50:150] = 255

    ret, thresh = cv2.threshold(img, 127, 255, 0)
    print(ret)

    #'image' is the modified image
    #'contours' is the image border(corner points)
    #'hierarchy' is their relationship
    image, contours, hierarchy = cv2.findContours(thresh, \
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.RETR_TREE detect multiple borders, and their relationship
    #cv2.RETR_EXTERNAL only finds the outer boder
    #so canbe used more often
    print(contours, hierarchy)
    color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    img = cv2.drawContours(color, contours, -1, \
        (0, 255, 0), 2)
    cv2.imshow('fuck', color)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return 0
def boderDectionTwo():
    img = cv2.pyrDown(cv2.imread('Sample.png', cv2.IMREAD_UNCHANGED))
    ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), \
        cv2.COLOR_BGR2GRAY), 12, 255, cv2.THRESH_BINARY)
    image, contours, hier = cv2.findContours(thresh, \
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x+w, y+h), \
            (0, 255, 0), 2)

        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)#'rect' is float
        cv2.drawContours(img, [box], 0, (0, 0, 255), 3)

        (x, y), radius = cv2.minEnclosingCircle(c)
        center = (int(x), int(y))
        radius = int(radius)
        img = cv2.circle(img, center, radius, (255, 0, 0), 2)
    cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
    #print(contours)
    cv2.imshow('fuck', img)
    cv2.waitKey(); cv2.destroyAllWindows()
    return 0
def boderDectectionTwo():
    img = cv2.pyrDown(cv2.imread('Sample.png', cv2.IMREAD_UNCHANGED))
    ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), \
        cv2.COLOR_BGR2GRAY), 12, 255, cv2.THRESH_BINARY)
    image, contours, hier = cv2.findContours(thresh, \
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]
    #print(cnt)
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    hull = cv2.convexHull(cnt)
    img[:] = 0
    
    cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
    cv2.drawContours(img, [hull], -1, (255, 0, 0), 1)
    cv2.drawContours(img, [approx], -1, (0, 255, 0), 1)
    #use 'hull' and '[hull]' will yeild a different result
    cv2.imshow('fuck', img)
    cv2.waitKey(); cv2.destroyAllWindows()
    return 0

def lineDectection():
    loc = r'C:\Amarth\Download\openCV\chapter3'
    imgLoc = loc + r'\lines.jpg'

    img = cv2.imread(imgLoc)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 100)
    #minLineLength = 20; maxLineGap = 5
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, \
        minLineLength = 10, maxLineGap = 5)
    print(lines[0])
    for [[x1, y1, x2, y2]] in lines:
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
    cv2.imshow('line', img)
    cv2.imshow('shit', edges)
    cv2.waitKey(); cv2.destroyAllWindows()
    return 0
def circleDectection():
    loc = r'C:\Amarth\Download\openCV\chapter3'
    imgLoc = loc + r'\planet_glow.jpg'
    planets = cv2.imread(imgLoc)
    gray = cv2.cvtColor(planets, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 5)
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img, \
        cv2.HOUGH_GRADIENT, 1, 120, param1 = 100, \
        param2 = 30, minRadius = 0, maxRadius = 0)
    circles = np.uint16(circles); print(circles[0])

    for i in circles[0]:
        cv2.circle(planets, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(planets, (i[0], i[1]), 2, (0, 255, 0), 3)
    cv2.imshow('fuck', planets)
    cv2.waitKey(); cv2.destroyAllWindows()
    return 0

def stereoVisionOne():
    windowSize = 5; minDisp = 16; numDisp = 192 - minDisp; blockSize = windowSize
    uniquenessRatio = 1; speckleRange = 3; speckleWindowSize = 3; disp12MaxDiff = 200
    P1 = 600; P2 = 2400

    def update(val = 0):
        stereo.setBlockSize(cv2.getTrackbarPos('windowSize', \
            'disparity'))
        stereo.setUniquenessRatio(cv2.getTrackbarPos(\
            'uniquenessRatio', 'disparity'))
        stereo.setSpeckleWindowSize(cv2.getTrackbarPos(\
            'speckleWindowSize', 'disparity'))
        stereo.setSpeckleRange(cv2.getTrackbarPos(\
            'speckleRange', 'disparity'))
        stereo.setDisp12MaxDiff(cv2.getTrackbarPos(\
            'disp12MaxDiff', 'disparity'))
        print('computing...')
        disp = np.array(stereo.compute(locImageL, locImageR)).astype(np.float32) / 16.0
        #cv2.imshow('left', locImageL)
        cv2.imshow('disparity', (disp - minDisp)/numDisp)
    
    loc = r'C:\Amarth\Download\openCV\chapter3'
    ImageR = loc + r'\color1_small.jpg'; ImageL = loc + r'color2_small.jpg'
    locImageR = cv2.imread(ImageR); locImageL = cv2.imread(ImageL)

    cv2.createTrackbar('speckleRange', 'disparity', \
        speckleRange, 50, update)
    cv2.createTrackbar('windowSize', 'disparity', \
        windowSize, 21, update)
    cv2.createTrackbar('uniquenessRatio', 'disparity', \
        uniquenessRatio, 50, update)
    cv2.createTrackbar('speckleWindowSize', 'disparity', \
        speckleWindowSize, 200, update)
    cv2.createTrackbar('disp12MaxDiff', 'disparity', \
        disp12MaxDiff, 250, update)

    stereo = cv2.StereoSGBM_create(\
        minDisparity = minDisp, \
        numDisparities = numDisp, \
        blockSize = windowSize, \
        uniquenessRatio = uniquenessRatio, \
        speckleRange = speckleRange, \
        speckleWindowSize = speckleWindowSize, \
        disp12MaxDiff = disp12MaxDiff, \
        P1 = P1, P2 = P2)
    update()
    cv2.waitKey()
    return 0

def frontDectionONe():
    imgLoc = loc + r'\statue_small.jpg'
    img = cv2.imread(imgLoc)
    mask = np.zeros(img.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgbModel = np.zeros((1, 65), np.float64)
    rect = (100, 50, 421, 378)
    cv2.grabCut(img, mask, rect, bgdModel, fgbModel, 5, \
        cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')
    img *= mask2[:, :, np.newaxis]

    cv2.imshow('fuck', img); cv2.waitKey(); cv2.destroyAllWindows()
    return 0

'''======================================================'''
#===========================================================
def cvMain():
    try:
        start = timeit.default_timer()
        #------------------------------------------
        
        cameraCap()

        #------------------------------------------
        end = timeit.default_timer()
        print('Time costed:',end - start)
    except (NameError) as err:
        print('Error!',err);

if __name__ == '__main__':
    cvMain();
