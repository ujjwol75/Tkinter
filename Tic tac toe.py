from tkinter import *

root = Tk()

# root.geometry('300x300')
# root.maxsize(400,400)
# root.minsize(400,400)

def b_click():
    pass


#=======our buttons to click=========================
b1 = Button(root, text=" ", font=("Helvetica", 20), fg="black", bg="grey",width=5, height=2, command=lambda:b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), fg="black", bg="grey",width=5, height=2, command=lambda:b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), fg="black", bg="grey",width=5, height=2, command=lambda:b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica", 20), fg="black", bg="grey",width=5, height=2, command=lambda:b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), fg="black", bg="grey",width=5, height=2, command=lambda:b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), fg="black", bg="grey",width=5, height=2, command=lambda:b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica", 20), fg="black", bg="grey",width=5, height=2, command=lambda:b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), fg="black", bg="grey",width=5, height=2, command=lambda:b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), fg="black", bg="grey",width=5, height=2, command=lambda:b_click(b9))



#===========grid above buttons======================
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)



root.mainloop()