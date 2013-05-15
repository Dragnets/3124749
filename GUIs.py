#GUIs.py
#GUIs
#19/03/2013
#Raitis Kupce

from demonstrator import *
from tkinter.filedialog import *
from tkinter import Tk, StringVar, ttk
import os


class TaskGUI():
    def __init__(self,master):
        '''Displays all the answers in GUIs'''

        self.browseActive= False    # Indicate that btn browse have not been used.
        
        # FRAMES Below >>>
        header  = Frame(master)
        header.grid(row=2,column=2, sticky=W)
        title   = Frame(master)
        title.grid(row=1, column=2)
        body    = Frame(master,)
        body.grid(row=3,column=2, sticky=W)
        # END of Frame >>>
        
        Label(header,height=5).grid(row=2, column=1) # GAP FOR TITLE
        Label(title, font='mono -36 bold', text="Raitis Kupce App").grid(row=1, column=3)
        Label(header,text='File name: ', font='cornsilk -20 bold').grid(row=3, column=1, sticky=E)
        Label(header,width=2).grid(row=3, column=3) #SPACE
        Button(header, text='Browse',width=10,font='mono -15 bold', bg='lightblue',
               command=self.open_file).grid(row=3, column=4,)
        Label(header,width=5,).grid(row=3, column=5) # SPACE
        Button(header, text="Process",width=20,font='mono -15 bold',bg='lightgreen',
               command=self.process_file).grid(row=3, column=6,)
        Label(header,height=2,).grid(row=4,) #GAP for Question
        Label(body,width=4).grid(column=1)   #Questions Indented

        #QUESTIONS BELOW >>>
        Label(body,text='Assignment Question',font='arial -20 bold').grid(row=1,column=2)
        Label(body,text='Answers', font='arial -20 bold').grid(row=1,column=3,sticky=E)
        Label(body, text='Q1 Find the sum of the values in the field [length] more than or equal to (6.346).',
              font='arial -20 bold').grid(row=2, column=2, sticky=W)
        self.Q1 = Label(body, width=10, bg='lightblue')
        self.Q1.grid(row=2, column=3,sticky=E)
        Label(body, text='Q2 What percentage of the numbers in [mark] lie between (52) and (123) inclusive.',
              font='arial -20 bold').grid(row=3, column=2)
        self.Q2 = Label(body, width=10, bg='lightblue')
        self.Q2.grid(row=3, column=3,sticky=E)
        Label(body, text="Q3 (sell's) are what percentage of the field [action].",
              font='arial -20 bold').grid(row=4, column=2, sticky=W)
        self.Q3 = Label(body, width=10, bg='lightblue')
        self.Q3.grid(row=4, column=3, sticky=E)
        Label(body, text='Q4 Find the average of the values in the field [count].',
              font='arial -20 bold').grid(row=5, column=2, sticky=W)
        self.Q4 = Label(body, width=10, bg='lightblue')
        self.Q4.grid(row=5, column=3, stick=E)
        Label(body, text="Q5 How many values in the 'code' field do not match the format [X9]9XX9#9?",
              font='arial -20 bold').grid(row=6, column=2, sticky=W)
        self.Q5 = Label(body, width=10, bg='lightblue')
        self.Q5.grid(row=6, column=3, sticky=E)
        Label(body, text='Q6 What percentage of strings have the value (Ebony) in the field [tree]?',
              font='arial -20 bold').grid(row=7, column=2, sticky=W) 
        self.Q6 = Label(body, width=10, bg='lightblue')
        self.Q6.grid(row=7, column=3, sticky=E)
        Label(body, text='Q7 Count the lines where length is more than 2.223 *or* count is less than 742.',
              font='arial -20 bold').grid(row=8, column=2, sticky=W)
        self.Q7 = Label (body, width=10, bg='lightblue')
        self.Q7.grid(row=8, column=3, sticky=E)
        # END OF Questions >>>

        self.combo(header)  #Combo box
        Button(body, text='QUIT', fg='red', font='arial -18 bold',
               command=self.quitMessage).grid(row=9, column=3,)

    def process_file(self, ev=None):
        '''Open the choosen file by calling Demonstrator Class'''
        
        filename=self.box.get() # gets value from self.box
        if self.browseActive == True:
            if self.check_combo(self.browsedFile) == True: # Add only to combo box
                self.fileUsed.append(self.browsedFile)     # if not already Used
            self.browseActive= False                # Resets browse button status
            filename=self.browsedFile

        self.reader=Demonstrator(filename)
        self.notify()    # call method to display question results

    def open_file(self):
        '''Ability to browse the file in your computer'''
        
        self.browsedFile = os.path.basename(askopenfilename(filetypes=[('','.csv')]))
        self.box.set(self.browsedFile) 
        self.browseActive= True # To mark that this function has been used.

    def check_combo(self,filename):
        '''Check If file alreadi is in combo box'''

        for file in self.fileUsed:
            if file == filename:
                return False
        return True  
        
    def combo(self,frame):
        '''Creates a Combo box and gives 3 default files'''
        
        self.box_value = StringVar()
        self.box = ttk.Combobox(frame, textvariable=self.box_value,
                                state='readonly') # Creates a combo box
        self.fileUsed=['3124749a.csv', '3124749b.csv', '3124749c.csv'] # Default combo list
        self.box['values'] = (self.fileUsed) 
        self.box.current(0) # Current value
        self.box.grid(row=3, column=2)
    
    def notify(self):
        ''' Get the value from each question to display them on screen '''
        
        self.Q1['text'] = str(self.reader.displayQ1())  # Use Demonstrator's method 
        self.Q2['text'] = str(self.reader.displayQ2())  # to get the value.
        self.Q3['text'] = str(self.reader.displayQ3())
        self.Q4['text'] = str(self.reader.displayQ4())
        self.Q5['text'] = str(self.reader.displayQ5())
        self.Q6['text'] = str(self.reader.displayQ6())
        self.Q7['text'] = str(self.reader.displayQ7())

    def quitMessage(self,):
        message = messagebox.askyesno(title="Quit", message="Are you sure want to exit?",icon= "warning")    
        if message:
            top.destroy() # On Yes exits application.


if __name__ == "__main__":
    top =Tk()
    top.geometry("920x550") # size of application
    top.title("Raitis Kupce Assignment")
    top.grid()
    
    app = TaskGUI(top)

    top.mainloop()
