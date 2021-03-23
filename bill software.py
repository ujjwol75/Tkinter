from tkinter import *
import math, random
from tkinter import messagebox

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("BILLING APP")
        bg_color = "#074463"
        #=================Billing software label=====================
        title = Label(self.root, text="Billing Software", font=("times new roman", 30, "bold"), bg=bg_color, fg="White",pady=2, bd=12, relief=GROOVE).pack(fill=X)
        
        #======================variables========================
        #===================cosmetics variables =========================
        self.bathsoap = IntVar()
        self.facecrm =IntVar()
        self.facewash = IntVar()
        self.harispray = IntVar()
        self.hairgel = IntVar()
        self.bodyloshan = IntVar()

        #====================grocery variables ================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.paddy = IntVar()
        self.cake = IntVar()

        #====================cold drinks =====================
        self.maza = IntVar()
        self.coke = IntVar()
        self.fanta = IntVar()
        self.sprite = IntVar()
        self.pepsi = IntVar()

        #=============total variables ================
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.colddrinks_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.colddrinks_tax = StringVar()
        #==============customers=======================
        self.customer_name = StringVar()
        self.customer_phone = StringVar()
        self.billno = StringVar()
        x = random.randint(1000, 9999)
        self.billno.set(x)
        self.search_bill = StringVar()

        
        self.ttl_items_price = (
                                    self.cosmetic_price.get() +
                                    self.grocery_price.get() +
                                    self.colddrinks_price.get() +
                                    self.cosmetic_tax.get() +
                                    self.grocery_tax.get() +
                                    self.colddrinks_tax.get()
                            )

        #=================Customer Details frame==========================
        frame1 =  LabelFrame(self.root, text="Customer details", fg="gold", font=("times new roman", 15, "bold"), bg=bg_color)
        frame1.place(x=0, y = 75, relwidth=1)

        cname_lbl = Label(frame1, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Customer Name").grid(row=0, column=1, padx=20, pady=4)
        cname_text = Entry(frame1, width=15,textvariable=self.customer_name, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=0, column=2, padx=5, pady=4)
        
        cphn_lbl = Label(frame1, font=("new times roman", 15, "bold"), bg=bg_color, fg="white", text="Phone No.").grid(row=0, column=3, padx=20, pady=4)
        cphn_text = Entry(frame1, width=15,textvariable=self.customer_phone, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=0, column=4, padx=20, pady=4)

        billnum_lbl = Label(frame1, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Bill No.").grid(row=0, column=5, padx=20, pady=4)
        billnum_text = Entry(frame1, width=15,textvariable=self.billno, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=0, column=6, padx=20, pady=4)
        
        search_button = Button(frame1, bg="white", font=("aries", 15), bd=7, relief=SUNKEN, text="Search").grid(row=0, column=7, padx=20, pady=4)
  

        #===========================Cosmetics Frame===========================
        frame2 = LabelFrame(self.root, text="Cosmetics", fg="gold", font=("times new roman", 15, "bold"), bg=bg_color)
        frame2.place(x=5, y=165, width=310, height=320)

        b_soap_lbl = Label(frame2, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Bath Soap").grid(row=0, column=0, sticky="w", padx=3, pady=4) 
        b_soap_text = Entry(frame2, width=12,textvariable=self.bathsoap, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=3, pady=4)
  
        f_cream_lbl = Label(frame2, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Face Cream").grid(row=1, column=0, sticky="w", padx=3, pady=4) 
        f_cream_text = Entry(frame2, width=12,textvariable=self.facecrm, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=3, pady=4)
  
        f_wash_lbl = Label(frame2, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Face Wash").grid(row=2, column=0, sticky="w", padx=3, pady=4) 
        f_wash_text = Entry(frame2, width=12,textvariable=self.facewash, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=3, pady=4)
  
        h_spray_lbl = Label(frame2, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Hair Spray").grid(row=3, column=0, sticky="w", padx=3, pady=4) 
        h_spray_text = Entry(frame2, width=12,textvariable=self.harispray, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=3, column=1, padx=3, pady=4)
  
        h_gel_lbl = Label(frame2, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Hair Gel").grid(row=4, column=0, sticky="w", padx=3, pady=4) 
        h_gel_text = Entry(frame2, width=12,textvariable=self.hairgel, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=4, column=1, padx=3, pady=4)
  
        b_loshan_lbl = Label(frame2, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Body Loshan").grid(row=5, column=0, sticky="w", padx=5, pady=4) 
        b_loshan_text = Entry(frame2, width=12,textvariable=self.bodyloshan, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=5, column=1, padx=3, pady=4)
  

        #===========================Grocery Frame===========================
        frame3 = LabelFrame(self.root, text="Grocery", fg="gold", font=("times new roman", 15, "bold"), bg=bg_color)
        frame3.place(x=320, y=165, width=310, height=320)

        food_Oil_lbl = Label(frame3, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Food Oil").grid(row=0, column=0, sticky="w", padx=6, pady=4) 
        food_oil_text = Entry(frame3, width=12,textvariable=self.food_oil, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=6, pady=4)
  
        wheat_lbl = Label(frame3, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Wheat").grid(row=1, column=0, sticky="w", padx=6, pady=4) 
        wheat_text = Entry(frame3, width=12,textvariable=self.wheat, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=6, pady=4)
        
        daal_lbl = Label(frame3, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Daal").grid(row=2, column=0, sticky="w", padx=6, pady=4) 
        daal_text = Entry(frame3, width=12,textvariable=self.daal, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=6, pady=4)

        paddy_lbl = Label(frame3, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Paddy").grid(row=3, column=0, sticky="w", padx=6, pady=4) 
        paddy_text = Entry(frame3, width=12,textvariable=self.paddy, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=3, column=1, padx=6, pady=4)

        cake_lbl = Label(frame3, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Cake").grid(row=4, column=0, sticky="w", padx=6, pady=4) 
        cake_text = Entry(frame3, width=12,textvariable=self.cake, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=4, column=1, padx=6, pady=4)



        #===========================Cosmetics Frame===========================
        frame4 = LabelFrame(self.root, text="Cosmetics", fg="gold", font=("times new roman", 15, "bold"), bg=bg_color)
        frame4.place(x=635, y=165, width=310, height=320)

        maza_lbl = Label(frame4, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Maza").grid(row=0, column=0, sticky="w", padx=3, pady=4) 
        maza_text = Entry(frame4, width=12,textvariable=self.maza, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=3, pady=4)
  
        coke_lbl = Label(frame4, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Coke").grid(row=1, column=0, sticky="w", padx=3, pady=4) 
        coke_text = Entry(frame4, width=12,textvariable=self.coke, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=3, pady=4)
  
        fanta_lbl = Label(frame4, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Fanta").grid(row=2, column=0, sticky="w", padx=3, pady=4) 
        fanta_text = Entry(frame4, width=12,textvariable=self.fanta, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=3, pady=4)
  
        sprite_lbl = Label(frame4, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Sprite").grid(row=3, column=0, sticky="w", padx=3, pady=4) 
        sprite_text = Entry(frame4, width=12,textvariable=self.sprite, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=3, column=1, padx=3, pady=4)
  
        pepsi_lbl = Label(frame4, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Pepsi").grid(row=4, column=0, sticky="w", padx=3, pady=4) 
        pepsi_text = Entry(frame4, width=12,textvariable=self.pepsi, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=4, column=1, padx=3, pady=4)
  

        #===============================Bill Area======================
        frame5 = Frame(self.root, bg="white")
        frame5.place(width=399, height=320, x=950, y=165)

        bill_area_lbl = Label(frame5, font=("arial", 20, "bold"), text="Bill Area", fg="black", bg="white", bd=5, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(frame5, orient=VERTICAL, bg="white")
        self.txtarea = Text(frame5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)


        #======================Button menu(billing menu)====================
        frame6 = LabelFrame(self.root, text="Bill Menu", fg="gold", font=("times new roman", 15, "bold"), bg=bg_color)
        frame6.place(x=5, y=490, width=1345, height=210)

        ttl_cosmetic_lbl = Label(frame6, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Total Cosmetics Price").grid(row=0, column=0, sticky="w", padx=5, pady=5) 
        ttl_cosmetic_text = Entry(frame6, width=12,textvariable=self.cosmetic_price, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=5, pady=5)

        ttl_grocery_lbl = Label(frame6, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Total Grocery Price").grid(row=1, column=0, sticky="w", padx=5, pady=5) 
        ttl_grocery_text = Entry(frame6, width=12,textvariable=self.grocery_price, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=5, pady=5)

        ttl_colddrinks_lbl = Label(frame6, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Total Cold Drinks Price").grid(row=2, column=0, sticky="w", padx=5, pady=5) 
        ttl_colddrinks_text = Entry(frame6, width=12,textvariable=self.colddrinks_price, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=5, pady=5)

        tax_cosmetic_lbl = Label(frame6, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Cosmetics Tax").grid(row=0, column=2, sticky="w", padx=3, pady=5) 
        tax_cosmetic_text = Entry(frame6, width=12,textvariable=self.cosmetic_tax, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=5, pady=5)

        tax_grocery_lbl = Label(frame6, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Grocery Tax").grid(row=1, column=2, sticky="w", padx=3, pady=5) 
        tax_grocery_text = Entry(frame6, width=12,textvariable=self.grocery_tax, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=5, pady=5)

        tax_colddrinks_lbl = Label(frame6, font=("times new roman", 15, "bold"), fg="white", bg=bg_color, text="Cold Drinks Tax").grid(row=2, column=2, sticky="w", padx=5, pady=5) 
        tax_colddrinks_text = Entry(frame6, width=12,textvariable=self.colddrinks_tax, font=("new times roman", 15, "bold"), bg="white", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=5, pady=5)

         #===============frame7 (Last Buttons)==================== 
        frame7 = Frame(frame6, relief=GROOVE, bd=5)
        frame7.place(x=720, width=600, height=150)

        Total_btn = Button(frame7, text="Total", font=("arial", 18, "bold"),command=self.total_price, bg=bg_color, fg="white", bd=6, relief=GROOVE).grid(row=0, column=0, padx=15, pady=35)
        generatebill_btn = Button(frame7, text="Generate Bill",command=self.bill, font=("arial", 18, "bold"), bg=bg_color, fg="white", bd=6, relief=GROOVE).grid(row=0, column=1, padx=15, pady=35)
        clear_btn = Button(frame7, text="Clear", font=("arial", 18, "bold"),command=self.clear, bg=bg_color, fg="white", bd=6, relief=GROOVE).grid(row=0, column=2, padx=15, pady=35)
        exit_btn = Button(frame7, text="Exit", font=("arial", 18, "bold"), bg=bg_color, fg="white", bd=6, relief=GROOVE).grid(row=0, column=3, padx=15, pady=35)
        self.welcome_bill()
    

    def total_price(self):
        self.total_cosmetic_price =(
                                (self.bathsoap.get() * 40) +
                                (self.facecrm.get() * 100) +
                                (self.facewash.get() * 150) +
                                (self.harispray.get() * 120) +
                                (self.hairgel.get() * 135) +
                                (self.bodyloshan.get() * 200)
                                )

        self.cosmetic_price.set(str(self.total_cosmetic_price))
        self.cosmetic_tax.set(str(round((self.total_cosmetic_price * 0.05),2)))

        self.total_grocery_price =(
                                (self.rice.get() * 60) +
                                (self.paddy.get() * 140) +
                                (self.food_oil.get() * 120) +
                                (self.cake.get() * 500) +
                                (self.wheat.get() * 200) +
                                (self.daal.get() * 100)
                                )

        self.grocery_price.set(str(self.total_grocery_price))
        self.grocery_tax.set(str(round((self.total_grocery_price * 0.1),2)))
        self.total_colddrinks_price =(
                                (self.maza.get() * 40) +
                                (self.sprite.get() * 45) +
                                (self.coke.get() * 190) +
                                (self.fanta.get() * 55) +
                                (self.pepsi.get() * 50) 
                                )
        
        self.colddrinks_price.set(str(self.total_colddrinks_price))
        self.colddrinks_tax.set(str(round((self.total_colddrinks_price * 0.05),2)))
        self.welcome_bill()
    
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END,"\t Welcome to Ujjwol Retail")
        self.txtarea.insert(END, f"\n Bill NO. : {self.billno.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.customer_name.get()}")
        self.txtarea.insert(END, f"\n Customer Phone No. : {self.customer_phone.get()}")
        self.txtarea.insert(END, f"\n ==============================================")
        self.txtarea.insert(END, f"\n Products \t\t Qty \t\t Price")
        self.txtarea.insert(END, f"\n ==============================================")


    
    

    def bill(self):
        
        self.welcome_bill()
        #==========check to see if costumer name and phone is written===============
        if (self.customer_name.get() == "") or (self.customer_phone == ""):
            messagebox.showerror("Error", "Customer details must")

        
        #========================cosmetics================================
        if self.bathsoap.get() != 0:
           self.txtarea.insert(END, f"\n Bath Soap \t\t {self.bathsoap.get()} \t\t {self.bathsoap.get()*40}")
        if self.bodyloshan.get() != 0:
            self.txtarea.insert(END, f"\n Body Loshan \t\t {self.bodyloshan.get()} \t\t {self.bodyloshan.get()*200}")
        if self.hairgel.get() != 0:
            self.txtarea.insert(END, f"\n Hair Gel \t\t {self.hairgel.get()} \t\t {self.hairgel.get()*135}")
        if self.harispray.get() != 0:
            self.txtarea.insert(END, f"\n Hair Spray \t\t {self.harispray.get()} \t\t {self.harispray.get()*120}")
        if self.facecrm.get() != 0:
            self.txtarea.insert(END, f"\n Face Cream \t\t {self.facecrm.get()} \t\t {self.facecrm.get()*100}")
        if self.facewash.get() != 0:
            self.txtarea.insert(END, f"\n Face Wash \t\t {self.facewash.get()} \t\t {self.facewash.get()*150}")

        #============================grocery=====================================
        if self.food_oil.get() != 0:
            self.txtarea.insert(END, f"\n Food Oil \t\t {self.food_oil.get()} \t\t {self.food_oil.get()*120}")
        if self.wheat.get() != 0:
            self.txtarea.insert(END, f"\n Wheat \t\t {self.wheat.get()} \t\t {self.wheat.get()*200}")
        if self.paddy.get() != 0:
            self.txtarea.insert(END, f"\n Paddy \t\t {self.paddy.get()} \t\t {self.paddy.get()*150}")
        if self.daal.get() != 0:
            self.txtarea.insert(END, f"\n Daal \t\t {self.daal.get()} \t\t {self.daal.get()*100}")
        if self.cake.get() != 0:
            self.txtarea.insert(END, f"\n Cake \t\t {self.cake.get()} \t\t {self.cake.get()*500}")

        #========================cold drinks =====================================
        if self.maza.get() != 0:
            self.txtarea.insert(END, f"\n Maza \t\t {self.maza.get()} \t\t {self.maza.get()*40}")
        if self.pepsi.get() != 0:
            self.txtarea.insert(END, f"\n Pepsi \t\t {self.pepsi.get()} \t\t {self.pepsi.get()*50}")
        if self.sprite.get() != 0:
            self.txtarea.insert(END, f"\n Sprite \t\t {self.sprite.get()} \t\t {self.sprite.get()*45}")
        if self.coke.get() != 0:
            self.txtarea.insert(END, f"\n Coke \t\t {self.coke.get()} \t\t {self.coke.get()*190}")
        if self.fanta.get() != 0:
            self.txtarea.insert(END, f"\n Fanta \t\t {self.fanta.get()} \t\t {self.fanta.get()*55}")
        
        self.txtarea.insert(END, f"\n ==============================================")
        #====================TOTAL PRICE ==========================================
        self.txtarea.insert(END, f"\n TOTAL PRICE : \t\t\t\t {self.ttl_items_price}")
        self.txtarea.insert(END, f"\n ==============================================")


    def clear(self):
        self.txtarea.delete('1.0', END)
    

        

        
                                                
root = Tk()
obj = Bill_App(root)
root.mainloop()
