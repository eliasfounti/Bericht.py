from tkinter import *
from PIL import Image, ImageTk

def ToonNaamBericht():
    berichtgemaaktFrame.pack_forget()
    NaamBerichtFrame.pack()

def ToonBerichtGemaakt():
    NaamBerichtFrame.pack_forget()
    berichtgemaaktFrame.pack()

def soortmod():
    if Naamvoer.get() == "":
        Naamvoer.get() == "anoniem"
    if Naamvoer.get().isnumeric():
        print("Geen nummers in uw naam")
    else:
        if len(Naamvoer.get()) == 1:
            print("Te korte naam")
        else:
            if berichtvoer.get() == "":
                print("Voer een bericht in")
            else:
                if len(berichtvoer.get()) > 5:
                    print("Te lange bericht")
                else:
                    ToonBerichtGemaakt()


root = Tk()

NaamBerichtFrame = Frame(master=root, background="Gold")
NaamBerichtFrame.pack(fill="both", expand=True)
naamlabel = Label(master=NaamBerichtFrame, text="Wat is uw naam?", font=("NS Sans", 12), height=1, background="Gold")
naamlabel.pack(padx=20, pady=2)
Naamvoer = Entry(master=NaamBerichtFrame, font=("", 16))
Naamvoer.pack(padx=20, pady=20)
berichtlabel = Label(master=NaamBerichtFrame, text="Wat is het bericht dat u wilt achterlaten?", font=("", 12), height=1, background="Gold")
berichtlabel.pack()
berichtvoer = Entry(master=NaamBerichtFrame, font=("", 16))
berichtvoer.pack(padx=20, pady=20)
enterknop = Button(master=NaamBerichtFrame, text='Enter', command=soortmod)
enterknop.pack(padx=20, pady=2)

berichtgemaaktFrame = Frame(master=root)
berichtgemaaktFrame.pack(fill="both", expand=True)
gemaakt = Label(master=berichtgemaaktFrame, text="Uw bericht is gemaakt! Tot ziens", font=("", 12))
gemaakt.pack()

ToonNaamBericht()
root.mainloop()