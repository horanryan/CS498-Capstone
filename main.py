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
import osmnx as ox
import plotly.graph_objects as go
import networkx as nx


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
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  

    df = pd.read_csv('stops.csv')
    i = 0
    while i < 494:
       marker = map_widget.set_marker(df['stop_lat'][i], df['stop_lon'][i], text = df['stop_name'][i])
       i+= 1
    map_widget.pack()    


def generate_path(origin_point, target_point, perimeter):
    
    origin_lat = origin_point[0]
    origin_long = origin_point[1]

    target_lat = target_point[0]
    target_long = target_point[1]
    
    # Build the geocoordinate structure of the path's graph

    # If the origin is further from the equator than the target
    if  origin_lat > target_lat:
        north = origin_lat 
        south = target_lat
    else:
      north = target_lat
      south = origin_lat

    # If the origin is further from the prime meridian than the target
    if  origin_long > target_long:
        east = origin_long 
        west = target_long
    else:
      east = target_long
      west = origin_long
    mode = 'subway'
    graph = ox.graph_from_bbox(north+perimeter, south-perimeter, east+perimeter, west-perimeter, network_type = mode, simplify=False )
    
    origin_node = ox.get_nearest_node(graph, origin_point) 

    # Get the nearest node in the OSMNX graph for the target point
    target_node = ox.get_nearest_node(graph, target_point)
    
    # Get the optimal path via dijkstra
    route = nx.shortest_path(graph, origin_node, target_node, weight = 'length', method='dijkstra')
    
    # Create the arrays for storing the paths
    lat = []
    long = []

    for i in route:
        point = graph.nodes[i]
        long.append(point['x'])
        lat.append(point['y'])
        
    # Return the paths
    return long, lat


def main():
    loadWindow()

if __name__ == "__main__":
    main()