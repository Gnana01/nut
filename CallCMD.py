from abc import ABC,abstractmethod
from Repository import Repository

class Call_CMD():
    @abstractmethod
    def initiate():
        pass
    @abstractmethod
    def add():
        pass
    @abstractmethod
    def commit():
        pass
    @abstractmethod
    def getlog():
        pass

class Initiate(Call_CMD):
    def initiate(self):
        self.path = Repository()
        #self.path.makeRepo()
        print(f"initiated the nut at {self.path.gitDir()}")

class Add(Call_CMD):
    def add(self,file):
        self._file = file
        return f"added {self._file} to the local repository"

class Commit(Call_CMD):
    def commit(self,cmmtMssg):
        self._cmmtMssg = cmmtMssg
        self.log_cmt()
    def log_cmt(self):
        self._log = Log()
        self._log.push(self._cmmtMssg)

class Log(Call_CMD):
    stack = []
    @classmethod
    def push(cls,mssg):
        cls.stack.append(mssg)
    @classmethod
    def getLog(cls):
        print(cls.stack.pop())

i = Initiate()
i.initiate()
