
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from datetime import date, datetime
import time
hour, minute, sec = 00, 00, 00

class Main:

    def __init__(self, root):
        self.root = root
        self.configure()
        width, height = self.get_window_size()
        self.set_window_size(width, height)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.frame1Func()

    def frame1Func(self):
        self.frame1 = Frame(self.root, width=200, height=100)
        self.frame2Func()
        self.namelbl = Label(self.frame1, text="Welcome To Admin Panel", font=('times new roman', 22),
                        fg='#FF7F50', )
        self.timelbl = Label(self.frame1, text="")
        def clock():
            hour = time.strftime("%H")
            minute = time.strftime("%M")
            sec = time.strftime("%S")
            self.timelbl.config(text=hour + ":" + minute + ":" + sec)
            self.timelbl.after(1000, clock)

        clock()
        self.namelbl.grid(column=0, row=0, columnspan=6, sticky=(N, S, E, W))
        self.timelbl.grid(column=6, row=0, sticky=(N, S, E, W))
        self.frame1.grid(column=0, row=0, columnspan=6, rowspan=6, sticky=(N, S, E, W))



    def frame2Func(self):
        self.frame2 = Frame(self.frame1, width=200, height=100)
        self.frame2_btn = Button(self.frame2, text="Go To Frame 3", command=self.frame3Func,
                                       compound=TOP, background='pink', activebackground='#FF7F50',
                                       foreground='green', font=('times new roman', 16))
        self.frame2.grid(column=0, row=1, columnspan=8, rowspan=8, sticky=(N, S, E, W))
        self.frame2_btn.grid(row=4, column=9, columnspan=3, rowspan=3, sticky=(N, S, E, W))


    def frame3Func(self):
        self.frame3 = Frame(self.frame1, width=200, height=100)
        self.frame3_btn = Button(self.frame3, text="Back To Frame 2", command=self.backtoframe2Func,
                                       compound=TOP, background='pink', activebackground='#FF7F50',
                                       foreground='green', font=('times new roman', 16))

        self.frame3.grid(column=0, row=1, columnspan=8, rowspan=8, sticky=(N, S, E, W))


        self.frame3_btn.grid(row=4, column=9, columnspan=3, rowspan=3, sticky=(N, S, E, W))


    def backtoframe2Func(self):
        self.frame2Func()

    def configure(self):
        self.root.title('Face Detection System')
        # self.root.resizable(False, False)
        self.root.configure(bg='#FF7F50', padx=20, pady=20)

    def get_window_size(self):
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        # width, height = 900, 600
        return width, height

    def set_window_size(self, width, height):
        self.root.geometry("%dx%d+0+0" % (width - 15, height - 75))


if __name__ == '__main__':
    root = Tk()
    obj = Main(root)
    root.mainloop()


