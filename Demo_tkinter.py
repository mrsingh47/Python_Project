import tkinter
import tkinter.messagebox as msg
MyObj = tkinter.Tk()
MyObj.geometry("400x400")
def Hello():
    msg.showinfo("Clicked")
b1=tkinter.Button(MyObj,text="Click here")
b2=tkinter.Button(MyObj,text="Output is here!!...",command=Hello)
b1.pack()
b2.pack()
MyObj.mainloop()