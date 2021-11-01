from tkinter import *
import sqlite3
from tkinter import messagebox
import datetime
import os
import random
date = datetime.datetime.now().date()

conn = sqlite3.connect("./store-db/store.db")
c = conn.cursor()

product_list=[]
product_quantity=[]
product_price=[]
product_id = []
class Datebase:
    def __init__(self , master , *args , **kwargs):

        self.master = master

        self.left = Frame(master , width='1000',height='1200',bg='white')
        self.left.pack(side=LEFT)

        self.right = Frame(master , width='700',height='1200')
        self.right.pack(side=RIGHT)

        self.header = Label(self.left,text="shop", font="arial 30 bold", fg="black" , bg="white")
        self.header.place(x=20,y=20)

        self.date_l = Label(self.right , text="today date : " + str(date),fg="black" ,font="arial 15 ")
        self.date_l.place(x=0,y=20)
        

        #---table 

        self.product_tb = Label(self.right, text="Product " ,fg="black" ,font="arial 15 ")
        self.product_tb.place(x=0,y=180)

        self.quantity_tb = Label(self.right, text="Quantity " ,fg="black" ,font="arial 15 ")
        self.quantity_tb.place(x=200,y=180)

        self.amount_tb = Label(self.right, text="Amount " ,fg="black" ,font="arial 15 ")
        self.amount_tb.place(x=400,y=180)

        self.fianl_price_l = Label(self.right, text=" " ,fg="black" ,font="arial 15 ")
        self.fianl_price_l.place(x=0,y=780)

        #---end of table

        #---search UI

        self.name_Search_l = Label(self.left ,text=" Enter product name ", font="arial 12 bold", fg="black",bg="white")
        self.name_Search_l.place(x=20,y=100)

        self.name_Search_e = Entry(self.left,width=25, font="arial 12 ", fg="darkBlue")
        self.name_Search_e.place(x=250,y=100)
        self.name_Search_e.focus()

        self.btn_search = Button(self.left,width=15,height=1,text="search " ,font="arial 12 ", fg="white",bg="blue",command=self.search)
        self.btn_search.place(x=550,y=95)

        #---end search ui

        #---show product info 
    
        self.product_name = Label(self.left,text="",font="arial 12 ", fg="black",bg="white")
        self.product_name.place(x=20,y="400")

        self.product_price = Label(self.left,text="",font="arial 12 ", fg="black",bg="white")
        self.product_price.place(x=20,y="450")

        self.product_stock = Label(self.left,text="",font="arial 12 ", fg="black",bg="white")
        self.product_stock.place(x=20,y="500")

        #---end show product inf0

    def search(self):
        sql = "SELECT * FROM inventory WHERE name=?"
        result = c.execute(sql,(self.name_Search_e.get(),))
     
        for r in result: 
            self.id = r[0] # id
            self.n1 = r[1] #name
            self.n2 = r[9] #sp
            self.n3 = r[2] #stock

        self.product_name.configure(text="product name : " + str(self.n1))
        self.product_price.configure(text="product price : " + str(self.n2) + " $")
        self.product_stock.configure(text="product amounts : " + str(self.n3))

        self.quantity_db = Label(self.left,text="Enter Quantity",font="arial 12 ", fg="black",bg="white")
        self.quantity_db.place(x=20,y="550")

        self.quantity_db_en = Entry(self.left,font="arial 12 ", fg="black",bg="white")
        self.quantity_db_en.place(x=220,y="550")

        self.btn_cart = Button(self.left,width=15,height=1,text="add to cart " ,font="arial 12 ", fg="white",bg="blue",command=self.add_to_cart)
        self.btn_cart.place(x=550,y=548)

    def add_to_cart(self):
        customer_amount = int(self.quantity_db_en.get())
        if customer_amount > self.n3:
            messagebox.showerror("error","please enter less or equla then the amount ! ")
        else:
            product_list.append(self.n1)
            product_quantity.append(customer_amount)
            f_p = float(self.n2 * customer_amount)
            product_price.append(f_p)
            product_id.append(self.id)

            row = 0
            column = 230
            column1 = 230
            column2= 230
            counter = 0
            sum = 0

            for self.p in product_list:
                self.product_tb_name = Label(self.right, text=str(self.p) ,fg="black" ,font="arial 15 ")
                self.product_tb_name.place(x=0,y=column)
                column +=50
                counter +=1
            for self.p in product_quantity:
                self.product_tb_quentity = Label(self.right, text=str(self.p),fg="black" ,font="arial 15 ")
                self.product_tb_quentity.place(x=200,y=column1)
                column1 +=50
            for self.p in product_price:
                self.product_tb_price = Label(self.right, text=str(self.p),fg="black" ,font="arial 15 ")
                self.product_tb_price.place(x=400,y=column2)
                column2 +=50
                sum += float(self.p)
            if sum > 0 :
                self.fianl_price_l.configure(text="final price  : " + str(sum) + " $")

            self.btn_check_out = Button(self.right,width=30,height=5,text=" check out and print bill " ,font="arial 12 ", fg="white",bg="blue",command=self.check_out)
            self.btn_check_out.place(x=0,y=848)
        
        self.quantity_db .place_forget()
        self.quantity_db_en .place_forget()
        self.btn_cart.destroy()
        self.product_name.configure(text="")
        self.product_price.configure(text="")
        self.product_stock.configure(text="")
        self.name_Search_e.delete(0,END)
        self.name_Search_e.focus()

    def check_out(self,  *args , **kwargs):
       path_file = "G:/pyhton/shop"
       directory = str(path_file) + "/bills/bills" + str(date) +"/"
       if  os.path.exists(directory) == False:
           os.makedirs(directory)
       print(os.path.exists(directory))
       file_name = str(directory)+str(random.randrange(1,100000))+".rtf"
       file = open(file_name,"w")
       counters = 0
       for f in product_list:
           file.write("\n\t\t\t\t"+str(counters+1)+"\t"+str(product_list[counters][:7])+"\t"+str(product_price[counters])+"\t"+str(product_quantity[counters]))
           counters +=1
       os.startfile(file_name, "print")
       file.close()
       self.x = 0
       intial = "SELECT * FROM inventory WHERE id=?"
       resualt = c.execute(intial,(product_id[self.x],))
  
       for i in product_list:
           for r in resualt:
             self.last_stock = r[2]
           self.new_stockss = int(self.last_stock) - int(product_quantity[self.x])
           sql = "UPDATE inventory SET stock=? WHERE id=?"
           c.execute(sql,(self.new_stockss,product_id[self.x]))
           conn.commit()
           self.x += 1

       messagebox.showinfo("updated","enjoy !")

                
  




root = Tk()
b = Datebase(root)
root.geometry("1700x900+0+0") 
root.title(" shop ")
root.mainloop()