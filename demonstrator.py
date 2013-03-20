#3124749.py
#21.February 2013
#Assignment
#Raitis Kupce

from process import Process
from filereader import FileReader
       
class Demonstrator():

    def __init__(self,filename):
        self.process = Process()
        self.reader = FileReader(filename,self.process)
        self.reader.run()
        #self.TaskGUI.notify()

    def newFile(self,filename):
        self.process.reset()
        self.reader.FileReader(filename,self.process)
        self.reader.run()
    
    def displayResults(self):
        print (self.process.showAnswer())

    def displayQ1(self): return '%0.3f'% (self.process.get_Length())
    def displayQ2(self): return '%0.0f%%'% (self.process.get_Mark())
    def displayQ3(self): return '%0.0f%%'% (self.process.get_Action())
    def displayQ4(self): return '%0.2f'% (self.process.get_Count())
    def displayQ5(self): return '%d'% (self.process.get_Match())
    def displayQ6(self): return '%d%%'% (self.process.get_Tree())
    def displayQ7(self): return '%d'% (self.process.get_LineCount())
##
##print("These are the files available to you: \nA= 3124749a.csv\nB= 3124749b.csv\nC= 3124749c.csv")
##files=input("\nPlease choose the file from above available to you A,B or C: ")
####a = Demonstrator(files)
##a = Demonstrator("3124749"+files+".csv")
##a.displayResults()
