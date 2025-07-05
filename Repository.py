#import subprocess
import os

class Repository():
    def gitDir(self):
        self.path = os.getcwd()
        return self.path
    def printDir(self):
        print(self.gitDir())
    def makeRepo(self):
        os.mkdir(".nut")


g = Repository()
g.pri
        




