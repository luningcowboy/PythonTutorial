import tkinter as tk
import tkinter.messagebox

win = tk.Tk()
win.title('test messagebox')
win.geometry('500x300')

def hit_me():
    tkinter.messagebox.showinfo(title='hi', message='你好, 信息对话框')
    tkinter.messagebox.showwarning(title='hi', message='你好, 有警告')
    tkinter.messagebox.showerror(title='hi', message='你好, 有错误')
    print(tkinter.messagebox.askquestion(title='hi', message='你好'))
    print(tkinter.messagebox.askyesno(title='hi', message='你好'))
    print(tkinter.messagebox.askokcancel(title='hi', message='你好'))

tk.Button(win, text='hit me', bg='green', font=('Arial', 14), command=hit_me).pack()
win.mainloop()
