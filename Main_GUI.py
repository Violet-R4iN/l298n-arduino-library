import serial
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
bluetooth = serial.Serial("COM6",9600)
class App:
    def __init__(self, root):
        #setting title
        root.title("Grand_Lighting_GUI")
        #setting window size
        width=320
        height=283
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        global stat
        GCheckBox_541 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_541["font"] = ft
        stat = tk.StringVar()
        GCheckBox_541["variable"] = stat
        stat.set("0")
        GCheckBox_541["fg"] = "#333333"
        GCheckBox_541["justify"] = "center"
        GCheckBox_541["text"] = "intelligent mode"
        GCheckBox_541.place(x=180,y=10,width=138,height=30)
        GCheckBox_541["offvalue"] = "Manual mode"
        GCheckBox_541["onvalue"] = "intelligent mode"
        GCheckBox_541["command"] = self.GCheckBox_541_command

        global GButton_571
        GButton_571 = tk.Button(root)
        GButton_571["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_571["font"] = ft
        GButton_571["fg"] = "#000000"
        GButton_571["justify"] = "center"
        GButton_571["text"] = "forward"
        GButton_571.place(x=50, y=50, width=220, height=30)
        GButton_571["state"] = "normal"
        GButton_571["command"] = self.GButton_571_command

        global GButton_900
        GButton_900 = tk.Button(root)
        GButton_900["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_900["font"] = ft
        GButton_900["fg"] = "#000000"
        GButton_900["justify"] = "center"
        GButton_900["text"] = "backward"
        GButton_900.place(x=50, y=90, width=220, height=30)
        GButton_900["command"] = self.GButton_900_command

        global GButton_649
        GButton_649 = tk.Button(root)
        GButton_649["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_649["font"] = ft
        GButton_649["fg"] = "#000000"
        GButton_649["justify"] = "center"
        GButton_649["text"] = "left"
        GButton_649.place(x=50, y=130, width=220, height=30)
        GButton_649["command"] = self.GButton_649_command

        global GButton_216
        GButton_216 = tk.Button(root)
        GButton_216["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_216["font"] = ft
        GButton_216["fg"] = "#000000"
        GButton_216["justify"] = "center"
        GButton_216["text"] = "right"
        GButton_216.place(x=50, y=170, width=220, height=30)
        GButton_216["command"] = self.GButton_216_command

        GLabel_223 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_223["font"] = ft
        GLabel_223["fg"] = "#333333"
        GLabel_223["justify"] = "center"
        GLabel_223["text"] = "Version : alpha_0.1(build by very)"
        GLabel_223.place(x=0,y=250,width=200,height=30)

        global GButton_81
        GButton_81=tk.Button(root)
        GButton_81["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_81["font"] = ft
        GButton_81["fg"] = "#cc0000"
        GButton_81["justify"] = "center"
        GButton_81["text"] = "Stop"
        GButton_81.place(x=50,y=210,width=220,height=30)
        GButton_81["command"] = self.GButton_81_command

    def GCheckBox_541_command(self):
        if stat.get() == "intelligent mode" :
            print("intelligent mode")
            bluetooth.write(b'z')
            self.ButtonLock()
        else:
            print("manual  mode")
            bluetooth.write(b'e')
            self.ButtonUnlock()

    def ButtonLock(self):
        GButton_571.config(state="disabled")
        GButton_900.config(state="disabled")
        GButton_649.config(state="disabled")
        GButton_216.config(state="disabled")
        GButton_81.config(state="disabled")

    def ButtonUnlock(self):
        GButton_571.config(state="normal")
        GButton_571.config(state="normal")
        GButton_900.config(state="normal")
        GButton_649.config(state="normal")
        GButton_216.config(state="normal")
        GButton_81.config(state="normal")

    def GButton_571_command(self):
        print("forward")
        bluetooth.write(b'a')

    def GButton_900_command(self):
        print("backward")
        bluetooth.write(b'b')

    def GButton_649_command(self):
        print("turn left")
        bluetooth.write(b'd')

    def GButton_216_command(self):
        print("turn right")
        bluetooth.write(b'c')

    def GButton_81_command(self):
        print("stop")
        bluetooth.write(b'e')
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
