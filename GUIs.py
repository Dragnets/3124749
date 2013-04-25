#GUIs.py
#GUIs
#19/03/2013
#Raitis Kupce

from tkinter.filedialog import *
from demonstrator import *
#from tkinter.filedialog import askopenfilename
from tkinter import Tk, StringVar, ttk


class TaskGUI():
    def __init__(self,master):
        '''Display all the answers in GUIs'''

        self.ok = True # Indicate if valid read
        self.browseActive= False
        Label(master, font='mono -36 bold', text="Raitis Kupce App").grid(row=1, column=8,)           
        Label(master,text='File name: ', font='cornsilk ').grid(row=3, column=1, sticky=E)
        self.filename = Entry(master,width=15, bg="cornsilk")
        self.filename.grid(row=3, column=2, sticky=E)
        
        Label(master,width=5).grid(row=3, column=3) #SPACE
        Label(master,width=10).grid(row=3, column=5) # SPACE
        Button(master, text='Browse',width=10,font='mono -15 bold', bg='lightblue',
               command=self.open_file).grid(row=3, column=3, columnspan=4)
        Button(master, text="Process",width=20,font='mono -15 bold',bg='lightgreen',
               command=self.process_file).grid(row=3, column=7, sticky=E)
        Label(master,height=3).grid(row=4) #SPACE
        
        #QUESTIONS BELOW >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        Label(master,text='Assignment Question',font='arial -20 bold').grid(row=5,column=8)
        Label(master,text='Answers', font='arial -20 bold').grid(row=5,column=9,sticky=E)
        Label(master, text='Q1 Find the sum of the values in the field [length] more than or equal to (6.346).  ', font='arial -20 bold').grid(row=6, column=8,)
        self.Q1 = Label(master, width=10, bg='lightblue')
        self.Q1.grid(row=6, column=9,sticky=E)
        Label(master, text='Q2 What percentage of the numbers in [mark] lie between (52) and (123) inclusive.', font='arial -20 bold').grid(row=7, column=8)
        self.Q2 = Label(master, width=10, bg='lightblue')
        self.Q2.grid(row=7, column=9,sticky=E)
        Label(master, text="Q3 (sell's) are what percentage of the field [action]", font='arial -20 bold').grid(row=8, column=8, sticky=W)
        self.Q3 = Label(master, width=10, bg='lightblue')
        self.Q3.grid(row=8, column=9, sticky=E)
        Label(master, text='Q4 Find the average of the values in the field [count]', font='arial -20 bold').grid(row=10, column=8, sticky=W)
        self.Q4 = Label(master, width=10, bg='lightblue')
        self.Q4.grid(row=10, column=9, stick=E)
        Label(master, text="Q5 How many values in the 'code' field do not match the format [X9]9XX9#9?", font='arial -20 bold').grid(row=12, column=8, sticky=W)
        self.Q5 = Label(master, width=10, bg='lightblue')
        self.Q5.grid(row=12, column=9, sticky=E)
        Label(master, text='Q6 What percentage of strings have the value (Ebony) in the field [tree]?', font='arial -20 bold').grid(row=14, column=8, sticky=W) 
        self.Q6 = Label(master, width=10, bg='lightblue')
        self.Q6.grid(row=14, column=9, sticky=E)
        Label(master, text='Q7 Count the lines where length is more than 2.223 *or* count is less than 742', font='arial -20 bold').grid(row=16, column=8, sticky=W)
        self.Q7 = Label (master, width=10, bg='lightblue')
        self.Q7.grid(row=16, column=9, sticky=E)


        self.parent=master
        self.combo()
        Button(master, text='QUIT', fg='red', font='arial -15 bold', command=master.destroy).grid(row=20, column=9)

        #Layout manager
        #MVC pattern
    def process_file(self, ev=None):
        filename=self.box.get()
        
        if self.browseActive == True:
            filename=self.browsedFile
            
        if self.ok:
            self.reader=Demonstrator(filename)
            self.notify()
    
    def open_file(self):
        self.browsedFile = askopenfilename(filetypes=[('','.csv')]) # I am HERE GEt the value into variable to work with the file
        self.browseActive= True
        
##    def filevalidation(self, filename):
        
        
    def combo(self):
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.parent, textvariable=self.box_value,
                                state='readonly')
        self.box['values'] = ('3124749a.csv', '3124749b.csv', '3124749c.csv')
        self.box.current(0)
        self.box.grid(column=2, row=3)
        
    
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
    top.geometry("1520x720")#"1920x1080")
    top.title("Raitis Kupce Assignment")
    top.grid()

    app = TaskGUI(top)

    top.mainloop()
