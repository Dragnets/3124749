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

    def newFile(self,filename):
        self.process.reset()
        self.reader.FileReader(filename,self.process)
        self.reader.run()
    
    def displayResults(self):
        print (self.process.showAnswer())

print("These are the files available to you: \nA= 3124749a.csv\nB= 3124749b.csv\nC= 3124749c.csv")
files=input("\nPlease choose the file from above available to you A,B or C: ")
a = Demonstrator("3124749"+files+".csv")
a.displayResults()



