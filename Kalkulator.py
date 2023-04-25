import tkinter
from tkinter import *

root=Tk()
root.title("Kalkulator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")

calculation = ""

def tampilkan(value):
    global calculation
    calculation += value
    label_hasil.config(text=calculation)

def hapus():
    global calculation
    calculation = ""
    label_hasil.config(text=calculation)

def samadengan():
    global calculation
    result = ""
    if calculation != "":
        try :
            result = eval(calculation)
        except :
            result = "Error"
            calculation = ""
    label_hasil.config(text=result)

label_hasil= Label(root, width=25, height=2, text="", font=("arial", 30))
label_hasil.pack()

Button(root, text="(", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan("(")).place(x=10, y=100)
Button(root, text=")", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan(")")).place(x=150, y=100)
Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan("%")).place(x=290, y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan("/")).place(x=430, y=100)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan("7")).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan("8")).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan("9")).place(x=290, y=200)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan("*")).place(x=430, y=200)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan("4")).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan("5")).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan("6")).place(x=290, y=300)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan("-")).place(x=430, y=300)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan("1")).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan("2")).place(x=150, y=400)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan("3")).place(x=290, y=400)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan("+")).place(x=430, y=400)

Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: hapus()).place(x=10, y=500)
Button(root, text="0", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan("0")).place(x=150, y=500)
Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: tampilkan(".")).place(x=290, y=500)
Button(root, text="=", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#fe9037", command=lambda: samadengan()).place(x=430, y=500)

root.mainloop()