#import callCMD
import typer
from repository import Repository
from callCMD import Call_CMD

class Nut():
    def __init__(self):
        self.obj = Repository()
        return self.obj.printDir

def main():
    nut = Nut()
    print(nut.obj)



if __name__ == "__main__":
    main()
    




