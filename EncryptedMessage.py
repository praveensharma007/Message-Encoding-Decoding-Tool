from tkinter import *
from tkinter import messagebox
import base64

screen = Tk()
screen.geometry("420x420")
screen.title("Secret Message App")
screen.configure(bg="lavender")

def encrypt():
    password = code.get()
    if password=="1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x250")
        screen1.configure(bg="pink")

        message = text1.get(1.0,END)
        encodemessage = message.encode("ascii")
        base64_bytes = base64.b64encode(encodemessage)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1,text="Encryption Successful",font="impack 10 bold").place(x=5,y=6)
        text2 = Text(screen1,font="30",bd=4,wrap=WORD)
        text2.place(x=2,y=30,width=390,height=180)
        text2.insert(END,encrypt)

    elif(password==""):
        messagebox.showerror("ERROR","PLEASE ENTER SECRET KEY")
    elif(password!="1234"):
        messagebox.showerror("OOPS!","Invalid Secret Key")

def decrypt():
    password = code.get()
    if password=="1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x250")
        screen2.configure(bg="beige")

        message = text1.get(1.0,END)
        encodemessage = message.encode("ascii")
        base64_bytes = base64.b64decode(encodemessage)
        encrypt = base64_bytes.decode("ascii")

        Label(screen2,text="Decryption Successful",font="impack 10 bold").place(x=5,y=6)
        text2 = Text(screen2,font="30",bd=4,wrap=WORD)
        text2.place(x=2,y=30,width=390,height=180)
        text2.insert(END,encrypt)

    elif(password==""):
        messagebox.showerror("ERROR","PLEASE ENTER SECRET KEY")
    elif(password!="1234"):
        messagebox.showerror("OOPS!","Invalid Secret Key")

def clear():
    text1.delete(1.0,END)
    code.set("")


#label
Label(screen,text="Enter the Message",font="impack 14 bold",bg="lightyellow").place(x=5,y=6)

#text
text1 = Text(screen,font="20")
text1.place(x=5,y=45,width=410,height=120)

#label2
Label(screen,text="Enter Secret Key",font="impack 13 bold").place(x=138,y=180)

#entry
code=StringVar()
Entry(textvariable=code,bd=4,font="20",show="*").place(x=110,y=220)

#button
Button(screen,text="ENCRYPT",font="arial 15 bold",bg="lightgreen",command=encrypt).place(x=25,y=280,width=180)
Button(screen,text="DECRYPT",font="arial 15 bold",bg="lightblue",command=decrypt).place(x=220,y=280,width=180)
Button(screen,text="CLEAR",font="arial 15 bold",bg="violet",command=clear).place(x=130,y=350,width=170)


mainloop()
