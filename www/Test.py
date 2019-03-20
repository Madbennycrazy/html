from tkinter import *
from BennysKnappar2 import *

#test

root = Tk()
b = BennysKnappar(root)


#knappar
def printTest(event):
    print("Test knapp 1")

def printTest2():
    print("Test knapp 2")

#musknappar
def leftClick(event):
    print("left")

def middleClick(event):
    print("middle")

def rightClick(event):
    print("right")


#knappframes
topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#musclick
frame2 = Frame(root, width=300, height=250)
frame2.bind("<Button-1>", leftClick)
frame2.bind("<Button-3>", rightClick)
frame2.bind("<Button-2>", middleClick)
frame2.pack()

#knappar
button1 = Button(topFrame, text="Test knapp1", fg="red")
button2 = Button(bottomFrame, text="Test knapp 2", fg="green", command=printTest2)

button1.bind("<Button-1>", printTest)
button1.pack(fill=Y)
button2.pack(fill=X)

root.mainloop()
