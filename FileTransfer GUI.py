
import tkinter
from tkinter import *
import os
import shutil




class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=True)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('File Transfer!')
        self.master.config(bg='lightgray')

        self.varFName =  StringVar()
        self.varLName =  StringVar()
        
        self.btnFName = Button(self.master,text='Source Folder: ', font =("Helvetica",16), fg='black', bg='lightgray' )
        self.btnFName.grid(row=0, column=0,padx=(30,0),pady=(30,0))
        
        self.btnLName = Button(self.master,text='Destination Folder: ', font =("Helvetica",16), fg='black', bg='lightgray' )
        self.btnLName.grid(row=1, column=0,padx=(30,0),pady=(30,0))

        self.lblDisplay = Label(self.master,text='', font =("Helvetica",16), fg='black', bg='lightgray' )
        self.lblDisplay.grid(row=3,column=1,padx=(30,0),pady=(30,0))

        self.txtFName = Entry(self.master,text=self.varFName, font=('Helvitica',16),fg='black', bg='lightblue')
        self.txtFName.grid(row=0,column=1,padx=(30,0),pady=(30,0))
        
        self.txtLName = Entry(self.master,text=self.varLName, font=('Helvitica',16),fg='black', bg='lightblue')
        self.txtLName.grid(row=1,column=1,padx=(30,0),pady=(30,0))

        self.btnSubmit = Button(self.master, text='Submit', width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2,column=1,padx=(0,0),pady=(30,0),sticky=NE)

        self.btnCancel = Button(self.master, text='Cancel', width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2,column=1,padx=(0,90),pady=(30,0),sticky=NE)

    def submit(self):
        fn = self.varFName.openaskdirectory()
        ln = self.varLName.openaskdirectory()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))

    def cancel(self):
        self.master.destroy()
        
        










if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
