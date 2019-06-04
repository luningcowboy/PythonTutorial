import tkinter as tk
win = tk.Tk()
win.title('test button')
win.geometry('500x300')
var = tk.StringVar()
label = tk.Label(win, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
label.pack()
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')
button = tk.Button(win, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
button.pack()
win.mainloop()

