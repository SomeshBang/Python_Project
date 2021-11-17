from tkinter import *
from tkinter import messagebox
import math
import operator

screen=Tk()
screen.title("Smart Calculator")
screen.configure(bg='#00BDFF')
screen.iconbitmap('N:\\Vscode\\PythonProgram\\Tkinter\\Calculator Using Tkinter\\calc.ico') 
screen.maxsize(width='343',height='380')
screen.minsize(width='254',height='380')
screen.geometry('250x355')

def trying():
    q=eval(entry1.get())
    tex.set(q)


# basic function ---------------- 
def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

    
def clear():
    global operator
    operator =''
    tex.set(operator)

def equal():
    ''' global operator
        result = eval(operator)
        #{ eval } calculate full given string in once (eg={1+2+5-4 = 4})
        operator = str(result)
        tex.set(result)
    '''
    try:
        q = eval(entry1.get())
        tex.set(q)
    except:
        messagebox.showinfo('Notification','Enter valid input')  

def cnsin():
    try:
        global operator
        result = math.sin(eval(tex.get()))  
        operator = str(operator)
        tex.set(result)
    except:
        messagebox.showinfo('Notification','Enter valid input')    

def cncos():
    try:
        global operator
        result = math.cos(eval(tex.get()))  
        operator = str(operator)
        tex.set(result)
    except:
        messagebox.showinfo('Notification', 'Enter valid input')


def cntan():
    try:
        global operator
        result = math.tan(eval(tex.get()))
        operator = str(operator)
        tex.set(result)
    except:
        messagebox.showinfo('Notification', 'Enter valid input')

def cnsqrt():
    try:
        global operator
        result = math.sqrt(eval(tex.get()))  
        operator = str(operator)
        tex.set(result)
    except:
        messagebox.showinfo('Notification', 'Enter valid input')

def cnlog():
    try:
        global operator
        result = math.log(eval(tex.get()))  
        operator = str(operator)
        tex.set(result)
    except:
        messagebox.showinfo('Notification', 'Enter valid input')


#Binding function for all keys ----------------
def on_enter1(z):
    btn1.configure(bg='#F00000',fg='white')
def on_leave1(z):
    btn1.configure(bg='yellow',fg='black')
def on_enter2(z):
    btn2.configure(bg='#F00000',fg='white')
def on_leave2(z):
    btn2.configure(bg='yellow',fg='black')
def on_enter3(z):
    btn3.configure(bg='#F00000',fg='white')
def on_leave3(z):
    btn3.configure(bg='yellow',fg='black')
def on_enter4(z):
    btn4.configure(bg='#F00000',fg='white')
def on_leave4(z):
    btn4.configure(bg='yellow',fg='black')
def on_enter5(z):
    btn5.configure(bg='#F00000',fg='white')
def on_leave5(z):
    btn5.configure(bg='yellow',fg='black')
def on_enter6(z):
    btn6.configure(bg='#F00000',fg='white')
def on_leave6(z):
    btn6.configure(bg='yellow',fg='black')
def on_enter7(z):
    btn7.configure(bg='#F00000',fg='white')
def on_leave7(z):
    btn7.configure(bg='yellow',fg='black')
def on_enter8(z):
    btn8.configure(bg='#F00000',fg='white')
def on_leave8(z):
    btn8.configure(bg='yellow',fg='black')
def on_enter9(z):
    btn9.configure(bg='#F00000',fg='white')
def on_leave9(z):
    btn9.configure(bg='yellow',fg='black')
def on_enter0(z):
    btn0.configure(bg='#F00000',fg='white')
def on_leave0(z):
    btn0.configure(bg='yellow',fg='black')
def on_enterclear(z):
    btnclear.configure(bg='#F00000',fg='white')
def on_leaveclear(z):
    btnclear.configure(bg='yellow',fg='black')
def on_enteradd(z):
    btnadd.configure(bg='#F00000',fg='white')
def on_leaveadd(z):
    btnadd.configure(bg='yellow',fg='black')
def on_entersub(z):
    btnsub.configure(bg='#F00000',fg='white')
def on_leavesub(z):
    btnsub.configure(bg='yellow',fg='black')
def on_entermul(z):
    btnmul.configure(bg='#F00000',fg='white')
def on_leavemul(z):
    btnmul.configure(bg='yellow',fg='black')
def on_enterdiv(z):
    btndiv.configure(bg='#F00000',fg='white')
def on_leavediv(z):
    btndiv.configure(bg='yellow',fg='black')
def on_enterequal(z):
    btnequal.configure(bg='#F00000',fg='white')
def on_leaveequal(z):
    btnequal.configure(bg='yellow',fg='black')
def on_entersin(z):
    btnsin.configure(bg='#F00000',fg='white')
def on_leavesin(z):
    btnsin.configure(bg='yellow',fg='black')
def on_entercos(z):
    btncos.configure(bg='#F00000',fg='white')
def on_leavecos(z):
    btncos.configure(bg='yellow',fg='black')    
def on_entertan(z):
    btntan.configure(bg='#F00000',fg='white')
def on_leavetan(z):
    btntan.configure(bg='yellow',fg='black')
def on_enterlog(z):
    btnlog.configure(bg='#F00000',fg='white')
def on_leavelog(z):
    btnlog.configure(bg='yellow',fg='black')
def on_enterSqrt(z):
    btnSqrt.configure(bg='#F00000',fg='white')
def on_leaveSqrt(z):
    btnSqrt.configure(bg='yellow',fg='black')  

#Main Program-------------------------

tex=StringVar()
operator=''

entry1=Entry(screen,bg='grey',fg='white',font=('arial',15,'bold'),bd=12,justify='right',textvariable=tex)
entry1.grid(row=0, columnspan=4)

btn7=Button(screen,text="7",font=('arial',15,'bold'),bg='yellow',bd=5,padx=15,pady=15,command=lambda:click(7),activebackground='blue',activeforeground='white')
btn7.grid(row=1,column=0)

btn8 = Button(screen, text="8",font=('arial',15,'bold'),bg='yellow',bd=5,padx=15,pady=15,command=lambda:click(8),activebackground='blue',activeforeground='white')
btn8.grid(row=1, column=1)

btn9 = Button(screen, text="9",font=('arial',15,'bold'),bg='yellow',bd=5,padx=15,pady=15,command=lambda:click(9),activebackground='blue',activeforeground='white')
btn9.grid(row=1, column=2)

btnadd = Button(screen, text="+",font=('arial',15,'bold'),bg='yellow',bd=5,padx=15,pady=15,command=lambda:click('+'),activebackground='blue',activeforeground='white')
btnadd.grid(row=1, column=3)

btn4=Button(screen,text="4",font=('arial',15,'bold'),bg='yellow',bd=5,padx=15,pady=15,command=lambda:click(4),activebackground='blue',activeforeground='white')
btn4.grid(row=2,column=0)

btn5 = Button(screen, text="5",font=('arial',15,'bold'),bg='yellow',bd=5,padx=15,pady=15,command=lambda:click(5),activebackground='blue',activeforeground='white')
btn5.grid(row=2, column=1)

btn6 = Button(screen, text="6", font=('arial', 15, 'bold'), bg='yellow', bd=5, padx=15,pady=15, command=lambda: click(6), activebackground='blue', activeforeground='white')
btn6.grid(row=2, column=2)

btnsub = Button(screen, text="-",font=('arial',15,'bold'),bg='yellow',bd=5,padx=17,pady=15,command=lambda:click('-'),activebackground='blue',activeforeground='white')
btnsub.grid(row=2, column=3)

btn1=Button(screen,text="1",font=('arial',15,'bold'),bg='yellow',bd=5,padx=15,pady=15,command=lambda:click(1),activebackground='blue',activeforeground='white')
btn1.grid(row=3,column=0)

btn2 = Button(screen, text="2",font=('arial',15,'bold'),bg='yellow',bd=5,padx=15,pady=15,command=lambda:click(2),activebackground='blue',activeforeground='white')
btn2.grid(row=3, column=1)

btn3 = Button(screen, text="3",font=('arial',15,'bold'),bg='yellow',bd=5,padx=15,pady=15,command=lambda:click(3),activebackground='blue',activeforeground='white')
btn3.grid(row=3, column=2)

btnmul = Button(screen, text="*",font=('arial',15,'bold'),bg='yellow',bd=5,padx=16,pady=15,command=lambda:click('*'),activebackground='blue',activeforeground='white')
btnmul.grid(row=3, column=3)

btn0=Button(screen,text="0",font=('arial',15,'bold'),bg='yellow',bd=5,padx=15,pady=15,command=lambda:click(0),activebackground='blue',activeforeground='white')
btn0.grid(row=4,column=0)

btnclear = Button(screen, text="C",font=('arial',15,'bold'),bg='yellow',bd=5,padx=14,pady=15,command=clear,activebackground='blue',activeforeground='white')
btnclear.grid(row=4, column=1)

btnequal = Button(screen, text="=",font=('arial',15,'bold'),bg='yellow',bd=5,padx=14,pady=15,command=equal,activebackground='blue',activeforeground='white')
btnequal.grid(row=4, column=2)

btndiv = Button(screen, text="/",font=('arial',15,'bold'),bg='yellow',bd=5,padx=17,pady=15,command=lambda:click('/'),activebackground='blue',activeforeground='white')
btndiv.grid(row=4, column=3)

#--------------------------------------------------

btnsin=Button(screen,text="Sin",font=('arial',14,'bold'),bg='yellow',bd=5,padx=16,pady=16,command=cnsin,activebackground='blue',activeforeground='white')
btnsin.grid(row=0,column=5)

btncos=Button(screen,text="Cos",font=('arial',14,'bold'),bg='yellow',bd=5,padx=13,pady=16,command=cncos,activebackground='blue',activeforeground='white')
btncos.grid(row=1,column=5)

btntan=Button(screen,text="Tan",font=('arial',14,'bold'),bg='yellow',bd=5,padx=14,pady=15.5,command=cntan,activebackground='blue',activeforeground='white')
btntan.grid(row=2,column=5)

btnSqrt=Button(screen,text="Sq.rt",font=('arial',13,'bold'),bg='yellow',bd=5,padx=15.5,pady=17.5,command=cnsqrt,activebackground='blue',activeforeground='white')
btnSqrt.grid(row=3,column=5)

btnlog=Button(screen,text="Log",font=('arial',14,'bold'),bg='yellow',bd=5,padx=15,pady=16,command=cnlog,activebackground='blue',activeforeground='white')
btnlog.grid(row=4,column=5)


#Binding ------------------
btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)
btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)
btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)
btn4.bind('<Enter>',on_enter4)
btn4.bind('<Leave>',on_leave4)
btn5.bind('<Enter>',on_enter5)
btn5.bind('<Leave>',on_leave5)
btn6.bind('<Enter>',on_enter6)
btn6.bind('<Leave>',on_leave6)
btn7.bind('<Enter>',on_enter7)
btn7.bind('<Leave>',on_leave7)
btn8.bind('<Enter>',on_enter8)
btn8.bind('<Leave>',on_leave8)
btn9.bind('<Enter>',on_enter9)
btn9.bind('<Leave>',on_leave9)
btn0.bind('<Enter>',on_enter0)
btn0.bind('<Leave>',on_leave0)

btnadd.bind('<Enter>',on_enteradd)
btnadd.bind('<Leave>',on_leaveadd)
btnsub.bind('<Enter>',on_entersub)
btnsub.bind('<Leave>',on_leavesub)
btnmul.bind('<Enter>',on_entermul)
btnmul.bind('<Leave>',on_leavemul)
btndiv.bind('<Enter>',on_enterdiv)
btndiv.bind('<Leave>',on_leavediv)
btnclear.bind('<Enter>',on_enterclear)
btnclear.bind('<Leave>',on_leaveclear)
btnequal.bind('<Enter>',on_enterequal)
btnequal.bind('<Leave>',on_leaveequal)

btnsin.bind('<Enter>',on_entersin)
btnsin.bind('<Leave>',on_leavesin)
btncos.bind('<Enter>',on_entercos)
btncos.bind('<Leave>',on_leavecos)
btntan.bind('<Enter>',on_entertan)
btntan.bind('<Leave>',on_leavetan)
btnlog.bind('<Enter>',on_enterlog)
btnlog.bind('<Leave>',on_leavelog)
btnSqrt.bind('<Enter>',on_enterSqrt)
btnSqrt.bind('<Leave>',on_leaveSqrt)

#-----------------------

screen.mainloop()
