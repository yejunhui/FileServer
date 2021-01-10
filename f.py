import os
import time

class F():

    def __init__(self):
        filePath = str(os.getcwd())

        if 'files' in os.listdir(filePath):
            pass
        else:
            os.mkdir(filePath+'/files')

        self.filePath = filePath + '/files'

    def fSava(self,f,fName):
        f.savs(self.filePath+fName)

