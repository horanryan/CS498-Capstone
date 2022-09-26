import tkinter as tk
from tkinter import Frame, Grid, ttk
from traceback import FrameSummary
from typing_extensions import Self

# global font style
typeFont = ("System", 25)

class tkinterScreen(tk.Tk):
    # init function for tkinter screen
    def __init__(self, *args, **kwargs):
        # init function for class tk in tkinterScreen
        tk.Tk.__init__(self, *args, **kwargs)

        # create a container
        container = tk.Frame(Self)
        container.pack(side = "top", fill="both", expand= True)

        container.grid_rowconfigure(0, weight= 1)
        container.grid_columnconfigure(0, weight=1)

        # Initialize frames to an empty array
        self.frames = {}

        # iterate through a tuple consisting of the different page layouts
        for F in (MainMenu, Page1, Page2):
            frame = F(container, self)

            # init frame of objhect from MainMenu, Page1, Page2 respectively with a for loop
            self.frames[F] = frame

            frame.grid(row= 0, column=0, sticky="nsew")
        
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
        label.grid(row=0, column=4, padx=10, pady=10)

        # Button for Page 1
        button1 = ttk.Button(self, text="Page 1", 
                             command= lambda : controller.showFrame(Page1))

        # setting up grid for button1
        button1.grid(row = 1, column=1, padx=10, pady=10)

        # Button for Page 2
        button2 = ttk.Button(self, text="Page 2", 
                             command= lambda : controller.showFrame(Page2))

        # setting up grid for button2
        button2.grid(row=2, column=1, padx=10, pady=10)


# second window frame page 1
class Page1(tk.Frame):
    # init function for Page1
    def __init__(self, parent, controller):
        # init function for class in Page1
        tk.Frame.__init__(self, parent)



        # label for page 1
        label = ttk.Label(self, text="Page 1", font=typeFont)

        # setting up grid for label
        label.grid(row=0, column=4, padx=10, pady=10)

        # Button for Page 1
        button1 = ttk.Button(self, text="Main Menu", 
                             command= lambda : controller.showFrame(MainMenu))

        # setting up grid for button1
        button1.grid(row = 1, column=1, padx=10, pady=10)

        # Button for Page 2
        button2 = ttk.Button(self, text="Page 2", 
                             command= lambda : controller.showFrame(Page2))

        # setting up grid for button2
        button2.grid(row=2, column=1, padx=10, pady=10)

# third window frame page 2
class Page2(tk.Frame):
    # init function for Page2
    def __init__(self, parent, controller):
        # init function for class in Page2
        tk.Frame.__init__(self, parent)



        # label for page 2
        label = ttk.Label(self, text="Page 2", font=typeFont)

        # setting up grid for label
        label.grid(row=0, column=4, padx=10, pady=10)

        # Button for Page 1
        button1 = ttk.Button(self, text="Page 1", 
                             command= lambda : controller.showFrame(Page1))

        # setting up grid for button1
        button1.grid(row = 1, column=1, padx=10, pady=10)

        # Button for Page 2
        button2 = ttk.Button(self, text="Main Menu", 
                             command= lambda : controller.showFrame(MainMenu))

        # setting up grid for button2
        button2.grid(row=2, column=1, padx=10, pady=10)