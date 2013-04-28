#filereader.py
#21.February 2013
#Raitis Kupce

class FileReader():
    '''Reads csv files and puts into variables'''
    def __init__(self, filename, process):
        self.process = process
        self.filename = filename

    def run(self):
        ''' Open file and puts them into variable'''
        
        theFile = open(self.filename, 'r') # Opens file by given name
        theFile.readline()                 # Skips first line
        for line in theFile:
            field = line.split(',')        # Split on comma
            length = float(field[0])
            mark   = int(field[1])         # Puts into fields
            action = field[2]
            count  = int(field[3])
            code   = field[4]
            tree   = field[5].strip()            
    
            self.process.runProcess(length,mark,action,count,code,tree,)
        theFile.close()
