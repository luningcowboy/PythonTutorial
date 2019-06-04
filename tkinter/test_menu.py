import tkinter as tk
win = tk.Tk()
win.title('test menu')
win.geometry('500x300')
l = tk.Label(win, text='     ', bg='green')
l.pack()

counter = 0
def to_job():
    global counter
    l.config(text='do '+ str(counter))
    counter += 1

menubar = tk.Menu(win)

filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=to_job)
filemenu.add_command(label='Open', command=to_job)
filemenu.add_command(label='Save', command=to_job)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=win.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=to_job)
editmenu.add_command(label='Copy', command=to_job)
editmenu.add_command(label='Past', command=to_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label='Submenu_1', command=to_job)

win.config(menu=menubar)

win.mainloop()
