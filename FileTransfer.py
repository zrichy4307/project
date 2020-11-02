import tkinter
from tkinter import *
from tkinter import filedialog
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

        self.sourcePath =  StringVar()
        self.destPath =  StringVar()
        
        self.btnsourcePath = Button(self.master,text='Source Folder: ', font =("Helvetica",16), fg='black', bg='lightgray' )
        self.btnsourcePath.grid(row=0, column=0,padx=(30,0),pady=(30,0))
        
        self.btndestPath = Button(self.master,text='Destination Folder: ', font =("Helvetica",16), fg='black', bg='lightgray' )
        self.btndestPath.grid(row=1, column=0,padx=(30,0),pady=(30,0))

        self.txtSource = Entry(self.master,text=self.sourcePath, font=("Helvetica",16), fg='black', bg='lightgray' )
        self.txtSource.grid(row=0, column=1,padx=(30,0),pady=(30,0))

        self.txtDestination = Entry(self.master,text=self.sourcePath, font=("Helvetica",16), fg='black', bg='lightgray' )
        self.txtDestination.grid(row=1, column=1,padx=(30,0),pady=(30,0))

        self.lblDisplay = Label(self.master,text='', font =("Helvetica",16), fg='black', bg='lightgray' )
        self.lblDisplay.grid(row=3,column=1,padx=(30,0),pady=(30,0))

        self.txtsourcePath = Entry(self.master,text=self.sourcePath, font=('Helvitica',16),fg='black', bg='lightblue')
        self.txtsourcePath.grid(row=0,column=1,padx=(30,0),pady=(30,0))
        
        self.txtdestPath = Entry(self.master,text=self.destPath, font=('Helvitica',16),fg='black', bg='lightblue')
        self.txtdestPath.grid(row=1,column=1,padx=(30,0),pady=(30,0))

        self.btnSource = Button(self.master, text='Source Folder: ', font=('Helvitica',16),fg='black', bg='lightblue', command=self.getSource)
        self.btnSource.grid(row=0,column=0,padx=(30,0),pady=(30,0))

        self.btnDestination = Button(self.master, text='Destination Folder: ', font=('Helvitica',16),fg='black', bg='lightblue', command=self.getDestination)
        self.btnDestination.grid(row=1,column=0,padx=(30,0),pady=(30,0))

        self.btnTransfer = Button(self.master, text='Transfer', width=10, height=2, command=self.transfer)
        self.btnTransfer.grid(row=3,column=2,padx=(0,90),pady=(30,0),sticky=NE)


    def transfer(self):
        self.master.destroy()

    def getSource(self):
        srcPath = filedialog.askdirectory()
        self.txtSource.delete(0,END)
        self.txtSource.insert(0, srcPath)

    def getDestination(self):
        dstPath = filedialog.askdirectory()
        self.txtdestPath.delete(0,END)
        self.txtdestPath.insert(0, dstPath)

    def transfer(self):
        srcPath = self.txtSource.get()
        destPath = self.txtdestPath.get()
        fileList = os.listdir(srcPath)

        for file in fileList:
            abspath = os.path.join(srcPath, file)
            shutil.move(abspath, destPath)
        
        










if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
