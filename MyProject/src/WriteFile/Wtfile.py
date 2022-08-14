
class Wt_file:
    def __init__(self,NameLog,mess):
        self.NameLog=NameLog
        self.mess=mess

class WriteLog(Wt_file):
    def WtLog(self):
        self.file1 = open(self.NameLog+".txt","a+") 
        self.file1.write(self.mess + "\n") 
        self.file1.close()
