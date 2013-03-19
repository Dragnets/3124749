#process.py
#26.February 2013
#Assignment
#Raitis Kupce

class Process():
    ''' Works out all the answers for each qustion, commens refers to a question.'''
    def __init__ (self,):
        self.total  = 0            #Q1
        self.whole  = 0
        self.markPart = 0          #Q2
        self.find_action = "sell"  #Q3
        self.actionPart  = 0
        self.actionPerc  = 0
        self.summ      = 0         #4
        self.countMean = 0         
        self.match     = 0         #5
        self.find_tree = "ebony"   #6
        self.treePart  = 0
        self.treePerc  = 0
        self.linePart  = 0         #7
        
        
    def percentage(self,part,whole):
        '''Works out percentage taking two argument whole and part.'''
        if whole == 0:
            return 0
        return (part/whole)*100

    def runProcess(self,length,mark,action,count,code,tree):
        self.findLengthSum (length)
        self.percentageOfMark(mark)
        self.percentageOfAction (action)
        self.meanCount(count)
        self.codeMatch(code)
        self.percentageOfTree (tree)
        self.countLine(length,count)
        self.whole +=1
        
    def findLengthSum (self,length): #Q1
        if length >= 6.346:
            self.total +=length

    def percentageOfMark (self,mark): #Q2                 
        if mark >= 52 and mark <= 123:
            self.markPart +=1

    def percentageOfAction (self,action): #Q3
        if action.lower() == self.find_action:
            self.actionPart +=1

    def meanCount(self, count): #4
        self.summ += count

    def codeMatch(self,code): #Q5
        import re
        if re.search (r'\[[A-Z][0-9]+\][0-9]+[A-Z]{2}[0-9]+#[0-9]+', code) is None:
            self.match +=1
        
    def percentageOfTree(self,tree):
        if tree.lower() == self.find_tree:
            self.treePart +=1
        
    def countLine(self,length, count):
        if length > 2.223 or count < 742:
            self.linePart +=1

    def reset(self):
        self.total  = 0            #Q1
        self.whole  = 0
        self.markPart = 0          #Q2
        self.actionPart  = 0       #Q3
        self.actionPerc  = 0
        self.summ      = 0         #4
        self.countMean = 0         
        self.match     = 0         #5  
        self.treePart  = 0         #6
        self.treePerc  = 0
        self.linePart  = 0         #7
        
    
    def showAnswer(self):
        self.markPerc = self.percentage(self.markPart,self.whole)
        self.treePerc = self.percentage(self.treePart,self.whole)
        self.countMean = self.summ/self.whole
        self.actionPerc = self.percentage(self.actionPart, self.whole)
        return ('''
\n\bQ1 Find the sum of the values in the field [length] more than or equal to (6.346)\nThe sum is: %0.3f
\n\bQ2 What percentage of the numbers in [mark] lie between (52) and (123) inclusive?\nThe answer is: %0.0f 
\n\bQ3 (sell's) are what percentage of the field [action]?\nThe answer is: %0.0f
\n\bQ4 Find the average of the values in the field [count]\nThe answer is: %0.2f
\n\bQ5 How many values in the 'code' field do not match the format [X9]9XX9#9?\nThe answer is: %d
\n\bQ6 What percentage of strings have the value (Ebony) in the field [tree]?\nThe answer is: %d
\n\bQ7 Count the lines where length is more than 2.223 *or* count is less than 742.\nThe answer is: %d
'''% (self.total, self.markPerc, self.actionPerc, self.countMean, self.match, self.treePerc, self.linePart ))
 
