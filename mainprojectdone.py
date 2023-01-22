from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql as py
import random


class super_market():
    
    def  __init__(self,win):
        self.win = win
        self.win.geometry('2000x900')
        self.win.title("sp")

        self.lbltitle=Label(self.win,text='AK Super Market',bg='white',fg='black',font=("times new roman",35,'bold'))
        self.lbltitle.place(x=0,y=0,width=1400,height=50)

        self.aashirvaad=IntVar()
        self.rice=IntVar()
        self.refinedoil=IntVar()
        self.dhall=IntVar()
        self.maida=IntVar()
        self.chilli=IntVar()
        self.sugar=IntVar()
        self.salt=IntVar()
        self.milk=IntVar()
        self.egg=IntVar()
        self.lays=IntVar()
        self.biscuit=IntVar()
        self.icecream=IntVar()
        self.cake=IntVar()
        self.juice=IntVar()
        self.chocolates=IntVar()
        self.bread=IntVar()
        self.waffers=IntVar()
        self.jam=IntVar()
        self.nuts=IntVar()
        self.pencil=IntVar()
        self.pen=IntVar()
        self.note=IntVar()
        self.marker=IntVar()
        self.scale=IntVar()
        self.pad=IntVar()
        self.inkbottle=IntVar()
        self.stabler=IntVar()
        self.a4sheet=IntVar()
        self.file=IntVar()
        self.dragon=IntVar()
        self.kiwi=IntVar()
        self.avagado=IntVar()
        self.strawberry=IntVar()
        self.litchi=IntVar()
        self.onion=IntVar()
        self.tomato=IntVar()
        self.carrot=IntVar()
        self.brinjal=IntVar()
        self.greens=IntVar()
        self.total_gro=StringVar()
        self.total_veg=StringVar()
        self.total_stat=StringVar()
        self.total_sna=StringVar()
        self.c_cusname=StringVar()
        self.billno=StringVar()
        x=random.randint(1000,9999)
        self.billno.set(str(x))
        self.mobno=StringVar()
        self.email=StringVar()

#Customer Details----------------------------------------------------------------
        
        details=LabelFrame(self.win,text="Customer Details",font=('arial',12),bg="black",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=50,relwidth=1)
    
        billno=Label(details,text="Bill Number",font=('arial',15),bg="black",fg="white").grid(row=0,column=0,padx=15)
        billnoentry=Entry(details,borderwidth=4,textvariable=self.billno,width=30).grid(row=0,column=1,padx=8)
    
        cusname=Label(details,text="Customer Name",font=('arial',15),bg="black",fg="white").grid(row=0,column=2,padx=15)
        cusnameentry=Entry(details,borderwidth=4,textvariable=self.c_cusname,width=30).grid(row=0,column=3,padx=8)

        mobno=Label(details,text="Mobile Number",font=('arial',15),bg="black",fg="white").grid(row=0,column=4,padx=15)
        mobnoentry=Entry(details,borderwidth=4,textvariable=self.mobno,width=30).grid(row=0,column=5,padx=8)
    
        email=Label(details,text="Email id",font=('arial',15),bg="black",fg="white").grid(row=0,column=6,padx=15)
        emailentry=Entry(details,borderwidth=4,textvariable=self.email,width=30).grid(row=0,column=7,padx=8)


#Grocery----------------------------------------------------------------------------

        gro=LabelFrame(self.win,text="Grocery",font=('arial',13),bg="black",fg="white",relief=GROOVE,bd=10)
        gro.place(x=5,y=120,width=280,height=480)
    
        aash=Label(gro,text="Aashirvaad",font=("Black",11),bg="black",fg="white").grid(row=0,column=0,pady=11)
        aash_entry=Entry(gro,borderwidth=2,textvariable=self.aashirvaad,width=15).grid(row=0,column=1,padx=10)
    
        rice=Label(gro,text="Rice",font=("Black",11),bg="black",fg="white").grid(row=1,column=0,pady=11)
        rice_entry=Entry(gro,borderwidth=2,textvariable=self.rice,width=15).grid(row=1,column=1,padx=10)

        maida=Label(gro,text="Maida",font=("Black",11),bg="black",fg="white").grid(row=2,column=0,pady=11)
        maida_entry=Entry(gro,borderwidth=2,textvariable=self.maida,width=15).grid(row=2,column=1,padx=10)

        refinedoil=Label(gro,text="Refined Oil",font=("Black",11),bg="black",fg="white").grid(row=3,column=0,pady=11)
        refinedoil_entry=Entry(gro,borderwidth=2,textvariable=self.refinedoil,width=15).grid(row=3,column=1,padx=10)

        milk=Label(gro,text="Milk",font=("Black",11),bg="black",fg="white").grid(row=4,column=0,pady=11)
        milk_entry=Entry(gro,borderwidth=2,textvariable=self.milk,width=15).grid(row=4,column=1,padx=10)

        egg=Label(gro,text="Egg",font=("Black",11),bg="black",fg="white").grid(row=5,column=0,pady=11)
        egg_entry=Entry(gro,borderwidth=2,textvariable=self.egg,width=15).grid(row=5,column=1,padx=10)

        sugar=Label(gro,text="Sugar",font=("Black",11),bg="black",fg="white").grid(row=6,column=0,pady=11)
        sugar_entry=Entry(gro,borderwidth=2,textvariable=self.sugar,width=15).grid(row=6,column=1,padx=10)

        salt=Label(gro,text="Salt",font=("Black",11),bg="black",fg="white").grid(row=7,column=0,pady=11)
        salt_entry=Entry(gro,borderwidth=2,textvariable=self.salt,width=15).grid(row=7,column=1,padx=10)

        dhall=Label(gro,text="Dhall",font=("Black",11),bg="black",fg="white").grid(row=8,column=0,pady=11)
        dhall_entry=Entry(gro,borderwidth=2,textvariable=self.dhall,width=15).grid(row=8,column=1,padx=10)

        chilli=Label(gro,text="Chilli",font=("Black",11),bg="black",fg="white").grid(row=9,column=0,pady=11)
        chilli_entry=Entry(gro,borderwidth=2,textvariable=self.chilli,width=15).grid(row=9,column=1,padx=10)
    
#Fruits&veg---------------------------------------------------------------------------------

        veg=LabelFrame(self.win,text="Fruits&Veg",font=('arial',13),bg="black",fg="white",relief=GROOVE,bd=10)
        veg.place(x=290,y=120,width=280,height=480)

        onion=Label(veg,text="Onion",font=("Black",11),bg="black",fg="white").grid(row=0,column=0,pady=11)
        onion_entry=Entry(veg,borderwidth=2,textvariable=self.onion,width=15).grid(row=0,column=1,padx=10)

        tomato=Label(veg,text="Tomato",font=("Black",11),bg="black",fg="white").grid(row=1,column=0,pady=11)
        tomato_entry=Entry(veg,borderwidth=2,textvariable=self.tomato,width=15).grid(row=1,column=1,padx=10)

        brinjal=Label(veg,text="Brinjal",font=("Black",11),bg="black",fg="white").grid(row=2,column=0,pady=11)
        brinjal_entry=Entry(veg,borderwidth=2,textvariable=self.brinjal,width=15).grid(row=2,column=1,padx=10)

        carrot=Label(veg,text="Carrot",font=("Black",11),bg="black",fg="white").grid(row=3,column=0,pady=11)
        carrot_entry=Entry(veg,borderwidth=2,textvariable=self.carrot,width=15).grid(row=3,column=1,padx=10)

        greens=Label(veg,text="Greens",font=("Black",11),bg="black",fg="white").grid(row=4,column=0,pady=11)
        greens_entry=Entry(veg,borderwidth=2,textvariable=self.greens,width=15).grid(row=4,column=1,padx=10)

        dragon=Label(veg,text="Dragon",font=("Black",11),bg="black",fg="white").grid(row=5,column=0,pady=11)
        dragon_entry=Entry(veg,borderwidth=2,textvariable=self.dragon,width=15).grid(row=5,column=1,padx=10)

        kiwi=Label(veg,text="Kiwi",font=("Black",11),bg="black",fg="white").grid(row=6,column=0,pady=11)
        kiwi_entry=Entry(veg,borderwidth=2,textvariable=self.kiwi,width=15).grid(row=6,column=1,padx=10)

        avagado=Label(veg,text="Avagado",font=("Black",11),bg="black",fg="white").grid(row=7,column=0,pady=11)
        avagado_entry=Entry(veg,borderwidth=2,textvariable=self.avagado,width=15).grid(row=7,column=1,padx=10)

        strawberry=Label(veg,text="Strawberry",font=("Black",11),bg="black",fg="white").grid(row=8,column=0,pady=11)
        strawberry_entry=Entry(veg,borderwidth=2,textvariable=self.strawberry,width=15).grid(row=8,column=1,padx=10)

        litchi=Label(veg,text="Litchi",font=("Black",11),bg="black",fg="white").grid(row=9,column=0,pady=11)
        litchi_entry=Entry(veg,borderwidth=2,textvariable=self.litchi,width=15).grid(row=9,column=1,padx=10)

#Stationary-----------------------------------------------------------------------

        stat=LabelFrame(self.win,text="Stationary",font=('arial',13),bg="black",fg="white",relief=GROOVE,bd=10)
        stat.place(x=575,y=120,width=280,height=480)

        pencil=Label(stat,text="Pencil",font=("Black",11),bg="black",fg="white").grid(row=0,column=0,pady=11)
        pencil_entry=Entry(stat,borderwidth=2,textvariable=self.pencil,width=15).grid(row=0,column=1,padx=10)

        pen=Label(stat,text="Pen",font=("Black",11),bg="black",fg="white").grid(row=1,column=0,pady=11)
        pen_entry=Entry(stat,borderwidth=2,textvariable=self.pen,width=15).grid(row=1,column=1,padx=10)

        marker=Label(stat,text="Marker",font=("Black",11),bg="black",fg="white").grid(row=2,column=0,pady=11)
        marker_entry=Entry(stat,borderwidth=2,textvariable=self.marker,width=15).grid(row=2,column=1,padx=10)

        scale=Label(stat,text="Scale",font=("Black",11),bg="black",fg="white").grid(row=3,column=0,pady=11)
        scale_entry=Entry(stat,borderwidth=2,textvariable=self.scale,width=15).grid(row=3,column=1,padx=10)

        pad=Label(stat,text="Pad",font=("Black",11),bg="black",fg="white").grid(row=4,column=0,pady=11)
        pad_entry=Entry(stat,borderwidth=2,textvariable=self.pad,width=15).grid(row=4,column=1,padx=10)

        inkbottle=Label(stat,text="InkBottle",font=("Black",11),bg="black",fg="white").grid(row=5,column=0,pady=11)
        inkbottle_entry=Entry(stat,borderwidth=2,textvariable=self.inkbottle,width=15).grid(row=5,column=1,padx=10)

        a4=Label(stat,text="A4Sheet",font=("Black",11),bg="black",fg="white").grid(row=6,column=0,pady=11)
        a4_entry=Entry(stat,borderwidth=2,textvariable=self.a4sheet,width=15).grid(row=6,column=1,padx=10)

        stabler=Label(stat,text="Stabler",font=("Black",11),bg="black",fg="white").grid(row=7,column=0,pady=11)
        stabler_entry=Entry(stat,borderwidth=2,textvariable=self.stabler,width=15).grid(row=7,column=1,padx=10)

        file=Label(stat,text="File",font=("Black",11),bg="black",fg="white").grid(row=8,column=0,pady=11)
        file_entry=Entry(stat,borderwidth=2,textvariable=self.file,width=15).grid(row=8,column=1,padx=10)

        note=Label(stat,text="Note",font=("Black",11),bg="black",fg="white").grid(row=9,column=0,pady=11)
        note_entry=Entry(stat,borderwidth=2,textvariable=self.note,width=15).grid(row=9,column=1,padx=10)

#Snacks-------------------------------------------------------------------------------

        sna=LabelFrame(self.win,text="Snacks",font=('arial',13),bg="black",fg="white",relief=GROOVE,bd=10)
        sna.place(x=860,y=120,width=280,height=480)

        lays=Label(sna,text="Lays",font=("Black",11),bg="black",fg="white").grid(row=0,column=0,pady=11)
        lays_entry=Entry(sna,borderwidth=2,textvariable=self.lays,width=15).grid(row=0,column=1,padx=10)

        bis=Label(sna,text="Biscuit",font=("Black",11),bg="black",fg="white").grid(row=1,column=0,pady=11)
        bis_entry=Entry(sna,borderwidth=2,textvariable=self.biscuit,width=15).grid(row=1,column=1,padx=10)

        ice=Label(sna,text="IceCream",font=("Black",11),bg="black",fg="white").grid(row=2,column=0,pady=11)
        ice_entry=Entry(sna,borderwidth=2,textvariable=self.icecream,width=15).grid(row=2,column=1,padx=10)

        cake=Label(sna,text="Cake",font=("Black",11),bg="black",fg="white").grid(row=3,column=0,pady=11)
        cake_entry=Entry(sna,borderwidth=2,textvariable=self.cake,width=15).grid(row=3,column=1,padx=10)

        jui=Label(sna,text="Juice",font=("Black",11),bg="black",fg="white").grid(row=4,column=0,pady=11)
        jui_entry=Entry(sna,borderwidth=2,textvariable=self.juice,width=15).grid(row=4,column=1,padx=10)

        cho=Label(sna,text="Chocolates",font=("Black",11),bg="black",fg="white").grid(row=5,column=0,pady=11)
        cho_entry=Entry(sna,borderwidth=2,textvariable=self.chocolates,width=15).grid(row=5,column=1,padx=10)

        bre=Label(sna,text="Bread",font=("Black",11),bg="black",fg="white").grid(row=6,column=0,pady=11)
        bre_entry=Entry(sna,borderwidth=2,textvariable=self.bread,width=15).grid(row=6,column=1,padx=10)

        waf=Label(sna,text="Waffers",font=("Black",11),bg="black",fg="white").grid(row=7,column=0,pady=11)
        waf_entry=Entry(sna,borderwidth=2,textvariable=self.waffers,width=15).grid(row=7,column=1,padx=10)

        jam=Label(sna,text="Jam",font=("Black",11),bg="black",fg="white").grid(row=8,column=0,pady=11)
        jam_entry=Entry(sna,borderwidth=2,textvariable=self.jam,width=15).grid(row=8,column=1,padx=10)

        nut=Label(sna,text="Nuts",font=("Black",11),bg="black",fg="white").grid(row=9,column=0,pady=11)
        nut_entry=Entry(sna,borderwidth=2,textvariable=self.nuts,width=15).grid(row=9,column=1,padx=10)


#Bill counter----------------------------------------------------------------------------------
        
        billcounter=Frame(self.win,bd=10,relief=GROOVE,bg="black")
        billcounter.place(x=1130,y=120,width=225,height=372)
        
        bill_title=Label(billcounter,text="Bill Counter",font=("Black",17),bd=7,relief=GROOVE,bg="black",fg="white").pack(fill=X)
        
        '''scrol_x=Scrollbar(billcounter,orient=HORIZONTAL)
        self.txtarea=Text(billcounter,xscrollcommand=scrol_x.set)
        scrol_x.pack(side=RIGHT,fill=X)
        scrol_x.config(command=self.txtarea.xview)
        self.txtarea.pack(fill=BOTH,expand=1)'''
        scrol_y=Scrollbar(billcounter,orient=VERTICAL)
        self.txtarea=Text(billcounter,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)


        button_frame=Frame(self.win,bd=7,relief=GROOVE,bg="white")
        button_frame.place(x=910,y=600,width=450,height=95)

        button_total=Button(button_frame,text="Total",font=("Arial Black",15),pady=10,bg="black",fg="white",command=self.total).grid(row=0,column=0,padx=12)
        button_save=Button(button_frame,text="save",font=("Arial Black",15),pady=10,bg="black",fg="white",command=self.save).grid(row=0,column=1,padx=12)
        button_clear=Button(button_frame,text="Clear",font=("Arial Black",15),pady=10,bg="black",fg="white",command=self.clear).grid(row=0,column=2,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Arial Black",14),pady=10,bg="black",fg="white",width=8,command=self.exit1).grid(row=0,column=3,padx=10,pady=6)
    
#Billing menu----------------------------------------------------------------------------------------------
        
        billing_menu=LabelFrame(self.win,text="Bill Sum",font=("Black",12),relief=GROOVE,bd=10,bg="black",fg="white")
        billing_menu.place(x=0,y=600,width=800,height=150)
        
        total_gro=Label(billing_menu,text="Total Grocery Price",font=("Black",11),bg="black",fg="white").grid(row=0,column=0)
        total_gro_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_gro).grid(row=0,column=1,padx=10,pady=7)
        
        total_veg=Label(billing_menu,text="Total fruits&veg Price",font=("Black",11),bg="black",fg="white").grid(row=1,column=0)
        total_veg_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_veg).grid(row=1,column=1,padx=10,pady=7)

        total_stat=Label(billing_menu,text="Total stationary price",font=("Black",11),bg="black",fg="white").grid(row=0,column=2)
        tax_stat_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_stat).grid(row=0,column=3,padx=10,pady=7)
        
        tax_sna=Label(billing_menu,text="Total snacks price",font=("Black",11),bg="black",fg="white").grid(row=1,column=2)
        tax_sna_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_sna).grid(row=1,column=3,padx=10,pady=7)


#Total---------------------------------------------------------------------------------------- 

    def total(self):
            
        if (self.c_cusname.get=="" or self.mobno.get()=="" or self.billno.get()=="" or self.email.get()==""):
            messagebox.showerror("Error", "Fill the complete Customer Details!!",parent=self.win)
        else:
            self.aash=self.aashirvaad.get()*50
            self.ri=self.rice.get()*60
            self.oil=self.refinedoil.get()*218
            self.ma=self.maida.get()*65
            self.mi=self.milk.get()*44
            self.eg=self.egg.get()*7
            self.sg=self.sugar.get()*112
            self.sa=self.salt.get()*120
            self.dh=self.dhall.get()*80
            self.ch=self.chilli.get()*229
            total_gro=(self.aash+self.ri+self.oil+self.ma+self.mi+self.eg+self.sg+self.sa+self.dh+self.ch)
            self.total_gro.set(str(total_gro)+" Rs")
       

            self.on=self.onion.get()*45
            self.tm=self.tomato.get()*34
            self.br=self.brinjal.get()*54
            self.cr=self.carrot.get()*65
            self.gr=self.greens.get()*20
            self.dr=self.dragon.get()*156
            self.ki=self.kiwi.get()*210
            self.av=self.avagado.get()*180
            self.st=self.strawberry.get()*276
            self.li=self.litchi.get()*189
            total_veg=(self.on+self.tm+self.br+self.cr+self.gr+self.dr+self.ki+self.av+self.st+self.li)
            self.total_veg.set(str(total_veg)+" Rs")
        


            self.pn=self.pencil.get()*13
            self.pe=self.pen.get()*10
            self.mr=self.marker.get()*56
            self.sc=self.scale.get()*12
            self.pd=self.pad.get()*120
            self.ink=self.inkbottle.get()*85
            self.a4=self.a4sheet.get()*210
            self.st=self.stabler.get()*76
            self.fi=self.file.get()*80
            self.no=self.note.get()*65
            total_stat=(self.pn+self.pe+self.mr+self.sc+self.pd+self.ink+self.a4+self.st+self.fi+self.no)
            self.total_stat.set(str(total_stat)+" Rs")
        


            self.ly=self.lays.get()*10
            self.bi=self.biscuit.get()*20
            self.ice=self.icecream.get()*45
            self.ca=self.cake.get()*34
            self.ju=self.juice.get()*64
            self.ch=self.chocolates.get()*10
            self.br=self.bread.get()*45
            self.wa=self.waffers.get()*23
            self.ja=self.jam.get()*67
            self.nu=self.nuts.get()*89
            total_sna=(self.ly+self.bi+self.ice+self.ca+self.ju+self.ch+self.br+self.wa+self.ja+self.nu)
            self.total_sna.set(str(total_sna)+" Rs")
            

            self.total_all_bill=(total_gro+total_veg+total_stat+total_sna)
                    
            self.total_all_bill=str(self.total_all_bill)+" Rs"
            self.billarea()


    def intro(self):
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(END,f"\tWELCOME TO AK SUPER MARKET\n\tPhone-No.7358651802")
        self.txtarea.insert(END,f"\n\nBill no. : {self.billno.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.c_cusname.get()}")
        self.txtarea.insert(END,f"\nPhone No. : {self.mobno.get()}")
        self.txtarea.insert(END,f"\nEmail.:{self.email.get()}")
        self.txtarea.insert(END,"\n====================================\n")
        self.txtarea.insert(END,"\nProd\t\tQty\tPrice\n")
        self.txtarea.insert(END,"\n====================================\n")
            


    def billarea(self):

        self.intro()
        
        if self.aashirvaad.get()!=0:
            self.txtarea.insert(END,f"Aashirvaad\t\t {self.aashirvaad.get()}\t{self.aash}\n")
        if self.rice.get()!=0:
            self.txtarea.insert(END,f"Rice\t\t {self.rice.get()}\t{self.ri}\n")
        if self.refinedoil.get()!=0:
           self.txtarea.insert(END,f"RefinedOil\t\t {self.refinedoil.get()}\t{self.oil}\n")
        if self.maida.get()!=0:
            self.txtarea.insert(END,f"Maida\t\t {self.maida.get()}\t{self.ma}\n")
        if self.milk.get()!=0:
            self.txtarea.insert(END,f"Milk\t\t {self.milk.get()}\t{self.mi}\n")
        if self.egg.get()!=0:
            self.txtarea.insert(END,f"Egg\t\t {self.egg.get()}\t{self.eg}\n")
        if self.sugar.get()!=0:
            self.txtarea.insert(END,f"Sugar\t\t {self.sugar.get()}\t{self.sg}\n")
        if self.salt.get()!=0:
            self.txtarea.insert(END,f"Salt\t\t {self.salt.get()}\t{self.sa}\n")
        if self.dhall.get()!=0:
            self.txtarea.insert(END,f"Dhall\t\t {self.dhall.get()}\t{self.dh}\n")
        if self.chilli.get()!=0:
            self.txtarea.insert(END,f"Chilli\t\t {self.chilli.get()}\t{self.ch}\n")
        if self.onion.get()!=0:
            self.txtarea.insert(END,f"Onion\t\t {self.onion.get()}\t{self.on}\n")
        if self.tomato.get()!=0:
            self.txtarea.insert(END,f"Tomato\t\t {self.tomato.get()}\t{self.tm}\n")
        if self.brinjal.get()!=0:
            self.txtarea.insert(END,f"Brinjal\t\t {self.brinjal.get()}\t{self.br}\n")
        if self.carrot.get()!=0:
            self.txtarea.insert(END,f"Carrot\t\t {self.carrot.get()}\t{self.cr}\n")
        if self.greens.get()!=0:
            self.txtarea.insert(END,f"Greens\t\t {self.greens.get()}\t{self.gr}\n")
        if self.dragon.get()!=0:
            self.txtarea.insert(END,f"Dragon\t\t {self.dragon.get()}\t{self.dr}\n")
        if self.kiwi.get()!=0:
            self.txtarea.insert(END,f"kiwi\t\t {self.kiwi.get()}\t{self.ki}\n")
        if self.avagado.get()!=0:
            self.txtarea.insert(END,f"Avagado\t\t {self.avagado.get()}\t{self.av}\n")
        if self.strawberry.get()!=0:
            self.txtarea.insert(END,f"Strawberry\t\t {self.strawberry.get()}\t{self.st}\n")
        if self.litchi.get()!=0:
            self.txtarea.insert(END,f"Litchi\t\t {self.litchi.get()}\t{self.li}\n")
        if self.pencil.get()!=0:
            self.txtarea.insert(END,f"Pencil\t\t {self.pencil.get()}\t{self.pn}\n")
        if self.pen.get()!=0:
            self.txtarea.insert(END,f"Pen\t\t {self.pen.get()}\t{self.pe}\n")
        if self.marker.get()!=0:
            self.txtarea.insert(END,f"Marker\t\t {self.marker.get()}\t{self.mr}\n")
        if self.scale.get()!=0:
            self.txtarea.insert(END,f"Scale\t\t {self.scale.get()}\t{self.sc}\n")
        if self.pad.get()!=0:
            self.txtarea.insert(END,f"Pad\t\t {self.pad.get()}\t{self.pd}\n")
        if self.inkbottle.get()!=0:
            self.txtarea.insert(END,f"InkBottle\t\t {self.inkbottle.get()}\t{self.ink}\n")
        if self.a4sheet.get()!=0:
            self.txtarea.insert(END,f"A4Sheet\t\t {self.a4sheet.get()}\t{self.a4}\n")
        if self.stabler.get()!=0:
            self.txtarea.insert(END,f"Stabler\t\t {self.stabler.get()}\t{self.st}\n")
        if self.file.get()!=0:
            self.txtarea.insert(END,f"File\t\t {self.file.get()}\t{self.fi}\n")
        if self.note.get()!=0:
            self.txtarea.insert(END,f"Note\t\t {self.note.get()}\t{self.no}\n")
        if self.lays.get()!=0:
            self.txtarea.insert(END,f"Lays\t\t {self.lays.get()}\t{self.ly}\n")
        if self.biscuit.get()!=0:
            self.txtarea.insert(END,f"Biscuit\t\t {self.biscuit.get()}\t{self.bi}\n")
        if self.icecream.get()!=0:
            self.txtarea.insert(END,f"IceCream\t\t {self.icecream.get()}\t{self.ice}\n")
        if self.cake.get()!=0:
            self.txtarea.insert(END,f"Cake\t\t {self.cake.get()}\t{self.ca}\n")
        if self.juice.get()!=0:
            self.txtarea.insert(END,f"Juice\t\t {self.juice.get()}\t{self.ju}\n")
        if self.chocolates.get()!=0:
            self.txtarea.insert(END,f"Chocolates\t\t {self.chocolates.get()}\t{self.ch}\n")
        if self.bread.get()!=0:
            self.txtarea.insert(END,f"Bread\t\t {self.bread.get()}\t{self.br}\n")
        if self.waffers.get()!=0:
            self.txtarea.insert(END,f"Waffers\t\t {self.waffers.get()}\t{self.wa}\n")
        if self.jam.get()!=0:
            self.txtarea.insert(END,f"Jam\t\t {self.jam.get()}\t{self.ja}\n")
        if self.nuts.get()!=0:
            self.txtarea.insert(END,f"Nuts\t\t {self.nuts.get()}\t{self.nu}\n")

        self.txtarea.insert(END,f"------------------------------------\n")
        self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bill}\n")
        self.txtarea.insert(END,f"------------------------------------\n")
        

    def save(self):

        op=messagebox.askyesno("Save","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.txtarea.get(1.0,END)
            f1=open("supermarket bill.txt",'w+')
            f1.write(self.bill_data)
            op1=messagebox.showinfo("Saved",f"Bill no:{self.billno.get()} Saved Successfully")
            f1.close()

            e_billno =self.billno.get()
            e_name = self.c_cusname.get()
            e_mobile = self.mobno.get()
            e_email = self.email.get()

            conn = py.connect(host="localhost",user="root", password="",  database="super_market")
            cur = conn.cursor()
            cur.execute("insert into billing(name,billno, mobileno,email) values( '"+e_name+"', '"+e_billno+"','"+e_mobile+"','"+e_email+"')")
            cur.fetchall()
            messagebox.showinfo('info','data inserted',parent = self.win)
            conn.close()



    def clear(self):
        
        self.txtarea.delete(1.0,END)
        self.aashirvaad.set(0)
        self.rice.set(0)
        self.refinedoil.set(0)
        self.maida.set(0)
        self.milk.set(0)
        self.egg.set(0)
        self.sugar.set(0)
        self.salt.set(0)
        self.dhall.set(0)
        self.chilli.set(0)
        self.onion.set(0)
        self.tomato.set(0)
        self.brinjal.set(0)
        self.carrot.set(0)
        self.greens.set(0)
        self.dragon.set(0)
        self.kiwi.set(0)
        self.avagado.set(0)
        self.strawberry.set(0)
        self.litchi.set(0)
        self.pencil.set(0)
        self.pen.set(0)
        self.marker.set(0)
        self.scale.set(0)
        self.pad.set(0)
        self.inkbottle.set(0)
        self.a4sheet.set(0)
        self.stabler.set(0)
        self.file.set(0)
        self.note.set(0)
        self.lays.set(0)
        self.biscuit.set(0)
        self.icecream.set(0)
        self.cake.set(0)
        self.juice.set(0)
        self.chocolates.set(0)
        self.bread.set(0)
        self.waffers.set(0)
        self.jam.set(0)
        self.nuts.set(0)
        self.total_gro.set(0)
        self.total_veg.set(0)
        self.total_stat.set(0)
        self.total_sna.set(0)
        self.c_cusname.set(0)
        self.billno.set(0)
        self.email.set(0)
        self.mobno.set(0)

    def exit1(self):
        ex=messagebox.askyesno("Exit","Do you want to exit")
        self.win.destroy()

if __name__=="__main__":
    
    win = Toplevel()
    k=super_market(win)
    win.mainloop()

    
     





