import tkinter as tk
import pyshorteners as ps
import pyperclip as pc
frame = tk.Tk()
frame.title("URL Shortner")
frame.geometry('400x200')


def printInput():
    inp = inputtxt.get(1.0, "end-1c")

    shortener = ps.Shortener()

    x = shortener.tinyurl.short(inp)
    lbl.config(text = "Shortnend URL : "+x)
    return x
    
def copydata():
    inp = inputtxt.get(1.0, "end-1c")

    shortener = ps.Shortener()

    x = shortener.tinyurl.short(inp)
    pc.copy(x)

inputtxt = tk.Text(frame,height = 1,width = 40)

inputtxt.pack(pady=10)


printButton = tk.Button(frame,text="Create",command = printInput)
printButton.pack(pady=20)

lbl = tk.Label(frame, text = "Shortnend URL : ")
lbl.pack()

printbutton = tk.Button(frame, text="Copy",command = copydata)
printbutton.pack(pady=10)
frame.mainloop()
