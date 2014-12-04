import numpy as np
import matplotlib.pyplot as plt
from math import *
from multiprocessing import Pool 

R_sun=695800000. #m
R_earth=6371000. #m
R_mars=3390000. #m

x_sun,y_sun=0.,0.
x_earth,y_earth=149.59787*(10**6)*(10**3),0.

dis=np.linspace(0.,pi,100)
xh=x_sun-R_sun*np.cos(dis)
yh=np.sqrt((R_sun)**2-xh**2)
yh=yh+y_sun

xh1=xh[:-1]
yh1=yh[:-1]
xs=np.concatenate([xh,xh1[::-1]])
ys=np.concatenate([yh,-yh1[::-1]])

dis=np.linspace(0.,pi,100)
xh=x_earth-R_earth*np.cos(dis)
yh=np.sqrt((R_earth)**2-(xh-x_earth)**2)
yh=yh+y_earth

xh1=xh[:-1]
yh1=yh[:-1]
xe=np.concatenate([xh,xh1[::-1]])
ye=np.concatenate([yh,-yh1[::-1]])


dis=np.linspace(0.,pi,100)
xh=x_sun-x_earth*np.cos(dis)
yh=np.sqrt((x_earth)**2-(xh-x_sun)**2)
yh=yh+y_sun

xh1=xh[:-1]
yh1=yh[:-1]
xo=np.concatenate([xh,xh1[::-1]])
yo=np.concatenate([yh,-yh1[::-1]])


plt.figure()
plt.plot(xs,ys)
plt.scatter(x_sun,y_sun)
plt.plot(xe,ye)
plt.scatter(x_earth,y_earth)
plt.plot(xo,yo)
plt.axis('equal')
plt.show()
