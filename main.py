"""
Authors:
Adrian Martinez 
Ryan Horan

Advisor:
Ron Sarner

CS498 Capstone Project
Fall 2022

"""
# from tkinter import *

from loadWindow import tkinterScreen




def loadWindow():
    # root window
    window = tkinterScreen()
    # set window size
    window.geometry("800x400")
    # set window title
    window.title("CS 498 Capstone")
    # set window icon
    window.iconbitmap("SPLogo.ico")
  
  

    window.mainloop()
    

def main():

    loadWindow()


if __name__ == "__main__":
    main()