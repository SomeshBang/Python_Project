from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import os

# path_file = input("Enter Folder Path : ")        #enter folder name where images are stored....
# path_file=(path_file+"/")
path_file = ("N:\\Vscode\\PythonProgram\\Images\\")
# --------Basic------------------

root = Tk()
root.title("Pictures")
root.geometry("350x350+25+25")
root.maxsize(width = "1036",height = "560")
root.minsize(width = "1036",height = "560")

#------define buttons-------------

def fenter(a):
    forw.configure(bg='#07e883',fg='black')
def fleave(a):
    forw.configure(bg='white',fg='black')
def benter(a):
    backw.configure(bg='#07e883',fg='black')
def bleave(a):
    backw.configure(bg='white',fg='black')

def on_enter(a):
    exit_button.configure(bg='#ed2f28',fg='white')
def on_leave(a):
    exit_button.configure(bg='white',fg='#ed2f28')

# --------File openning-------------

fopen = open("output.txt", "w")
for path, subdirs, files in os.walk(path_file):
    for filename in files:
        f = os.path.join(filename)
        fopen.write(str(f) + os.linesep) 

lst = []
count=0
fopen=open("output.txt")
for line in fopen:
    fname = line.strip()
    if len(fname) < 1:
        pass
    else:
        lst.append(fname)
        count+=1

# ------Define clicks forward and backward ----------

i=0
def forwclick():
    global lst
    global i 
    i=i+1
    if i==len(lst):
        messagebox.showwarning("Notification","You have reached last Image.....")
        i= i-1
    img = Image.open(path_file + lst[i])
    resize_img = img.resize((900,500))
    photo = ImageTk.PhotoImage(resize_img)
    lable_img=Label(image = photo,anchor = CENTER)
    lable_img.image = photo
    lable_img.grid(row=0,column=1 ,rowspan=3,columnspan=3)
    counting = Label(root,text="Images "+str(i+1)+" out of "+str(count),font=("times",10,"bold"),fg="#0b03fc")
    counting.grid(row=4,column=3,columnspan=5,sticky=E)


def backwclick():
    global lst
    global i 
    i=i-1
    if i < 0:
        messagebox.showwarning("Notification","No previous Image.....")
        i=i+1
        
    img = Image.open(path_file + lst[i])
    resize_img = img.resize((900,500))
    photo = ImageTk.PhotoImage(resize_img)
    lable_img=Label(image = photo,anchor = CENTER)
    lable_img.image = photo
    lable_img.grid(row=0,column=1 ,rowspan=3,columnspan=3)
    counting = Label(root,text="Images "+str(i+1)+" out of "+str(count),font=("times",10,"bold"),fg="#0b03fc")
    counting.grid(row=4,column=3,columnspan=5,sticky=E)


def click():
    fopen.close()
    if os.path.exists("output.txt"):
        exit_button=Button(root,text="Exit Button",fg="#ed2f28",font=6,bd=1,relief=SUNKEN,command = root.quit())
        exit_button.grid(row=3,column=2,pady=3)

        os.remove("output.txt")
    

# ------Initial Display--------------------

img = Image.open(path_file + lst[0])        #it open image as per default index (i.e: 0 )
resize_img = img.resize((900,500))          #it resize the image as per given size 
photo = ImageTk.PhotoImage(resize_img)
lable_img=Label(image = photo,anchor = CENTER)
lable_img.image = photo
lable_img.grid(row=0,column=1 ,rowspan=3,columnspan=3)


counting = Label(root,text="Images "+str(i+1)+" out of "+str(count),font=("times",10,"bold"),fg="#0b03fc")
counting.grid(row=4,column=3,columnspan=5,sticky=E)


# --------Buttons ---------
forw = Button(root,text = ">",padx = 15,pady=160,font=("arial",18,"bold"),command = forwclick)
forw.grid(row = 1,column = 4)
forw.bind('<Enter>',fenter)
forw.bind('<Leave>',fleave)

backw = Button(root,text = "<",padx = 15,pady=160,font=("arial",18,"bold"),command = backwclick)
backw.grid(row = 1,column = 0)
backw.bind('<Enter>',benter)
backw.bind('<Leave>',bleave)

# ------exit button------
exit_button=Button(root,text="Exit Button",fg="#ed2f28",font=6,bd=1,relief=SUNKEN,command =click)
exit_button.grid(row=3,column=2,pady=3)
exit_button.bind('<Enter>',on_enter)
exit_button.bind('<Leave>',on_leave)

# -------Final --------
root.mainloop()