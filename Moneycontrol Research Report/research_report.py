import os
from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import urllib.error, urllib.parse ,urllib.request

#-------Basic Declaration--------------------
b="#0c1231"
ff = "{Georgia} 15"

#------Basic ---------------------
mainwin = Tk()
mainwin.geometry("200x100+10+10")

#--------------------------------------------------------------------------------------------------------------------
def main_win():
    broker_res = []
    br_lst = []
    stock_res = []
    st_lst = []
    root = Toplevel()
    root.geometry("1350x720+5+5")
    root.configure(bg=b)
    root.title("Research Report from Money Control")

    # =============================================================================
    #-------Define--------------------
    def show_result():
        global frame
        #-------Frame and scrolltext--------------------
        text = ScrolledText(root, state='disabled',bg=b,bd=1)
        text.place(relx=0.005,rely=0.15,width=1345,height=610)
        frame = Frame(text,bg=b)
        text.window_create('1.0', window=frame)

        p = 1
        i = 1
        fil = open("stock.txt","r")
        fil = fil.readlines()
        for lne in fil:
            lne = lne.strip()
            
            if p==1: #date
                pass
            if p==2: #company
                lab = Label(frame,text=lne+"          " ,font=("gadugi",10,"bold"),bg=b,fg="#ff00cc")
                lab.grid(row=i,column=p)
            if p==3: #broker
                lab = Label(frame,text=lne[0:21]+"      " ,font=("gadugi",10),bg=b,fg="#b46d35")
                lab.grid(row=i,column=p)
            if p==4: #buy / sell
                if lne == "BUY":
                    x="#25ff51"
                elif lne == "SELL":
                    x="red"
                else:
                    x="white"
                lab = Label(frame,text=lne+"        " ,font=("gadugi",10,"bold"),bg=b,fg=x)
                lab.grid(row=i,column=p)
            if p==5: #report price
                lab = Label(frame,text=lne+"      " ,font=("courier",10,"bold"),bg=b,fg="white")
                lab.grid(row=i,column=p) 
            if p==6: #cmp
                lab = Label(frame,text=lne+"     " ,font=("courier",10,"bold"),bg=b,fg="white")
                lab.grid(row=i,column=p)
            if p==7: #target price
                lab = Label(frame,text=lne+"       " ,font=("courier",10,"bold"),bg=b,fg="white")
                lab.grid(row=i,column=p)
            if p==8: #profit 
                lab = Label(frame,text=lne+"       " ,font=("courier",10,"bold"),bg=b,fg="white")
                lab.grid(row=i,column=p)
            if p==9: #relized return
                if lne[0]=="-":
                    xy="red"
                else:
                    xy="#25ff51"
                lab = Label(frame,text=lne+"              " ,font=("courier",10,"bold"),bg=b,fg=xy)
                lab.grid(row=i,column=p)
            if p==10: #sensex return
                if lne[0]=="-":
                    xyz="red"
                else:
                    xyz="#25ff51"
                lab = Label(frame,text=lne,font=("courier",10,"bold"),bg=b,fg=xyz)
                lab.grid(row=i,column=p)
            if p==11:
                lab = Label(frame,text=lne,font=("gadugi",10),bg=b,fg="red")
                lab.grid(row=i,column=p)
            if p==12:
                lab = Label(frame,text=lne,font=("gadugi",10),bg=b,fg="red")
                lab.grid(row=i,column=p)
            if p==13:
                lab = Label(frame,text=lne,font=("gadugi",10),bg=b,fg="red")
                lab.grid(row=i,column=p)
            if p==14:
                p=1
                i+=1

            p+=1


    def broker_filter(e):
        global b_n
        frame.destroy()

        cy = 0.16
        for i in range(31):
            clr_lb = Label(root,  text = "                                   ",font=("arial",20) ,bg = b)
            clr_lb.place(relx = 0.008,rely = cy)
            clr1_lb = Label(root,  text = "                                ",font=("arial",20) ,bg = b)
            clr1_lb.place(relx = 0.135,rely = cy)
            cy+=0.025

        broker_index = 2
        stock_index = 1
        ry = 0.17
        lst_bk = []
        x = cb_brk.get()
        try:
            for i in range(1000):
                if x == fopen[broker_index]: #checking the user input and all similiar terms
                    stock_name = fopen[stock_index]
                    if stock_name in lst_bk:
                        pass
                    else:
                        lst_bk.append(stock_name) #adding stock name to list
                    stock_index+=13
                    broker_index+=13
                else:
                    stock_index+=13
                    broker_index+=13
        except:
            pass
        
        for nm in lst_bk:
            b_n = Label(root,text=nm,bg=b,fg="white")
            b_n.place(relx=0.01,rely=ry)
            ry+=0.025

    def stock_filter(e):
        global s_n
        frame.destroy()

        cy = 0.16
        for i in range(31):
            clr_lb = Label(root,  text = "                                ",font=("arial",20) ,bg = b)
            clr_lb.place(relx = 0.008,rely = cy)
            clr1_lb = Label(root,  text = "                                                                  ",font=("arial",20) ,bg = b)
            clr1_lb.place(relx = 0.0135,rely = cy)
            cy+=0.025


        stock_index = 1
        broker_index = 2
        ry = 0.17
        lst_st = []
        y = cb_stk.get()
        try:
            for i in range(1000):
                if y == fopen[stock_index]: #checking the user input and all similiar terms
                    broker_name = fopen[broker_index]
                    if broker_name in lst_st:
                        pass
                    else:
                        lst_st.append(broker_name) #adding broker name to list
                    stock_index+=13
                    broker_index+=13
                else:
                    stock_index+=13
                    broker_index+=13
        except:
            pass

        for mn in lst_st:
            s_n = Label(root,text=mn,bg=b,fg="white")
            s_n.place(relx=0.135,rely=ry)
            ry+=0.025

    # ==========================================================================================
    if os.path.exists("stock.txt"):
        os.remove("stock.txt")  #Checking for file

    for pg in range(1,6):
        try:
            lnk="https://www.moneycontrol.com/broker-research/latestResearchReport/"+str(pg)
            url = urllib.request.urlopen(lnk) #opening url
            if pg >=2:
                fopen = open("stock.txt","a")
                fopen = fopen.writelines("\n\n\n\n")
        except:
            messagebox.showwarning("Notification","Check your internet connection and try again later !!!")

        bs = BeautifulSoup(url,"html.parser")
        tg = bs('tbody')
        for line in tg:
            lne = line.text
            fopen = open("stock.txt","a") #Writing lines to file
            f = fopen.writelines(lne.strip())
    pg=pg+1

    #--------Button-------------------
    btn = Button(root,text="Get Result...!!!",font=("georgia",14,"bold"),bd=2,bg=b,fg="gold",command=show_result)
    btn.place(relx=0.001,rely=0.005,width=300,height=45)

    #------Label---------------------
    stockname_lb =Label(root,text="Company",font=ff ,fg="#ffc202",bg=b)
    stockname_lb.place(relx=0.01,rely=0.07)

    broker_lb =Label(root,text="Broker",font=ff ,fg="#ffc202",bg=b)
    broker_lb.place(relx=0.14,rely=0.07)

    bors_lb =Label(root,text="Buy/Sell",font=ff ,fg="#ffc202",bg=b)
    bors_lb.place(relx=0.24,rely=0.07)

    prs_lb =Label(root,text="Report Price",font=ff ,fg="#ffc202",bg=b)
    prs_lb.place(relx=0.32,rely=0.07)

    cmpp_lb =Label(root,text="CMP",font=ff ,fg="#ffc202",bg=b)
    cmpp_lb.place(relx=0.42,rely=0.07)

    tgt_lb =Label(root,text="Target price",font=ff ,fg="#ffc202",bg=b)
    tgt_lb.place(relx=0.485,rely=0.07)

    pf_lb =Label(root,text="Profit %",font=ff ,fg="#ffc202",bg=b)
    pf_lb.place(relx=0.59,rely=0.07)

    rr_lb =Label(root,text="Realized Return",font=ff ,fg="#ffc202",bg=b)
    rr_lb.place(relx=0.66,rely=0.07)

    ss =Label(root,text="Sensex Return",font=ff ,fg="#ffc202",bg=b)
    ss.place(relx=0.79,rely=0.07)

    #--------Creating label for combobox(filter)---------------------
    fopen = open("stock.txt","r")
    fopen =  fopen.readlines()
    brk = 2
    try:
        for i in range(10000):
            bro = fopen[brk]
            brk = brk+13
            br_lst.append(bro)
            if bro in broker_res:
                pass
            else:
                broker_res.append(bro)
    except:
        pass

    stk = 1
    try:
        for ii in range(10000):
            sk = fopen[stk]
            stk = stk+13
            st_lst.append(sk)
            if sk in stock_res:
                pass
            else:
                stock_res.append(sk)
    except:
        pass

    # --------Combobox---------------
    cb_brk = ttk.Combobox(root)
    cb_brk["values"] = broker_res
    cb_brk["state"] = "readonly"
    cb_brk.place(relx=0.125,rely=0.113)
    cb_brk.bind('<<ComboboxSelected>>',broker_filter)


    cb_stk = ttk.Combobox(root)
    cb_stk["values"] = stock_res
    cb_stk["state"] = "readonly"
    cb_stk.place(relx=0.005,rely=0.113)
    cb_stk.bind('<<ComboboxSelected>>',stock_filter)

    #-------Finalization--------------------
    root.mainloop() 


bt = Button(mainwin,text="Research Report ....!!!",command=main_win)
bt.grid(row=0,column=0)
#--------------------------------------------------------------------------------------------------------------------

mainwin.mainloop()