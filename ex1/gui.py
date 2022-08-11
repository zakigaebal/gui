from ast import main
from tkinter import *

root = Tk()
root.title("간단한 계산기")

entry = Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, padx=10,pady=10)

def btn_click(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(current)+str(number))
    return


button1 = Button(root, text="1", padx=30, pady=20, command=lambda: btn_click(1))
button2 = Button(root, text="2",padx=30,pady=20, command=lambda: btn_click(2))
button3 = Button(root, text="3",padx=30,pady=20, command=lambda: btn_click(3))
button4 = Button(root, text="4",padx=30,pady=20, command=lambda: btn_click(4))
button5 = Button(root, text="5",padx=30,pady=20, command=lambda: btn_click(5))
button6 = Button(root, text="6",padx=30,pady=20, command=lambda: btn_click(6))
button7 = Button(root, text="7",padx=30,pady=20, command=lambda: btn_click(7))
button8 = Button(root, text="8",padx=30,pady=20, command=lambda: btn_click(8))
button9 = Button(root, text="9",padx=30,pady=20, command=lambda: btn_click(9))
button0 = Button(root, text="0",padx=30,pady=20, command=lambda: btn_click(0))
buttonplus = Button(root, text="+",padx=30,pady=20, command=lambda: btn_click(0))



button1.grid(row=1, column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button0.grid(row=4,column=0)




mainloop()


