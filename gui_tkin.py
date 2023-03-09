import serial
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

#port = 'COM6'
#bluetooth = serial.Serial(port,9600)

class App:
    def __init__(self, root):
        #setting title
        root.title("Hockey_GUI_Lite")
        #setting window size
        width=300
        height=241
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        global stat
        GCheckBox_541=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_541["font"] = ft
        stat = tk.StringVar()
        GCheckBox_541["variable"] = stat
        stat.set("0")
        GCheckBox_541["fg"] = "#333333"
        GCheckBox_541["justify"] = "center"
        GCheckBox_541["text"] = "intelligent mode"
        GCheckBox_541.place(x=160,y=10,width=138,height=30)
        GCheckBox_541["offvalue"] = "Manual mode"
        GCheckBox_541["onvalue"] = "intelligent mode"
        GCheckBox_541["command"] = self.GCheckBox_541_command

        GButton_571=tk.Button(root)
        GButton_571["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_571["font"] = ft
        GButton_571["fg"] = "#000000"
        GButton_571["justify"] = "center"
        GButton_571["text"] = "forward"
        GButton_571.place(x=50,y=50,width=197,height=30)
        GButton_571["command"] = self.GButton_571_command

        GButton_900=tk.Button(root)
        GButton_900["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_900["font"] = ft
        GButton_900["fg"] = "#000000"
        GButton_900["justify"] = "center"
        GButton_900["text"] = "backward"
        GButton_900.place(x=50,y=90,width=198,height=30)
        GButton_900["command"] = self.GButton_900_command

        GButton_649=tk.Button(root)
        GButton_649["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_649["font"] = ft
        GButton_649["fg"] = "#000000"
        GButton_649["justify"] = "center"
        GButton_649["text"] = "left"
        GButton_649.place(x=50,y=130,width=199,height=30)
        GButton_649["command"] = self.GButton_649_command

        GButton_216=tk.Button(root)
        GButton_216["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_216["font"] = ft
        GButton_216["fg"] = "#000000"
        GButton_216["justify"] = "center"
        GButton_216["text"] = "right"
        GButton_216.place(x=50,y=170,width=200,height=30)
        GButton_216["command"] = self.GButton_216_command

        GLabel_223=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_223["font"] = ft
        GLabel_223["fg"] = "#333333"
        GLabel_223["justify"] = "center"
        GLabel_223["text"] = "Version : alpha_0.1"
        GLabel_223.place(x=0,y=210,width=116,height=30)

    def GCheckBox_541_command(self):
        print(stat.get())

    def GButton_571_command(self):
        print("forward")
        #bluetooth.write(b'a')

    def GButton_900_command(self):
        print("backward")
        #bluetooth.write(b'b')

    def GButton_649_command(self):
        print("turn left")
        #bluetooth.write(b'c')

    def GButton_216_command(self):
        print("turn right")
        #bluetooth.write(b'd')

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
