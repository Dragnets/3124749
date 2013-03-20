#GUIs.py
#GUIs
#19/03/2013
#Raitis Kupce

from tkinter import *
from demonstrator import *


class TaskGUI():
    def __init__(self,master):
        

        Label(master, font='mono -36 bold', 
              text="Raitis Kupce App").grid(row=1, column=3,columnspan=10, sticky=W)

        Label(master,text='File name: ', font='cornsilk ').grid(row=3, column=1, sticky=E)
        self.filename = Entry(master,width=15, bg="cornsilk")
        self.filename.grid(row=3, column=2, sticky=W)
        Label(master, text='Question 1', font='arial -20 bold').grid(row=4, column=2,)
        self.Q1 = Label(master, width=10, bg='lightblue')
        self.Q1.grid(row=5, column=2)
        Label(master, text='Question 2', font='arial -20 bold').grid(row=6, column=2)
        self.Q2 = Label(master, width=10, bg='lightblue')
        self.Q2.grid(row=7, column=2)
        Label(master, text='Question 3', font='arial -20 bold').grid(row=8, column=2)
        self.Q3 = Label(master, width=10, bg='lightblue')
        self.Q3.grid(row=9, column=2)
        Label(master, text='Question 4', font='arial -20 bold').grid(row=10, column=2)
        self.Q4 = Label(master, width=10, bg='lightblue')
        self.Q4.grid(row=11, column=2)
        Label(master, text='Question 5', font='arial -20 bold').grid(row=12, column=2)
        self.Q5 = Label(master, width=10, bg='lightblue')
        self.Q5.grid(row=13, column=2)
        Label(master, text='Question 6', font='arial -20 bold').grid(row=14, column=2)
        self.Q6 = Label(master, width=10, bg='lightblue')
        self.Q6.grid(row=15, column=2)
        Label(master, text='Question 7', font='arial -20 bold').grid(row=16, column=2)
        self.Q7 = Label (master, width=10, bg='lightblue')
        self.Q7.grid(row=17, column=2)
        

        Button(master, text="Process",width=10,font='mono -15 bold',bg='lightgreen',
               command=self.process_file).grid(row=19, column=6)

        



    def process_file(self, ev=None):
        filename = self.filename.get()

        if filename == '3124749a.csv':
            self.ok = True
            #self.process.reset()  # SORT IT [Line31] >>>>>>>>>>>>>>>>>>>>>>>>>>>
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
    top.geometry("900x600")
    top.title("Raitis Kupce Assignment")
    top.grid()

    app = TaskGUI(top)

    top.mainloop()
