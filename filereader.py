#filereader.py
#21.February 2013
#Raitis Kupce

class FileReader():
    '''Reads csv files'''
    
    def __init__(self, filename, process):
        self.process = process      # Refference of object
        self.filename = filename

    def run(self):
        ''' Open file and puts fields into local variable then
        send those variables to a method runProcess'''
        
        theFile = open(self.filename, 'r')  # Opens file by given name
        theFile.readline()                  # Skips first line
        for line in theFile:
            field = line.strip().split(',') # Split on comma
            length = float(field[0])
            mark   = int(field[1])          # Puts into fields
            action = field[2]
            count  = int(field[3])
            code   = field[4]
            tree   = field[5]
            
            self.process.runProcess(length,mark,action,count,code,tree,)
        theFile.close()


