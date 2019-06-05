import tkinter as tk
win = tk.Tk()
win.title('test_toplevel')
win.geometry('500x300')


def show_login():
    sub_win = tk.Toplevel(win)
    sub_win.title('sub win')
    sub_win.geometry('300x200')


tk.Button(win, text='LOGIN', command=show_login).pack()

win.mainloop()
