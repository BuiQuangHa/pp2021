# module import

from tkinter import *
import tkinter.messagebox
import sqlite3

#FE UI class

class Books
    def _init_ (self,root):
       
       
        self.root = root
        self.root.title("FORREST BOOKSTORE MANAGEMENT SYSTEM")
        self.root.geometry("1325x690")
        self.root.config(bg="black")

        #declare
        
        BookID = StringVar()
        BookName = StringVar()
        Price = StringVar()
        Author = StringVar()
        Year = StringVar()
        Publisher = StringVar()
        Quantity = StringVar()

        #Frame
        
        MainFrame = Frame(self.root,bg="brown")
        MainFrame.grid()

        HeadFrame = Frame(MainFrame, bd=1, padx=40,pady=12,bg='white',relief=RIDGE)
        HeadFrame.pack(side=TOP)
        
        self.ITitle = Label(HeadFrame,font=('arial',54),text='Forrest bookstore',bg='green')
        self.ITitle.grid()

        OpeFrame = Frame (MainFrame,bd=2,width=1100,height=50, padx=40,pady=20,bg='white',relief=RIDGE)
        OpeFrame.pack(side=BOTTOM)

        Bodyframe = Frame (MainFrame,bd=2,width=1090,height=400, padx=30,pady=20,bg='white',relief=RIDGE)
        Bodyframe.pack(side=BOTTOM)

        LeftBodyFrame = LabelFrame(BodyFrame,bd=2,width=600,height=350, padx=20,pady=10,bg='green',relief=RIDGE, font=('arial',13),text='Details')
        LeftBodyFrame.pack(side=LEFT)

        RightBodyFrame = LabelFrame(BodyFrame,bd=2,width=300,height=350, padx=20,pady=10,bg='green ',relief=RIDGE, font=('arial',13),text='Books Information')
        RightBodyFrame.pack(side=RIGHT)    
        
        # Adding to left body farme
        #BookID
        self.labelBookID = Label(LeftBodyFrame, font=('arial',13), text ="ID", padx = 2, bg='white', fg= 'red')
        self.labelBookID.grid(row = 0 ,column = 0,sticky=W)

        self.txtBookID = Entry(LeftBodyFrame,font=('arial',18),textvariable=BookID, width=25)
        self.txtBookID.grid(row = 0,column = 1,sticky=W)
        
        #BookName
        
        self.labelBookName = Label(LeftBodyFrame, font=('arial',13), text ="Name/Title", padx = 2, bg='white', fg= 'red')
        self.labelBookName.grid(row = 1,column = 0,sticky=W)

        self.txtBookName = Entry(LeftBodyFrame,font=('arial',15),textvariable=BookName, width = 25)
        self.txtBookName.grid(row = 1,column = 1,sticky=W)
        
        #Price

        self.labelPrice = Label(LeftBodyFrame, font=('arial',13), text ="Price", padx = 2, bg='white', fg= 'red')
        self.labelPrice.grid(row = 2 ,column = 0,sticky=W)

        self.txtPrice = Entry(LeftBodyFrame,font=('arial',15),textvariable=Price, width=25)
        self.txtPrice.grid(row = 2,column = 1,sticky=W)

        #Author

        self.labelAuthor = Label(LeftBodyFrame, font=('arial',13), text ="Author", padx = 2, bg='white', fg= 'red')
        self.labelAuthor.grid(row = 3 ,column = 0,sticky=W)

        self.txtAuthor = Entry(LeftBodyFrame,font=('arial',15),textvariable=Author, width=25)
        self.txtAuthor.grid(row = 3,column = 1,sticky=W)
        
        #Year
        
        self.labelYear = Label(LeftBodyFrame, font=('arial',13), text ="Published year", padx = 2, bg='white', fg= 'red')
        self.labelYear.grid(row = 4 ,column = 0,sticky=W)

        self.txtYear = Entry(LeftBodyFrame,font=('arial',15),textvariable=Year, width=25)
        self.txtYear.grid(row = 4,column = 1,sticky=W)

        #Publisher

        self.labelPublisher = Label(LeftBodyFrame, font=('arial',13), text ="Publisher", padx = 2, bg='white', fg= 'red')
        self.labelPublisher.grid(row = 5 ,column = 0,sticky=W)

        self.txtPublisher = Entry(LeftBodyFrame,font=('arial',15),textvariable=Publisher, width=25)
        self.txtPublisher.grid(row = 5,column = 1,sticky=W)

        #Quantity

        self.labelQuantity = Label(LeftBodyFrame, font=('arial',13), text ="Quantity", padx = 2, bg='white', fg= 'red')
        self.labelQuantity.grid(row = 6 ,column = 0,sticky=W)

        self.txtQuantity = Entry(LeftBodyFrame,font=('arial',18),textvariable=Quantity, width=25)
        self.txtQuantity.grid(row = 6,column = 1,sticky=W)


if __name__=='__main__':
    root = Tk()
    application = Books(root)
    root.mainloop()


