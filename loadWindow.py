# imports needed for tkinter
import tkinter as tk
from tkinter import Grid, ttk

# global font style
typeFont = ("System", 25)

class tkinterScreen(tk.Tk):
    # init function for tkinter screen
    def __init__(self, *args, **kwargs):
        # init function for class tk in tkinterScreen
        tk.Tk.__init__(self, *args, **kwargs)

        # create a container
        container = tk.Frame(self)
        container.pack(side = "top")

        container.grid_rowconfigure(0, weight= 1)
        container.grid_columnconfigure(0, weight=1)

        # Initialize frames to an empty array
        self.frames = {}

        # iterate through a tuple consisting of the different page layouts
        for F in (MainMenu, Bronx, Manhattan, Brooklyn, Queens, StatenIsland):
            frame = F(container, self)

            # init frame of objhect from MainMenu, Page1, Page2 respectively with a for loop
            self.frames[F] = frame

            frame.grid(row= 0, column=0, sticky="NSEW")
        
        self.showFrame(MainMenu)

    # display current frame passed as parameter
    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



# first window frame main menu
class MainMenu(tk.Frame):
    # init function for main menu 
    def __init__(self, parent, controller):
        # init functon for class tk in MainMenu
        tk.Frame.__init__(self, parent)

        # label for main menu
        label = ttk.Label(self, text="Main Menu", font=typeFont)
    

        # setting up grid for label
        label.grid(row=2, column=2, sticky="NE")
        
        
        # sub label for main menu
        subLabel = ttk.Label(self, text="Choose starting borough", font=typeFont)
        subLabel.grid(row=3, column=2, padx=0, pady=10, sticky="NE")

        # Button for the bronx
        button1 = ttk.Button(self, text="Bronx", 
                             command= lambda : controller.showFrame(Bronx))

        # grid set up for Bronx button
        button1.grid(row = 7, column=1)

        # Button for manhattan
        button2 = ttk.Button(self, text="Manhattan", 
                             command= lambda : controller.showFrame(Manhattan))

        # grid set up for Manhattan button
        button2.grid(row=7, column=2)

        # Button for Brooklyn
        button3 = ttk.Button(self, text="Brooklyn",
                             command= lambda : controller.showFrame(Brooklyn))

        # grid set up for Brooklyn button
        button3.grid(row=7, column=3)

        # Button for Queens
        button4 = ttk.Button(self, text="Queens",
                             command= lambda : controller.showFrame(Queens))
        button4.grid(row=7, column=4)                             

        button5 = ttk.Button(self, text="Staten Island",
                             command= lambda : controller.showFrame(StatenIsland))    
        button5.grid(row=7, column=5)

# second window frame Bronx
class Bronx(tk.Frame):
    # init function for Page1
    def __init__(self, parent, controller):
        # init function for class in Page1
        tk.Frame.__init__(self, parent)



        # label for page 1
        label = ttk.Label(self, text="Bronx", font=typeFont)

        # setting up grid for label
        label.grid(row=0, column=4, padx=10, pady=10)

        # Button for Page 1
        button1 = ttk.Button(self, text="Main Menu", 
                             command= lambda : controller.showFrame(MainMenu))

        # setting up grid for button1
        button1.grid(row = 1, column=1, padx=10, pady=10)

        # Button for Page 2
        button2 = ttk.Button(self, text="Manhattan", 
                             command= lambda : controller.showFrame(Manhattan))

        # setting up grid for button2
        button2.grid(row=2, column=1, padx=10, pady=10)

# third window frame Manhattan
class Manhattan(tk.Frame):
    # init function for Manhattan
    def __init__(self, parent, controller):
        # init function for class in Manhattan
        tk.Frame.__init__(self, parent)

        # label for manhattan
        label = ttk.Label(self, text="Manhattan", font=typeFont)

        # setting up grid for label
        label.grid(row=0, column=4, padx=10, pady=10)
        
        # Button for main menu
        button2 = ttk.Button(self, text="Main Menu", 
                             command= lambda : controller.showFrame(MainMenu))

        # setting up grid for button2
        button2.grid(row = 1, column=1, padx=10, pady=10)

        # Button for Bronx
        button1 = ttk.Button(self, text="Bronx", 
                             command= lambda : controller.showFrame(Bronx))

        # setting up grid for bronx
        button1.grid(row=2, column=1, padx=10, pady=10)

# fourth window frame Brooklyn 
class Brooklyn(tk.Frame):
    # init function for Brooklyn
    def __init__(self, parent, controller):
        # init function for class in Brooklyn
        tk.Frame.__init__(self, parent)

        # label for manhattan
        label = ttk.Label(self, text="BrookLyn", font=typeFont)

        # setting up grid for label
        label.grid(row=0, column=4, padx=10, pady=10)
        
        # Button for main menu
        button2 = ttk.Button(self, text="Main Menu", 
                             command= lambda : controller.showFrame(MainMenu))

        # setting up grid for button2
        button2.grid(row = 1, column=1, padx=10, pady=10)

        # Button for Bronx
        button1 = ttk.Button(self, text="Bronx", 
                             command= lambda : controller.showFrame(Bronx))

        # setting up grid for bronx
        button1.grid(row=2, column=1, padx=10, pady=10)


class Queens(tk.Frame):
    # init function for Queens
    def __init__(self, parent, controller):
        # init function for class in queens
        tk.Frame.__init__(self, parent)

        # label for queens
        label = ttk.Label(self, text="Queens", font=typeFont)

        # setting up grid for label
        label.grid(row=0, column=4,padx=0,pady=0)

        # Button for main menu
        button2 = ttk.Button(self, text="Main Menu", 
                             command= lambda : controller.showFrame(MainMenu))

        # setting up grid for button2
        button2.grid(row = 1, column=1, padx=10, pady=10)

        # Button for Bronx
        button1 = ttk.Button(self, text="Bronx", 
                             command= lambda : controller.showFrame(Bronx))

        # setting up grid for bronx
        button1.grid(row=2, column=1, padx=10, pady=10)
    
class StatenIsland(tk.Frame):
    # init function for Queens
    def __init__(self, parent, controller):
        # init function for class in queens
        tk.Frame.__init__(self, parent)

        # label for queens
        label = ttk.Label(self, text="Staten Island", font=typeFont)

        # setting up grid for label
        label.grid(row=0, column=4,padx=0,pady=0)

        # Button for main menu
        button2 = ttk.Button(self, text="Main Menu", 
                             command= lambda : controller.showFrame(MainMenu))

        # setting up grid for button2
        button2.grid(row = 1, column=1, padx=10, pady=10)

        # Button for Bronx
        button1 = ttk.Button(self, text="Bronx", 
                             command= lambda : controller.showFrame(Bronx))

        # setting up grid for bronx
        button1.grid(row=2, column=1, padx=10, pady=10)
        