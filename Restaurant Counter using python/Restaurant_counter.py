from tkinter import *
import time
import datetime
from tkinter import messagebox

# -----Basic-----
bgc="cyan"
root = Tk()
root.title("Restaurant Billing Unit")
root.config(bg=bgc)
root.geometry("1330x720+10+10")

#------Time and date-----
def clock_time():
    time= datetime.datetime.now()
    time= (time.strftime("Date: %d/%m/%Y Time: %I:%M:%S %p"))
    txt.set(time)
    root.after(1,clock_time)

root.after(1,clock_time)
txt = StringVar()
lbl = Label(root,textvariable=txt,foreground= "black",background= bgc)
lbl.place(relx=0.556,rely=0.08)

# ------Pre styles-------
font1="{Calisto MT} 30 bold"
font2="{Bookman Old Style} 13 bold"
font3="{Arial } 15"
localt = time.asctime(time.localtime(time.time()))

#-----Price of food Item------ 
f1="15"
f2="20"
f3="50"
f4="25"
f5="20"
f6="20"
f7="30"
f8="50"
f9="100"
f10="20"
f11="15"
f12="60"
f13="80"
f14="70"
f15="70"
f16="90"

# -----Define----
def on_enter(e):
    close.config(background='red', foreground= "white")
def on_leave(e):
    close.config(background= '#002fff', foreground= 'white')

def lst():
    bgr="blue"
    sec_root = Toplevel()
    sec_root.title("Menu")
    sec_root.config(bg=bgr)
    sec_root.geometry("300x600+1000+50")

    itm = Label(sec_root,text="Items ",font=("Georgia",20,"bold"),bg=bgr,fg="red")
    itm.place(relx=0.05,rely=0.01)

    price = Label(sec_root,text="  ₹",font=("Georgia",20,"bold"),bg=bgr,fg="red")
    price.place(relx=0.55,rely=0.01)

    itm1=Label(sec_root,text="Cold Drink",font=("arial",15),bg=bgr,fg="yellow")
    itm1.place(relx=0.05,rely=0.13)
    itm2=Label(sec_root,text="Coffee",font=("arial",15),bg=bgr,fg="yellow")
    itm2.place(relx=0.05,rely=0.18)
    itm3=Label(sec_root,text="Cold Coffee",font=("arial",15),bg=bgr,fg="yellow")
    itm3.place(relx=0.05,rely=0.23)
    itm4=Label(sec_root,text="Tea",font=("arial",15),bg=bgr,fg="yellow")
    itm4.place(relx=0.05,rely=0.28)
    itm5=Label(sec_root,text="Lemon Tea",font=("arial",15),bg=bgr,fg="yellow")
    itm5.place(relx=0.05,rely=0.33)
    itm6=Label(sec_root,text="Coke",font=("arial",15),bg=bgr,fg="yellow")
    itm6.place(relx=0.05,rely=0.38)
    itm7=Label(sec_root,text="Juice",font=("arial",15),bg=bgr,fg="yellow")
    itm7.place(relx=0.05,rely=0.43)
    itm8=Label(sec_root,text="Milk Shake",font=("arial",15),bg=bgr,fg="yellow")
    itm8.place(relx=0.05,rely=0.48)
    itm9=Label(sec_root,text="Pizza",font=("arial",15),bg=bgr,fg="yellow")
    itm9.place(relx=0.05,rely=0.53)
    itm10=Label(sec_root,text="Burger",font=("arial",15),bg=bgr,fg="yellow")
    itm10.place(relx=0.05,rely=0.58)
    itm11=Label(sec_root,text="Sandwich",font=("arial",15),bg=bgr,fg="yellow")
    itm11.place(relx=0.05,rely=0.63)
    itm12=Label(sec_root,text="Noodles",font=("arial",15),bg=bgr,fg="yellow")
    itm12.place(relx=0.05,rely=0.68)
    itm13=Label(sec_root,text="Finger Chips",font=("arial",15),bg=bgr,fg="yellow")
    itm13.place(relx=0.05,rely=0.73)
    itm14=Label(sec_root,text="Dosa",font=("arial",15),bg=bgr,fg="yellow")
    itm14.place(relx=0.05,rely=0.78)
    itm15=Label(sec_root,text="Idli",font=("arial",15),bg=bgr,fg="yellow")
    itm15.place(relx=0.05,rely=0.83)
    itm16=Label(sec_root,text="Pav Bhaji",font=("arial",15),bg=bgr,fg="yellow")
    itm16.place(relx=0.05,rely=0.88)

    price1=Label(sec_root,text="15",font=("arial",15),bg=bgr,fg="yellow")
    price1.place(relx=0.58,rely=0.13)
    price2=Label(sec_root,text="20",font=("arial",15),bg=bgr,fg="yellow")
    price2.place(relx=0.58,rely=0.18)
    price3=Label(sec_root,text="50",font=("arial",15),bg=bgr,fg="yellow")
    price3.place(relx=0.58,rely=0.23)
    price4=Label(sec_root,text="25",font=("arial",15),bg=bgr,fg="yellow")
    price4.place(relx=0.58,rely=0.28)
    price5=Label(sec_root,text="20",font=("arial",15),bg=bgr,fg="yellow")
    price5.place(relx=0.58,rely=0.33)
    price6=Label(sec_root,text="20",font=("arial",15),bg=bgr,fg="yellow")
    price6.place(relx=0.58,rely=0.38)
    price7=Label(sec_root,text="30",font=("arial",15),bg=bgr,fg="yellow")
    price7.place(relx=0.58,rely=0.43)
    price8=Label(sec_root,text="50",font=("arial",15),bg=bgr,fg="yellow")
    price8.place(relx=0.58,rely=0.48)
    price9=Label(sec_root,text="100",font=("arial",15),bg=bgr,fg="yellow")
    price9.place(relx=0.58,rely=0.53)
    price10=Label(sec_root,text="20",font=("arial",15),bg=bgr,fg="yellow")
    price10.place(relx=0.58,rely=0.58)
    price11=Label(sec_root,text="15",font=("arial",15),bg=bgr,fg="yellow")
    price11.place(relx=0.58,rely=0.63)
    price12=Label(sec_root,text="60",font=("arial",15),bg=bgr,fg="yellow")
    price12.place(relx=0.58,rely=0.68)
    price13=Label(sec_root,text="80",font=("arial",15),bg=bgr,fg="yellow")
    price13.place(relx=0.58,rely=0.73)
    price14=Label(sec_root,text="70",font=("arial",15),bg=bgr,fg="yellow")
    price14.place(relx=0.58,rely=0.78)
    price15=Label(sec_root,text="70",font=("arial",15),bg=bgr,fg="yellow")
    price15.place(relx=0.58,rely=0.83)
    price16=Label(sec_root,text="90",font=("arial",15),bg=bgr,fg="yellow")
    price16.place(relx=0.58,rely=0.88)

    note=Label(sec_root,text=" * Special Discount for Bill more than ₹1500/- * ",font=("arial",10),bg=bgr,fg="white")
    note.place(relx=0.03,rely=0.960)

    sec_root.mainloop()

def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

def clear():
    global operator
    operator =''
    tex.set(operator)

def equal():
    global qq
    try:
        q = eval(calc_entry.get())
        tex.set(q)
        qq=tex.set(q)
    except:
        messagebox.showinfo('Notification','Enter valid input')

def reset():
    foode1.delete(0,END)
    foode2.delete(0,END)
    foode3.delete(0,END)
    foode4.delete(0,END)
    foode5.delete(0,END)
    foode6.delete(0,END)
    foode7.delete(0,END)
    foode8.delete(0,END)
    foode9.delete(0,END)
    foode10.delete(0,END)
    foode11.delete(0,END)
    foode12.delete(0,END)
    foode13.delete(0,END)
    foode14.delete(0,END)
    foode15.delete(0,END)
    foode16.delete(0,END)
    tote.delete(0,END)
    sub_te.delete(0,END)
    dis_e.delete(0,END)

def total():
    tote.delete(0,END)
    sub_te.delete(0,END)
    dis_e.delete(0,END)
    if foode1.get()>str(0):
        f1ans=int(f1)*int(foode1.get())
    else:
        f1ans=int(0)

    if foode2.get()>str(0):
        f2ans=int(f2)*int(foode2.get())
    else:
        f2ans=int(0)

    if foode3.get()>str(0):
        f3ans=int(f3)*int(foode3.get())
    else:
        f3ans=int(0)

    if foode4.get()>str(0):
        f4ans=int(f4)*int(foode4.get())
    else:
        f4ans=int(0)

    if foode5.get()>str(0):
        f5ans=int(f5)*int(foode5.get())
    else:
        f5ans=int(0)

    if foode6.get()>str(0):
        f6ans=int(f6)*int(foode6.get())
    else:
        f6ans=int(0)

    if foode7.get()>str(0):
        f7ans=int(f7)*int(foode7.get())
    else:
        f7ans=int(0)

    if foode8.get()>str(0):
        f8ans=int(f8)*int(foode8.get())
    else:
        f8ans=int(0)

    if foode9.get()>str(0):
        f9ans=int(f9)*int(foode9.get())
    else:
        f9ans=int(0)

    if foode10.get()>str(0):
        f10ans=int(f10)*int(foode10.get())
    else:
        f10ans=int(0)

    if foode11.get()>str(0):
        f11ans=int(f11)*int(foode11.get())
    else:
        f11ans=int(0)

    if foode12.get()>str(0):
        f12ans=int(f12)*int(foode12.get())
    else:
        f12ans=int(0)

    if foode13.get()>str(0):
        f13ans=int(f13)*int(foode13.get())
    else:
        f13ans=int(0)

    if foode14.get()>str(0):
        f14ans=int(f14)*int(foode14.get())
    else:
        f14ans=int(0)

    if foode15.get()>str(0):
        f15ans=int(f15)*int(foode15.get())
    else:
        f15ans=int(0)

    if foode16.get()>str(0):
        f16ans=int(f16)*int(foode16.get())
    else:
        f16ans=int(0)

    sum = float(f1ans+f2ans+f3ans+f4ans+f5ans+f6ans+f7ans+f8ans+f9ans+f10ans+f11ans+f12ans+f13ans+f14ans+f15ans+f16ans+5.2+10)
    ans = "₹ "+ str(sum)

    if int(sum)>=1500:
        dis_e.insert(0,"5%")
        discounted_price = int(sum)*5/100
        ans1 = float(sum)-discounted_price
        ans1=int(ans1)
        final_ans = "₹ "+ str(ans1)
        sub_te.insert(0,ans)
        tote.insert(0,final_ans)
    else:
        sub_te.insert(0,ans)
        tote.insert(0,ans)

# ------Main heading------
n_label=Label(root,text="Restaurant Counter",font=font1,bg=bgc,fg="blue")
n_label.place(relx=0.3,rely=0.01 ,width=650,height=50)

# ------Food label---------
food1 = Label(root,text="Cold Drink:",font=font2,bg=bgc,fg="black")
food1.place(relx=0.09,rely=0.25)
food2 = Label(root,text="Coffee:",font=font2,bg=bgc,fg="black")
food2.place(relx=0.09,rely=0.30)
food3 = Label(root,text="Cold Coffee:",font=font2,bg=bgc,fg="black")
food3.place(relx=0.09,rely=0.35)
food4 = Label(root,text="Tea:",font=font2,bg=bgc,fg="black")
food4.place(relx=0.09,rely=0.40)
food5 = Label(root,text="Lemon Tea:",font=font2,bg=bgc,fg="black")
food5.place(relx=0.09,rely=0.45)
food6 = Label(root,text="Coke:",font=font2,bg=bgc,fg="black")
food6.place(relx=0.09,rely=0.50)
food7 = Label(root,text="Juice:",font=font2,bg=bgc,fg="black")
food7.place(relx=0.09,rely=0.55)
food8 = Label(root,text="Milk Shake:",font=font2,bg=bgc,fg="black")
food8.place(relx=0.09,rely=0.60)
food9 = Label(root,text="Pizza:",font=font2,bg=bgc,fg="black")
food9.place(relx=0.35,rely=0.25)
food10 = Label(root,text="Burger:",font=font2,bg=bgc,fg="black")
food10.place(relx=0.35,rely=0.30)
food11 = Label(root,text="Sandwich:",font=font2,bg=bgc,fg="black")
food11.place(relx=0.35,rely=0.35)
food12 = Label(root,text="Noodles:",font=font2,bg=bgc,fg="black")
food12.place(relx=0.35,rely=0.40)
food13 = Label(root,text="Finger chips:",font=font2,bg=bgc,fg="black")
food13.place(relx=0.35,rely=0.45)
food14 = Label(root,text="Dosa:",font=font2,bg=bgc,fg="black")
food14.place(relx=0.35,rely=0.50)
food15 = Label(root,text="Idli:",font=font2,bg=bgc,fg="black")
food15.place(relx=0.35,rely=0.55)
food16 = Label(root,text="Pav Bhaji:",font=font2,bg=bgc,fg="black")
food16.place(relx=0.35,rely=0.60)

# ---------Food entry------------
ent_qu = Label(root,text="Enter Quantity",bg=bgc,font=font2)
ent_qu.place(relx=0.19,rely=0.212)
ent_qu1 = Label(root,text="Enter Quantity",bg=bgc,font=font2)
ent_qu1.place(relx=0.45,rely=0.212)

foode1 = Entry(root,textvariable="f1",font="bold")
foode1.place(relx=0.19,rely=0.255,width=150,height=20)
foode2 = Entry(root,textvariable="f2",font="bold")
foode2.place(relx=0.19,rely=0.305,width=150,height=20)
foode3 = Entry(root,textvariable="f3",font="bold")
foode3.place(relx=0.19,rely=0.355,width=150,height=20)
foode4 = Entry(root,textvariable="f4",font="bold")
foode4.place(relx=0.19,rely=0.405,width=150,height=20)
foode5 = Entry(root,textvariable="f5",font="bold")
foode5.place(relx=0.19,rely=0.455,width=150,height=20)
foode6 = Entry(root,textvariable="f6",font="bold")
foode6.place(relx=0.19,rely=0.505,width=150,height=20)
foode7 = Entry(root,textvariable="f7",font="bold")
foode7.place(relx=0.19,rely=0.555,width=150,height=20)
foode8 = Entry(root,textvariable="f8",font="bold")
foode8.place(relx=0.19,rely=0.605,width=150,height=20)
foode9 = Entry(root,textvariable="f9",font="bold")
foode9.place(relx=0.45,rely=0.255,width=150,height=20)
foode10 = Entry(root,textvariable="f10",font="bold")
foode10.place(relx=0.45,rely=0.305,width=150,height=20)
foode11 = Entry(root,textvariable="f11",font="bold")
foode11.place(relx=0.45,rely=0.355,width=150,height=20)
foode12 = Entry(root,textvariable="f12",font="bold")
foode12.place(relx=0.45,rely=0.405,width=150,height=20)
foode13 = Entry(root,textvariable="f13",font="bold")
foode13.place(relx=0.45,rely=0.455,width=150,height=20)
foode14 = Entry(root,textvariable="f14",font="bold")
foode14.place(relx=0.45,rely=0.505,width=150,height=20)
foode15 = Entry(root,textvariable="f15",font="bold")
foode15.place(relx=0.45,rely=0.555,width=150,height=20)
foode16 = Entry(root,textvariable="f16",font="bold")
foode16.place(relx=0.45,rely=0.605,width=150,height=20)

# -----Charges------
tax = Label(root,text="Tax:",font=font2,bg=bgc,fg="black")
tax.place(relx=0.580,rely=0.45)
charges = Label(root,text="Charges:",font=font2,bg=bgc,fg="black")
charges.place(relx=0.580,rely=0.50)
dis = Label(root,text="Discount:",font=font2,bg=bgc,fg="black")
dis.place(relx=0.580,rely=0.55)
sub_t = Label(root,text="Sub Total:",font=font2,bg=bgc,fg="black")
sub_t.place(relx=0.580,rely=0.60)


tax_e = Entry(root,textvariable="t",font="bold",justify="right")
tax_e.insert(0,"₹ 5.2")
tax_e.place(relx=0.655,rely=0.45,width=100,height=20)

charges_e = Entry(root,textvariable="c",font="bold",justify="right")
charges_e.insert(0,"₹ 10")
charges_e.place(relx=0.655,rely=0.50,width=100,height=20)

dis_e = Entry(root,textvariable="d",font="bold",justify="right")
dis_e.place(relx=0.655,rely=0.55,width=100,height=20)

sub_te= Entry(root,textvariable="st",font="bold",justify="right")
sub_te.place(relx=0.655,rely=0.60,width=100,height=20)

# ------Final Button-----

price_list=Button(root,text="Price List",font=("arial",13),border="1",fg="white",bg="#002fff",command=lst)
price_list.place(relx=0.09,rely=0.75,relwidth=0.09)

rst=Button(root,text="Reset",font=("arial",13),border="1",fg="white",bg="#002fff",command=reset)
rst.place(relx=0.19,rely=0.75,relwidth=0.09)

close=Button(root,text="Close",font=("arial",13),border="1",fg="white",bg="#002fff",command=root.destroy)
close.place(relx=0.39,rely=0.75,relwidth=0.09)
close.bind('<Enter>', on_enter)
close.bind('<Leave>', on_leave)

# -----Total------
tot = Label(root,text="Total :",font=("century",22,"bold"),bg=bgc,fg="blue")
tot.place(relx=0.500,rely=0.668)

tote = Entry(root,font=("century",16,"bold"),fg="red",justify="right")
tote.place(relx=0.580,rely=0.672,height=35,width=190)

cal=Button(root,text="Calculate",font=("arial",13),border="1",fg="white",bg="#002fff",command=total)
cal.place(relx=0.29,rely=0.75,relwidth=0.09)



# -----Calc--------
tex=StringVar()
operator=''
calc_entry = Entry(root,font=("arial",16),textvariable=tex)
calc_entry.place(relx=0.750,rely=0.25,relwidth=0.20,relheight=0.050)

but7=Button(root,text="7", font=font3, border="1",fg="#28007d",command=lambda:click(7))
but7.place(relx=0.750,rely=0.310,height=50,width=60)
but8=Button(root,text="8", font=font3, border="1",fg="#28007d",command=lambda:click(8))
but8.place(relx=0.800,rely=0.310,height=50,width=60)
but9=Button(root,text="9", font=font3, border="1",fg="#28007d",command=lambda:click(9))
but9.place(relx=0.850,rely=0.310,height=50,width=60)
but_plus=Button(root,text="+", font=font3, border="1",fg="#28007d",command=lambda:click('+'))
but_plus.place(relx=0.905,rely=0.310,height=50,width=60)

but4=Button(root,text="4", font=font3, border="1",fg="#28007d",command=lambda:click(4))
but4.place(relx=0.750,rely=0.390,height=50,width=60)
but5=Button(root,text="5", font=font3, border="1",fg="#28007d",command=lambda:click(5))
but5.place(relx=0.800,rely=0.390,height=50,width=60)
but6=Button(root,text="6", font=font3, border="1",fg="#28007d",command=lambda:click(6))
but6.place(relx=0.850,rely=0.390,height=50,width=60)
but_minus=Button(root,text="-", font=font3, border="1",fg="#28007d",command=lambda:click('-'))
but_minus.place(relx=0.905,rely=0.390,height=50,width=60)

but1=Button(root,text="1", font=font3, border="1",fg="#28007d",command=lambda:click(1))
but1.place(relx=0.750,rely=0.470,height=50,width=60)
but2=Button(root,text="2", font=font3, border="1",fg="#28007d",command=lambda:click(2))
but2.place(relx=0.800,rely=0.470,height=50,width=60)
but3=Button(root,text="3", font=font3, border="1",fg="#28007d",command=lambda:click(3))
but3.place(relx=0.850,rely=0.470,height=50,width=60)
but_mul=Button(root,text="*", font=font3, border="1",fg="#28007d",command=lambda:click('*'))
but_mul.place(relx=0.905,rely=0.470,height=50,width=60)

but0=Button(root,text="0", font=font3, border="1",fg="#28007d",command=lambda:click(0))
but0.place(relx=0.750,rely=0.550,height=50,width=125)
but_clr=Button(root,text="C", font=font3, border="1",fg="#28007d",command=clear)
but_clr.place(relx=0.850,rely=0.550,height=50,width=60)
but_div=Button(root,text="/", font=font3, border="1",fg="#28007d",command=lambda:click('/'))
but_div.place(relx=0.905,rely=0.550,height=50,width=60)

but_eq=Button(root,text="=", font=font3, border="1",fg="#28007d",command=equal)
but_eq.place(relx=0.750,rely=0.630,height=35,width=267)


root.mainloop()