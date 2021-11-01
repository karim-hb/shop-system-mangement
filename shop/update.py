from tkinter import *
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect("./store-db/store.db")
c = conn.cursor()



class Datebase:
    def __init__(self , master , *args , **kwargs):

        self.master = master
        self.heading = Label(master,text="update products ", font="arial 30 bold", fg="black")
        self.heading.place(x=750,y=20)

        self.id_l = Label(master,text=" Enter product id ", font="arial 12 bold", fg="black")
        self.id_l.place(x=10,y=100)

        self.name_l = Label(master,text=" Enter product name", font="arial 12 bold", fg="black")
        self.name_l.place(x=10,y=150)

        self.stock_l = Label(master,text=" Enter stock", font="arial 12 bold", fg="black")
        self.stock_l.place(x=10,y=200)

        self.sp_l = Label(master,text=" Enter cost price", font="arial 12 bold", fg="black")
        self.sp_l.place(x=10,y=250)

        self.cp_l = Label(master,text=" Enter selller price", font="arial 12 bold", fg="black")
        self.cp_l.place(x=10,y=300)

        self.vendor_l = Label(master,text=" Enter vendor name", font="arial 12 bold", fg="black")
        self.vendor_l.place(x=10,y=350)

        self.vendor_phone_number_l = Label(master,text=" Enter vendor phone number", font="arial 12 bold", fg="black")
        self.vendor_phone_number_l.place(x=10,y=400)

        self.id_e = Entry(master,width=25, font="arial 12 ", fg="darkBlue")
        self.id_e.place(x=250,y=100)

        self.name_e = Entry(master,width=25, font="arial 12 ", fg="darkBlue")
        self.name_e.place(x=250,y=150)

        self.stock_e = Entry(master,width=25, font="arial 12 ", fg="darkBlue")
        self.stock_e.place(x=250,y=200)

        self.sp_e = Entry(master,width=25, font="arial 12 ", fg="darkBlue")
        self.sp_e.place(x=250,y=250)

        self.cp_e = Entry(master,width=25, font="arial 12 ", fg="darkBlue")
        self.cp_e.place(x=250,y=300)

        self.vendor_e = Entry(master,width=25, font="arial 12 ", fg="darkBlue")
        self.vendor_e.place(x=250,y=350)

        self.vendor_phone_number_e = Entry(master,width=25, font="arial 12 ", fg="darkBlue")
        self.vendor_phone_number_e.place(x=250,y=400)

        self.btn_add = Button(master,width=25,height=1,text="Update" ,font="arial 12 ", fg="white",bg="green",command=self.update)
        self.btn_add.place(x=550,y=600)

        self.btn_clear = Button(master,width=25,height=1,text="Clear form" ,font="arial 12 ", fg="white",bg="orange",command=self.clear_item)
        self.btn_clear.place(x=850,y=600)

        self.btn_search = Button(master,width=15,height=1,text="search " ,font="arial 12 ", fg="white",bg="blue",command=self.search)
        self.btn_search.place(x=550,y=100)

        self.btn_clear = Button(master,width=25,height=1,text="Delete" ,font="arial 12 ", fg="white",bg="red",command=self.delete_item)
        self.btn_clear.place(x=1150,y=600)

    def search (self , *args , **kwargs):
        sql = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(sql,(self.id_e.get(),))
        for r in result:
            self.n1 = r[1] #name
            self.n2 = r[2] #stock
            self.n3 = r[3] #totalcp
            self.n4 = r[4] #totalsp
            self.n5 = r[5] #assume
            self.n6 = r[6] #vendor
            self.n7 = r[7] #vendor_phone_number
            self.n8 = r[8] #cp
            self.n9 = r[9] #sp

        conn.commit()
        self.name_e.delete(0,END)
        self.name_e.insert(0,str(self.n1))
        self.stock_e.delete(0,END)
        self.stock_e.insert(0,str(self.n2))
        self.sp_e.delete(0,END)
        self.sp_e.insert(0,str(self.n9))
        self.cp_e.delete(0,END)
        self.cp_e.insert(0,str(self.n8))
        self.vendor_e.delete(0,END)
        self.vendor_e.insert(0,str(self.n6))
        self.vendor_phone_number_e.delete(0,END)
        self.vendor_phone_number_e.insert(0,str(self.n7))


    def clear_item(self  , *args , **kwargs):
         self.id_e.delete(0,END)
         self.name_e.delete(0,END)
         self.stock_e.delete(0,END)
         self.sp_e.delete(0,END)
         self.cp_e.delete(0,END)
         self.vendor_e.delete(0,END)
         self.vendor_phone_number_e.delete(0,END)

    def update(self  , *args , **kwargs):
         self.name = self.name_e.get()
         self.stock = self.stock_e.get()
         self.sp = self.sp_e.get()
         self.cp = self.cp_e.get()
         self.vendor = self.vendor_e.get()
         self.vendor_phone_number = self.vendor_phone_number_e.get()
         self.total_cp = float(self.cp) * float(self.stock)
         self.total_sp = float(self.sp) * float(self.stock)
         self.assume_profit = float(self.total_sp) - float(self.total_cp)
         if(self.id_e == ""):
            messagebox.showerror("error","for add product please go to addProduct page here we just update product")
         elif self.name =="" or self.stock =="" or self.sp =="" or self.cp =="" or self.vendor =="" or  self.vendor =="":
             messagebox.showerror("error","please complete the form then sumbit it ")
         else:
             query = "UPDATE inventory SET name = ?,stock = ?,totalcp = ?,totalsp = ?,assume_profit = ?,vendor = ?,vendor_phone_number = ?,cp = ?,sp = ? WHERE id=?"
             c.execute(query,(self.name,self.stock,self.total_cp,self.total_sp,self.assume_profit,self.vendor,self.vendor_phone_number,self.cp,self.sp,self.id_e.get()))
             conn.commit()
             messagebox.showinfo("updated","product update successfully")

    def delete_item(self  , *args , **kwargs):
        if (self.id_e.get() != ""):
            messagebox.showerror("error","for add product please go to addProduct page here we just update product")
        else:
            intial = "DELETE FROM inventory WHERE id=?;"
            c.execute(intial,(self.id_e.get()))
            conn.commit()
            messagebox.showinfo("updated","product remove successfully")
            self.id_e.delete(0,END)
            self.name_e.delete(0,END)
            self.stock_e.delete(0,END)
            self.sp_e.delete(0,END)
            self.cp_e.delete(0,END)
            self.vendor_e.delete(0,END)
            self.vendor_phone_number_e.delete(0,END)




root = Tk()
b = Datebase(root)
root.geometry("1700x900+30+30") 
root.title("ویرایش کردن کالا")
root.mainloop()