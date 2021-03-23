from tkinter import *
root = Tk()
root.geometry('400x500')

#===============================

# m = Menu(root)
# menubar = Menu(root)
# m.add_command(label="file")
# menubar.add_cascade(label="random", menu=m, activeforeground="red")
# root.config(menu=menubar)

#=================================

def hello():
    print("HEllO WORLD")

m = Menu(root)
m.add_command(label="file", activeforeground='blue', command=hello)
root.config(menu=m)

#===================================

root.mainloop()