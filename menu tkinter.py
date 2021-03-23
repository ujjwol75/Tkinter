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

# def hello():
#     print("HEllO WORLD")

# m = Menu(root)
# m.add_command(label="file", activeforeground='blue', command=hello)
# root.config(menu=m)

#===================================

def myfunc():
    print("hey")

mainmenu = Menu(root)
m1 = Menu(mainmenu)
m1.add_command(label="Print", command=myfunc())
m1.add_command(label="Edit", command=myfunc())
m1.add_separator()
m1.add_command(label="Save ", command=myfunc())
m1.add_command(label="Save As", command=myfunc())
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)



root.config(menu=mainmenu)
mainmenu.add


#===================================

root.mainloop()