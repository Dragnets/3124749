#GUIs.py
#GUIs
#19/03/2013
#Raitis Kupce
from tkinter import *
from process import *


class TaskGUI():
    def __init__(self,master):
          


        Label(master, font='mono -36 bold', 
              text="Raitis Kupce App").grid(row=1, column=3,columnspan=10, sticky=W)

        Label(master,text='File name: ', font='cornsilk ').grid(row=3, column=1, sticky=E)
        self.filename = Entry(master,width=15, bg="cornsilk")
        self.filename.grid(row=3, column=2, sticky=W)
        





    def runGUI(self, ev=None):
        filename = self.flname.get()

        if filename == '3124749a.csv':
            self.ok =True
            #self.process.reset()  # SORT IT [Line31] >>>>>>>>>>>>>>>>>>>>>>>>>>>
            



























if __name__ == "__main__":
    top =Tk()
    top.geometry("900x600")
    top.title("Raitis Kupce Assignment")
    top.grid()

    app = TaskGUI(top)

    top.mainloop()
