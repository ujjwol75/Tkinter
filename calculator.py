from tkinter import *

root = Tk()
root.geometry('550x550')
root.maxsize(550, 520)
root.minsize(550, 520)
root.title("Calculator By Ujjwol")
 

# equal = StringVar()

screen_value = StringVar()
operator = ""

def click_numbers(num):
    global operator
    operator = operator + str(num)
    screen_value.set(operator)

def click():
    global operator
    x = str(eval(operator))
    screen_value.set(x)
    operator = ""

def clear():
    global operator
    screen_value.set("")
    operator = ""

def delete_one():
    global screen_value
    screen_value.set(screen_value.get()[0:-1])
    
    
    
    

#=================screen entry==========================
screen = Entry(root, bg='skyblue', bd=7,textvariable=screen_value, relief=GROOVE, font=("arial", 35, "bold"))
screen.pack()
bg_color = "#074463"
#=============key frame===============
key_frame = Frame(root, bd=5, bg="yellow")
key_frame.place(x=5, y=80, width=540, height=440)
#============buttons================
seven_button = Button(key_frame, text="7", bd=5,command=lambda:click_numbers(7), relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
seven_button.grid(row=0, column=0, padx=6,pady=5)
eight_button = Button(key_frame, text="8", bd=5,command=lambda:click_numbers(8), relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
eight_button.grid(row=0, column=1, padx=6,pady=5)
nine_button = Button(key_frame, text="9", bd=5,command=lambda:click_numbers(9), relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
nine_button.grid(row=0, column=2, padx=6,pady=5)
divide_button = Button(key_frame, text="/", bd=5,command=lambda:click_numbers("/"), relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
divide_button.grid(row=0, column=3, padx=6,pady=5)

four_button = Button(key_frame, text="4", bd=5,command=lambda:click_numbers(4), relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
four_button.grid(row=1, column=0, padx=6,pady=5)
five_button = Button(key_frame, text="5", bd=5,command=lambda:click_numbers(5), relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
five_button.grid(row=1, column=1, padx=6,pady=5)
six_button = Button(key_frame, text="6", bd=5,command=lambda:click_numbers(6), relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
six_button.grid(row=1, column=2, padx=6,pady=5)
multiply_button = Button(key_frame, text="x", bd=5,command=lambda:click_numbers("*"), relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
multiply_button.grid(row=1, column=3, padx=6,pady=5)

one_button = Button(key_frame, text="1", bd=5,command=lambda:click_numbers(1), relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
one_button.grid(row=2, column=0, padx=6,pady=5)
two_button = Button(key_frame, text="2", bd=5,command=lambda:click_numbers(2), relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
two_button.grid(row=2, column=1, padx=6,pady=5)
three_button = Button(key_frame, text="3", bd=5,command=lambda:click_numbers(3), relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
three_button.grid(row=2, column=2, padx=6,pady=5)
plus_button = Button(key_frame, text="+", bd=5,command=lambda:click_numbers("+"), relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
plus_button.grid(row=2, column=3, padx=6,pady=5)

zero_button = Button(key_frame, text="0", bd=5,command=lambda:click_numbers(0), relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
zero_button.grid(row=3, column=0, padx=6,pady=5)
dot_button = Button(key_frame, text=".", bd=5,command=lambda:click_numbers("."), relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
dot_button.grid(row=3, column=1, padx=6,pady=5)
delete_button = Button(key_frame, text="DEL", bd=5,command=delete_one, relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
delete_button.grid(row=3, column=2, padx=6,pady=5)
minus_button = Button(key_frame, text="-",command=lambda:click_numbers("-"), bd=5, relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
minus_button.grid(row=3, column=3, padx=6,pady=5)

equal_button = Button(key_frame, text="=", command=click, bd=5, relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
equal_button.grid(row=4, column=0, padx=6,pady=5)
percent_button = Button(key_frame, text="%", bd=5,command=lambda:click_numbers("%"), relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
percent_button.grid(row=4, column=1, padx=6,pady=5)
clear_button = Button(key_frame, text="CLR", bd=5,command=clear, relief=GROOVE, bg=bg_color, font=("arial", 25, "bold"), width=5, fg="red")
clear_button.grid(row=4, column=2, padx=6,pady=5)







root.mainloop()