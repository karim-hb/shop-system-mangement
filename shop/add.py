from tkinter import *
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect("./store-db/store.db")
c = conn.cursor()


resualt = c.execute("SELECT Max(id) from inventory")
for r in resualt:
    id = r[0]


class Datebase:
    def __init__(self , master , *args , **kwargs):

        self.master = master
        self.heading = Label(master,text="add new products ", font="arial 30 bold", fg="black")
        self.heading.place(x=750,y=20)


        self.name_l = Label(master,text=" Enter product name", font="arial 12 bold", fg="black")
        self.name_l.place(x=10,y=100)

        self.stock_l = Label(master,text=" Enter stock", font="arial 12 bold", fg="black")
        self.stock_l.place(x=10,y=150)

        self.sp_l = Label(master,text=" Enter cost price", font="arial 12 bold", fg="black")
        self.sp_l.place(x=10,y=200)

        self.cp_l = Label(master,text=" Enter selller price", font="arial 12 bold", fg="black")
        self.cp_l.place(x=10,y=250)

        self.vendor_l = Label(master,text=" Enter vendor name", font="arial 12 bold", fg="black")
        self.vendor_l.place(x=10,y=300)

        self.vendor_phone_number_l = Label(master,text=" Enter vendor phone number", font="arial 12 bold", fg="black")
        self.vendor_phone_number_l.place(x=10,y=350)

        self.name_e = Entry(master,width=25, font="arial 12 ", fg="darkBlue")
        self.name_e.place(x=250,y=100)

        self.stock_e = Entry(master,width=25, font="arial 12 ", fg="darkBlue")
        self.stock_e.place(x=250,y=150)

        self.sp_e = Entry(master,width=25, font="arial 12 ", fg="darkBlue")
        self.sp_e.place(x=250,y=200)

        self.cp_e = Entry(master,width=25, font="arial 12 ", fg="darkBlue")
        self.cp_e.place(x=250,y=250)

        self.vendor_e = Entry(master,width=25, font="arial 12 ", fg="darkBlue")
        self.vendor_e.place(x=250,y=300)

        self.vendor_phone_number_e = Entry(master,width=25, font="arial 12 ", fg="darkBlue")
        self.vendor_phone_number_e.place(x=250,y=350)

        self.btn_add = Button(master,width=25,height=1,text="Sumbit" ,font="arial 12 ", fg="white",bg="green",command=self.get_item)
        self.btn_add.place(x=550,y=550)

        self.btn_clear = Button(master,width=25,height=1,text="Clear form" ,font="arial 12 ", fg="white",bg="red",command=self.clear_item)
        self.btn_clear.place(x=850,y=550)

        self.details = Text(master,width=55,height=15,font="arial 12 ", fg="darkBlue")
        self.details.place(x=1000,y=90)
        self.details.insert(END,"inventory   : "+ str(id))


    def get_item(self  , *args , **kwargs):
         self.name = self.name_e.get()
         self.stock = self.stock_e.get()
         self.sp = self.sp_e.get()
         self.cp = self.cp_e.get()
         self.vendor = self.vendor_e.get()
         self.vendor_phone_number = self.vendor_phone_number_e.get()
         self.total_cp = float(self.cp) * float(self.stock)
         self.total_sp = float(self.sp) * float(self.stock)
         self.assume_profit = float(self.total_sp) - float(self.total_cp)
         if self.name =="" or self.stock =="" or self.sp =="" or self.cp =="" or self.vendor =="" or  self.vendor =="":
             messagebox.showerror("error","please complete the form then sumbit it ")
         else:
             sql = "INSERT INTO inventory (name,stock,totalcp,totalsp,assume_profit,vendor,vendor_phone_number,cp,sp) VALUES (?,?,?,?,?,?,?,?,?)"
             c.execute(sql,(self.name,self.stock,self.total_cp,self.total_sp,self.assume_profit,self.vendor,self.vendor_phone_number,self.cp,self.sp))
             conn.commit()

             messagebox.showinfo("updated","product add successfully")
             self.details.insert(END,"\n product add : "+ str(self.name))
    def clear_item(self  , *args , **kwargs):
         self.name_e.delete(0,END)
         self.stock_e.delete(0,END)
         self.sp_e.delete(0,END)
         self.cp_e.delete(0,END)
         self.vendor_e.delete(0,END)
         self.vendor_phone_number_e.delete(0,END)

root = Tk()
b = Datebase(root)
root.geometry("1700x900+30+30") 
root.title("اضافه کردن کالا")
root.mainloop()