import serial
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=plt.figaspect(0.5))
ser = serial.Serial('COM12', 9600, timeout=1)

ax = fig.add_subplot(1, 1, 1, projection='3d')
time.sleep(2)
def rotasi ():
    d =[]
    #for i in range(1):
    for i in range(5):
            b = str(ser.readline(),'utf-8')
            c = (b.split("\r\n"))
            e = c[0].split(",")
            f = np.array(e)#.tolist()
            x = f.shape
            if x[0] >1:
                print(f.shape,f)
                d.append(f)
    d = pd.DataFrame(d,columns=['X','Y','Z'])
    d.to_csv('g.csv')
    d1 = pd.read_csv('g.csv')
    X = np.sin(d1['Y'])
    Y = np.cos(d1['Y'])
    #Z = np.cos(d1['Z'])
    #X = np.arange(-5, 5, 0.25)
    #Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z =R
    print(Z)
    
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

    #ax = fig.add_subplot(1, 2, 2, projection='3d')
    #ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    #fig.colorbar(surf, shrink=0.5, aspect=10)

    ''' X = d1['Y']
    Y = np.sin(d1['Z'])
    Z = np.cos(d1['Z'])
    ax.scatter(X,Y,Z,cmap='viridis')'''
    fig.canvas.flush_events()
    #ax.cla()

while True:
    rotasi()
    fig.canvas.manager.show()
 
   
  
   
   
   
    
   
   
    