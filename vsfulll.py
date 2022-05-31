import serial
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

ser = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)
while True:
    d =[]
    for i in range(120):
        b = str(ser.readline(),'utf-8')
        c = (b.split("\r\n"))
        e = c[0].split(",")
        f = np.array(e)#.tolist()
        x = f.shape
        if x[0] >1:
            print(f.shape,f)
            d.append(f)
        
        #d.append(e)
    #c.to_csv('c.csv')
    #print(np.array(d).reshape(-1,3))
    g= np.array(d)
    p = pd.DataFrame(g)
    p.columns=["x","y","z"]
    p.to_csv('g.csv')
    print(g.shape)
    z =pd.read_csv('g.csv')
    print(z["y"])
    x1= z["x"]
    z1= z["y"]
    y1= z["z"]
    print(z1)
   #xs = np.arange(0,100,1)
    #ys = np.arange(0,100,1)
    #xs,ys= np.meshgrid(xs,ys)

    
    x2 = z1* np.sin(180 * z1)
    y2 = z1 * np.cos(180* z1)
    print(z.shape)
    fig = plt.figure()
    ax = plt.axes(projection ='3d')
    #ax.plot_surface(x1, y1, z1, c=z1, cmap='viridis', linewidth=0.5)
    ax.plot_trisurf(x2, y2, y1,  cmap='viridis',)
    

    

    #ax.plot3D(x2, y2, z1, 'green')
    #ax.set_title('3D line plot geeks for geeks')
    #plt.show()
    #ax.scatter(x2 ,y2, z1, c=z1, cmap='viridis', linewidth=0.5 )
    plt.show()
  
   
  
   
   
   
    
   
   
    