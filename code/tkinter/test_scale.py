import tkinter as tk
win = tk.Tk()
win.title('test scale')
win.geometry('500x300')
l = tk.Label(win, bg='green', fg='white', width=20, text='empty')
l.pack()

def print_selection(v):
    l.config(text='you have selected ' + v)
s = tk.Scale(win, label='try me', from_=0, to=10, \
        orient=tk.HORIZONTAL, length=200, \
        showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

win.mainloop()
