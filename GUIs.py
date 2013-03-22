#GUIs.py
#GUIs
#19/03/2013
#Raitis Kupce

from tkinter import *
from demonstrator import *


class TaskGUI():
    def __init__(self,master):
        '''Display all the answers in GUIs'''

##	frm1 = Frame(master, bg='lightgrey')
##	frm2 = Frame(master)
##	Label(frm1, font='mono -36 bold',bg='lightgrey', text="Raitis Kupce App").pack(side=TOP)
##	frm1.pack(side=TOP, fill=BOTH)
##	Label(frm2,text='File name: ', font='cornsilk ').grid(row=10, column=2)
##	frm2.pack(side=LEFT)
        
        Label(master, font='mono -36 bold', text="Raitis Kupce App").grid(row=1, column=3,columnspan=1,)
        TitleSpace = Label(master,height=3).grid(row=2)
        Label(master,text='File name: ', font='cornsilk ').grid(row=3, column=1, sticky=E)
        self.filename = Entry(master,width=15, bg="cornsilk")
        self.filename.grid(row=3, column=2, sticky=E)
        FileSpace = Label(master,height=3).grid(row=4)
        Label(master,text='Assignment Question',font='arial -20 bold').grid(row=5,column=3)
        Label(master,text='Answers', font='arial -20 bold').grid(row=5,column=4,sticky=E)
        Label(master, text='Q1 Find the sum of the values in the field [length] more than or equal to (  6.346).  ', font='arial -20 bold').grid(row=6, column=3,)
        self.Q1 = Label(master, width=10, bg='lightblue')
        self.Q1.grid(row=6, column=4,sticky=E)
        Label(master, text='Q2 What percentage of the numbers in [mark] lie between (52) and (123) inclusive.', font='arial -20 bold').grid(row=7, column=3)
        self.Q2 = Label(master, width=10, bg='lightblue')
        self.Q2.grid(row=7, column=4,sticky=E)
        Label(master, text="Q3 (sell's) are what percentage of the field [action]", font='arial -20 bold').grid(row=8, column=3, sticky=W)
        self.Q3 = Label(master, width=10, bg='lightblue')
        self.Q3.grid(row=8, column=4, sticky=E)
        Label(master, text='Q4 Find the average of the values in the field [count]', font='arial -20 bold').grid(row=10, column=3, sticky=W)
        self.Q4 = Label(master, width=10, bg='lightblue')
        self.Q4.grid(row=10, column=4, sticky=E)
        Label(master, text="Q5 How many values in the 'code' field do not match the format [X9]9XX9#9?", font='arial -20 bold').grid(row=12, column=3, sticky=W)
        self.Q5 = Label(master, width=10, bg='lightblue')
        self.Q5.grid(row=12, column=4, sticky=E)
        Label(master, text='Q6 What percentage of strings have the value (Ebony) in the field [tree]?', font='arial -20 bold').grid(row=14, column=3, sticky=W) 
        self.Q6 = Label(master, width=10, bg='lightblue')
        self.Q6.grid(row=14, column=4, sticky=E)
        Label(master, text='Q7 Count the lines where length is more than 2.223 *or* count is less than 742', font='arial -20 bold').grid(row=16, column=3, sticky=W)
        self.Q7 = Label (master, width=10, bg='lightblue')
        self.Q7.grid(row=16, column=4, sticky=E)
        
        Button(master, text="Process",width=10,font='mono -15 bold',bg='lightgreen',
               command=self.process_file).grid(row=3, column=3)
        Button(master, text='QUIT', fg='red', font='arial -15 bold', command=master.destroy).grid(row=20, column=4)

        #Layout manager
        #MVC pattern
    def process_file(self, ev=None):
        filename = self.filename.get()

        if filename == '3124749a.csv' or '3124749b.csv' or '3124749b.csv' :
            self.ok = True
            self.reader=Demonstrator(filename)
            self.notify()
        
    def notify(self):
        self.Q1['text'] = str(self.reader.displayQ1()) 
        self.Q2['text'] = str(self.reader.displayQ2())
        self.Q3['text'] = str(self.reader.displayQ3())
        self.Q4['text'] = str(self.reader.displayQ4())
        self.Q5['text'] = str(self.reader.displayQ5())
        self.Q6['text'] = str(self.reader.displayQ6())
        self.Q7['text'] = str(self.reader.displayQ7())


if __name__ == "__main__":
    top =Tk()
    top.geometry("1200x800")
    top.title("Raitis Kupce Assignment")
    top.grid()

    app = TaskGUI(top)

    top.mainloop()
