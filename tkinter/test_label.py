import tkinter as tk
win = tk.Tk()
win.title('test label')
win.geometry('500x300')
label = tk.Label(win, text='TestLabel',bg='green',font=('Arial', 12), width=30, height=2)
label.pack()
win.mainloop()
