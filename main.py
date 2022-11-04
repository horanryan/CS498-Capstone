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
    
    # read in all the stops for nyc subway from file
    df = pd.read_csv('stops.csv')
    i = 0 # loop control variable 
    
    # preloading all the stops as markers on the map with names
    while i < df.shape[0]:
       marker = map_widget.set_marker(df['stop_lat'][i], df['stop_lon'][i], text = df['stop_name'][i])
       i+= 1
    map_widget.pack()    


def main():
    loadWindow()

if __name__ == "__main__":
    main()