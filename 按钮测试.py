import tkinter
import tkinter.messagebox

t = tkinter.Tk()
t.title("按下按钮")
t.geometry("500x300")

window1 = tkinter.Label(text="按下这按钮！").pack()

def reportdataAA():
    tkinter.messagebox.showinfo(title="哈哈",message="这是测试")
window = tkinter.Button(t,command=reportdataAA,text="按下我吧")

window.pack()

t.mainloop()
