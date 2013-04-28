#3124749.py
#21.February 2013
#Assignment
#Raitis Kupce

from process import Process
from filereader import FileReader
       
class Demonstrator():
    ''' Runs both files in one go process and filereader '''
    def __init__(self,filename):
        self.process = Process()
        self.reader = FileReader(filename,self.process)
        self.reader.run()
        

    def newFile(self,filename):
        self.process.reset()
        self.reader.FileReader(filename,self.process)
        self.reader.run()
    
    def displayResults(self):
        print (self.process.showAnswer())

    def displayQ1(self): return '%0.2f'% (self.process.get_Length())
    def displayQ2(self): return '%0.2f%%'% (self.process.get_Mark())
    def displayQ3(self): return '%0.2f%%'% (self.process.get_Action())
    def displayQ4(self): return '%0.2f'% (self.process.get_Count())
    def displayQ5(self): return '%d'% (self.process.get_Match())
    def displayQ6(self): return '%0.2f%%'% (self.process.get_Tree())
    def displayQ7(self): return '%d'% (self.process.get_LineCount())
