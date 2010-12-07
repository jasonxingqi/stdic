
from imagefilter import ImageFilter

class PictureNumberFilter(ImageFilter):
    
    def __init__(self, analyzepicturenumber = -1, firstpicturenumber = -1, lastpicturenumber = -1):
        self.analyzepicturenumber = analyzepicturenumber
        self.firstpicturenumber = firstpicturenumber
        self.lastpicturenumber = lastpicturenumber
        
    def filter(self, image):
        picturenumber = int(image.picturenumber)
        if (picturenumber == self.analyzepicturenumber) and (self.analyzepicturenumber != -1):
            return True
        if (picturenumber < self.firstpicturenumber) and (self.firstpicturenumber != -1):
            return False
        if (picturenumber > self.lastpicturenumber) and (self.lastpicturenumber != -1):
            return False
        return True