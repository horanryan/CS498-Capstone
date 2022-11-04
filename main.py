"""
Authors:
Adrian Martinez 
Ryan Horan

Advisor:
Ron Sarner

CS498 Capstone Project
Fall 2022

"""
import tkinter
import tkintermapview
import pandas as pd

def loadWindow():
    root = tkinter.Tk()
    root.title("CS 498")
    root.geometry("900x700")
    root.iconbitmap("SPLOGO.ico")

    label = tkinter.LabelFrame(root)
    label.pack(pady=20)

    loadMap(label)

    root.mainloop()

def loadMap(label):
    map_widget = tkintermapview.TkinterMapView(label, width=800, height=600, corner_radius=0)
    map_widget.set_position(40.7128, -74.0060)
    map_widget.set_zoom(10)
    map_widget.pack()

    


def main():
    loadWindow()


def add_markers():
    t_stops = pd.read_csv('C:\Users\Ryan\CS498-Capstone\MTALines\stops.csv')
    
    
    
    
    



if __name__ == "__main__":
    main()