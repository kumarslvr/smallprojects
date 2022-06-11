from tkinter import *
import random
root= Tk()

frame2= Frame(root)
frame2.pack(side=BOTTOM)
frame1= Frame(root)
frame1.pack(side=BOTTOM)

frame3= Frame(root)
flag="show"      #flag to display frame in which listbox is packed 
flag2="enter"    #flag to update entery box with item selected from listbox
oldselect=[]
class Custom_button:

    def __init__(self, name, row_number, column_number, frame, width, height):
        self.name=name
        self.row_number=row_number
        self.column_number=column_number
        self.frame=frame
        self.width=width
        self.height=height

    def draw_button(self):
        self.buttons = Button(self.frame, text=self.name, command=self.button_clicked, width=self.width, height=self.height)
        self.buttons.grid(row=self.row_number, column=self.column_number,padx=1,pady=1 )

    def button_clicked(self):
        global flag
        sym = self.buttons['text']

        try:
            if sym=="=" :
                e=entry.get()
                listbox_1.insert(END,e)
                entry.delete(0,END)
                entry.insert(END,eval(e))
            elif sym=="C":
                entry.delete(0,END)
            elif sym=="⌫":
                eg=entry.get()
                entry.delete(0,END)
                eg=eg[:-1]
                entry.insert(0,eg)
            elif sym=="History":
                if flag=="show":
                    frame3.pack(side=TOP)
                    flag="hide"
                else:
                    frame3.forget()
                    flag="show"
                    

            else:
                entry.insert(END,self.buttons['text'])
        except:
            entry.delete(0,END)
            entry.insert(END,"Error")


 
symbol=['1','2','3','+','4','5','6',"-",'7','8','9',"*",".", "0", "=", "/"]

c=0
for n in range(4):
        for i in range(4):
            co=Custom_button(symbol[c],n,i, frame2,5,2)
            c=c+1
            co.draw_button()

entry = Entry(frame1, width=30)
entry.grid(row=0, column=0, columnspan=3,sticky=W, ipady=7)

co=Custom_button("History",1,0, frame1,10,2)
co.draw_button()
co=Custom_button("⌫",1,1, frame1,5,2)
co.draw_button()
co=Custom_button("C",1,2, frame1,5,2)
co.draw_button()

scrollbar_1= Scrollbar(frame3,orient=VERTICAL)
listbox_1=Listbox(frame3, width=30, height=5 ,yscrollcommand=scrollbar_1.set)

scrollbar_1.config(command=listbox_1.yview)
scrollbar_1.pack(side=RIGHT, fill=Y)

listbox_1.pack(side=LEFT)

while True:
    selection=listbox_1.curselection()  #selection is a tuple which only has one item at a time which is the index of the item selected on the listbox
   
    if flag2=="enter":
        if len(selection)>0:
            oldselect=selection
            index=selection[0]
            entry.delete(0,END)
            actual_value=listbox_1.get(index)
            entry.insert(END,actual_value)
            flag2="exit"
            
    if selection!=oldselect:
        flag2="enter"
        
    root.update()
        
