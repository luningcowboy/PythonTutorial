import tkinter as tk
win = tk.Tk()
win.title('test text')
win.geometry('500x300')
e = tk.Entry(win, show=None)
e.pack()
def insert_point():
    var = e.get()
    t.insert('insert', var)
def insert_end():
    var = e.get()
    t.insert('end', var)

b1 = tk.Button(win, text='InsertPoint', width=10, height=2, command=insert_point)
b1.pack()
b2 = tk.Button(win, text='InsertEnd', width=10, height=2, command=insert_end)
b2.pack()

t = tk.Text(win, height=3)
t.pack()

win.mainloop()
