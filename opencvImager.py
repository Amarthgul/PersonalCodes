class opencvImager():

    def __init__(self, loc = 'abs'):
        self._path = None
        self._images = []
        self._imgLoc = []
        self._imgType = ['png', 'jpg', 'bmp']
        self.mode = 'pos' # or neg
        self.method = loc # or direct path
        self.OS = 'windows' # or unix
    
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
    def path(self):
        if self.OS == 'windows': sep = '\\'
        else: sep = '/'
        self.method = self.method.lower()
        if self.method == 'abs':
            current = str(os.path.abspath(__file__))
            for itera in range(len(current) - 1, 0, -1):
                if current[itera] == sep:
                    dir = current[0: itera]#Get current directory
                    break;
            self._path = dir
        else:
            self._path = self.method
        return self._path
    @property
    def images(self):
        files = os.listdir(self.path)
        for _ in files:
            for ext in self.imgType:
                if re.match(r'.*\.'+ str(ext) + '', _):
                    self._images.append(_); break
        return self._images
    @property
    def imgLoc(self):
        for _ in self.images:
            self._imgLoc.append(self.path + _)
        return self._imgLoc
