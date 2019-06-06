import tkinter as tk
win = tk.Tk()
win.title('计算器')
win.geometry('300x500')

def tap_AC():
    print('tap_AC')
def tap_Change():
    print('tap_Change')
def tap_Remainder():
    print('tap_Remainder')
def tap_Division():
    print('tap_Division')
def tap_0():
    print('tap_0')

text = tk.Text(win, height=7, bg='green')
text.pack()

f0 = tk.Frame(win)
f0.pack()

btn_AC = tk.Button(f0, text='AC',width=4, command=tap_AC)
btn_Change = tk.Button(f0, text='+/-',width=4, command=tap_Change)
btn_Remainder = tk.Button(f0, text='%',width=4, command=tap_Remainder)
btn_Division = tk.Button(f0, text='/',width=4, command=tap_Division)

btn_AC.grid(row=0,column=0 ,padx=5, pady=10,ipadx=10,ipady=10)
btn_Change.grid(row=0,column=1,padx=5, pady=10,ipadx=10,ipady=10)
btn_Remainder.grid(row=0,column=2,padx=5, pady=10,ipadx=10,ipady=10)
btn_Division.grid(row=0,column=3,padx=5, pady=10,ipadx=10,ipady=10)
# 7,8,9,x
f1 = tk.Frame(win)
f1.pack()

btn_7 = tk.Button(f1, text='7',width=4, command=tap_AC)
btn_8 = tk.Button(f1, text='8',width=4, command=tap_Change)
btn_9 = tk.Button(f1, text='9',width=4, command=tap_Remainder)
btn_x = tk.Button(f1, text='X',width=4, command=tap_Division)

btn_7.grid(row=0,column=0 ,padx=5, pady=10,ipadx=10,ipady=10)
btn_8.grid(row=0,column=1,padx=5, pady=10,ipadx=10,ipady=10)
btn_9.grid(row=0,column=2,padx=5, pady=10,ipadx=10,ipady=10)
btn_x.grid(row=0,column=3,padx=5, pady=10,ipadx=10,ipady=10)
# 4,5,6,-
f2 = tk.Frame(win)
f2.pack()

btn_4 = tk.Button(f2, text='4',width=4, command=tap_AC)
btn_5 = tk.Button(f2, text='5',width=4, command=tap_Change)
btn_6 = tk.Button(f2, text='6',width=4, command=tap_Remainder)
btn_Sub = tk.Button(f2, text='-',width=4, command=tap_Division)

btn_4.grid(row=0,column=0 ,padx=5, pady=10,ipadx=10,ipady=10)
btn_5.grid(row=0,column=1,padx=5, pady=10,ipadx=10,ipady=10)
btn_6.grid(row=0,column=2,padx=5, pady=10,ipadx=10,ipady=10)
btn_Sub.grid(row=0,column=3,padx=5, pady=10,ipadx=10,ipady=10)
# 1,2,3,+
f3 = tk.Frame(win)
f3.pack()

btn_1 = tk.Button(f3, text='1',width=4, command=tap_AC)
btn_2 = tk.Button(f3, text='2',width=4, command=tap_Change)
btn_3 = tk.Button(f3, text='3',width=4, command=tap_Remainder)
btn_Add= tk.Button(f3, text='+',width=4, command=tap_Division)

btn_1.grid(row=0,column=0 ,padx=5, pady=10,ipadx=10,ipady=10)
btn_2.grid(row=0,column=1,padx=5, pady=10,ipadx=10,ipady=10)
btn_3.grid(row=0,column=2,padx=5, pady=10,ipadx=10,ipady=10)
btn_Add.grid(row=0,column=3,padx=5, pady=10,ipadx=10,ipady=10)

# 0,.,= 
f4 = tk.Frame(win)
f4.pack()

btn_0 = tk.Button(f4, text='0',width=8, command=tap_AC)
btn_Point = tk.Button(f4, text='.',width=4, command=tap_Change)
btn_Equ = tk.Button(f4, text='=',width=4, command=tap_Remainder)

btn_0.grid(row=0,column=0 ,padx=5, pady=10,ipadx=10,ipady=10)
btn_Point.grid(row=0,column=1,padx=5, pady=10,ipadx=10,ipady=10)
btn_Equ.grid(row=0,column=2,padx=5, pady=10,ipadx=10,ipady=10)

win.mainloop()
