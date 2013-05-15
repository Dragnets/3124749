#process.py
#26.February 2013
#Assignment
#Raitis Kupce

class Process():
    ''' Works out all the answers for each question,
    comments refers to a question.'''
    
    def __init__ (self,):
        self.reset()               #calls resets method 
        self.find_action = "sell"  #Q3
        self.find_tree = "ebony"   #Q6

    def reset(self):
        '''Resets all fields to 0'''
        
        self.total  = 0            #Q1
        self.whole  = 0
        self.markPart = 0          #Q2
        self.actionPart  = 0       #Q3
        self.actionPerc  = 0
        self.summ      = 0         #Q4
        self.countMean = 0         
        self.match     = 0         #Q5  
        self.treePart  = 0         #Q6
        self.treePerc  = 0
        self.linePart  = 0         #Q7
        
        
    def percentage(self,part,whole):
        '''Works out percentage taking two argument whole and part.'''
        
        if whole == 0:
            return 0
        return (part/whole)*100

    def runProcess(self,length,mark,action,count,code,tree):
        ''' Run all question in one go'''
        
        self.findLengthSum (length)
        self.percentageOfMark(mark)
        self.percentageOfAction (action)
        self.meanCount(count)
        self.codeMatch(code)
        self.percentageOfTree (tree)
        self.countLine(length,count)
        self.whole +=1              # Counts how many rows
        
    def workOut(self):
        '''This method works out percentage and mean'''
        
        self.markPerc = self.percentage(self.markPart,self.whole) #Q2 Works out percentage 
        self.actionPerc = self.percentage(self.actionPart, self.whole)#Q3
        if self.summ == 0 or self.whole == 0:       #Q4
            self.countMean= 0  # To avoid of error if 0
        else:
            self.countMean = self.summ/self.whole
        self.treePerc = self.percentage(self.treePart,self.whole) #Q6

    def findLengthSum (self,length): #Q1
        '''finds the sum in [length] which is more than or equal to (6.346)'''
        
        if length >= 6.346:
            self.total +=length # add to field self.total if condition is true
    def get_Length(self): return self.total

    def percentageOfMark (self,mark): #Q2
        '''What Percentage of mark lies between 52 and 123 inclusive?'''
        
        if mark >= 52 and mark <= 123:
            self.markPart +=1 
    def get_Mark(self): return self.markPerc

    def percentageOfAction (self,action): #Q3
        '''Works out percentage of given value from field action'''
        
        if action.lower() == self.find_action.lower():
            self.actionPart +=1
    def get_Action(self): return self.actionPerc

    def meanCount(self, count): #Q4
        '''Finds average of given field'''
        
        self.summ += count 
    def get_Count(self): return self.countMean

    def codeMatch(self,code): #Q5
        '''Search how many valid format'''
        
        import re
        if re.search (r'\[[A-Z][0-9]+\][0-9]+[A-Z]{2}[0-9]+#[0-9]+', code) is None:
            self.match +=1  # counts how many regular expresion format match found
    def get_Match(self): return self.match
        
    def percentageOfTree(self,tree): #Q6
        '''What percentage of given string is in the field tree?'''
        
        if tree.lower() == self.find_tree.lower():
            self.treePart +=1
    def get_Tree(self): return self.treePerc
        
    def countLine(self,length, count): #Q7
        '''Counts lines where [length] is more than 2.223 or [count] is lees than 742'''
        
        if length > 2.223 or count < 742:
            self.linePart +=1
    def get_LineCount(self): return self.linePart

    def showAnswer(self):
        return ('''
\n\bQ1 Find the sum of the values in the field [length] more than or equal to (6.346)\nThe sum is: %0.3f
\n\bQ2 What percentage of the numbers in [mark] lie between (52) and (123) inclusive?\nThe answer is: %0.0f 
\n\bQ3 (sell's) are what percentage of the field [action]?\nThe answer is: %0.0f
\n\bQ4 Find the average of the values in the field [count]\nThe answer is: %0.2f
\n\bQ5 How many values in the 'code' field do not match the format [X9]9XX9#9?\nThe answer is: %d
\n\bQ6 What percentage of strings have the value (Ebony) in the field [tree]?\nThe answer is: %d
\n\bQ7 Count the lines where length is more than 2.223 *or* count is less than 742.\nThe answer is: %d
'''% (self.total, self.markPerc, self.actionPerc, self.countMean, self.match, self.treePerc, self.linePart ))
 
