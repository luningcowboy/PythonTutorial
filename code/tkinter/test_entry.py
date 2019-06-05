import tkinter as tk
win = tk.Tk()
win.title('test entry')
win.geometry('500x300')
e1 = tk.Entry(win, show='*', font=('Arial', 14))
e2 = tk.Entry(win, show=None, font=('Arial', 14))
e1.pack()
e2.pack()
win.mainloop()
