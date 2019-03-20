from tkinter import *


class BennysKnappar:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=master.destroy)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("wow det funkar")
