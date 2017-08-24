import os, re, platform
import cv2


class opencvImager():

    def __init__(self, loc = 'abs'):
        self._path = None
        self._images = []
        self._imgLoc = []
        self._imgType = ['png', 'jpg', 'bmp']
        self._sep = None
        self.mode = 'pos' # or neg
        self.method = loc # or direct path
        self.OS = str(platform.system()).lower() # or unix
        self.maxSize = 100   #the biggest edge's pixel after scaled
        self.equalScale = True   #whether it's scaled equally
        self.directScale = [0, 0]   #use a scaler to scale the images


#===========================================================
    @property
    def imgType(self): return self._imgType
    @imgType.setter
    def imgType(self, value):
        for _ in value: self._imgType.append(_)
        self._imgType = list(set(self._imgType))
    def imgTypeOveride(self, newType):
        self._imgType = []
        for _ in newType: self._imgType.append(_)
        self._imgType = list(set(self._imgType))

    @property
    def sep(self): #get seperate based on sys
        if self.OS.lower() == 'windows':
            self._sep = '\\'
        else: self._sep = '/'
        return self._sep
    @property
    def path(self): #get the folder contains pos and neg 
        if self.method == 'abs':
            self._path = os.path.dirname(os.path.realpath(__file__))
        else: self._path = self.method
        return self._path
    @property
    def images(self): #get images' names
        folderPath = self.path + self.sep + self.mode
        if os.path.exists(folderPath):
            files = os.listdir(folderPath)
            for _ in files:
                for ext in self.imgType:
                    if re.match(r'.*\.'+ str(ext) + '', _):
                        self._images.append(_); break      
        return self._images
    @property
    def imgLoc(self): #get the locations of the images
        for _ in self.images:
            self._imgLoc.append(self.path + self.sep + \
                self.mode + self.sep + _)
        return self._imgLoc

    def reSize(self, inlist):
        if self.equalScale:
            smallEdge = int( min(inlist[0], inlist[1]) * self.maxSize / max(inlist[0], inlist[1]))
            if inlist[0] > inlist[1]: return self.maxSize, smallEdge
            elif inlist[0] < inlist[1]: return smallEdge, self.maxSize
            elif inlist[0] == inlist[1]: return self.maxSize, self.maxSize
        else: return self.maxSize, self.maxSize

    def sizeAndOverwrite(self):
        for _ in list(set(self.imgLoc)):
            print('processing:', _, '\n')
            img = cv2.imread(_)
            tarHeight, tarWidth = self.reSize(img.shape[:2])
            if not self.directScale[0]:
                scaled = cv2.resize(img, \
                    (tarWidth, tarHeight), \
                    interpolation = cv2.INTER_CUBIC)
                #cv2.imshow('fuck', scaled); cv2.waitKey(100)
            else:
                scaled = cv2.resize(img, None, \
                    fx = self.directScale[0], \
                    fy = self.directScale[1], \
                    interpolation = cv2.INTER_CUBIC)
                #cv2.imshow('fuck', scaled); cv2.waitKey(100)
            #names = re.findall(r'.*\W(\w*\..*)', str(_))
            os.remove(_)
            cv2.imwrite(_, scaled)
            txtLoc = self.path + self.sep + self.mode
            with open(txtLoc + self.sep + self.mode + r'.txt', 'a') as file:
                file.write(str(_))
                if self.mode == 'pos':
                    file.write(' 1 0 0 {}  {}'.format(tarWidth, tarHeight))
                file.write('\n')
