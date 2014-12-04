import numpy as np
import matplotlib.pyplot as plt
from math import *

nu=0.0001
Nx=21
Ny=21
xd=np.linspace(0.0,.01,Nx)
yd=np.linspace(0.0,.01,Ny)
dx=xd[1]-xd[0]
dy=yd[1]-yd[0]

qx=0.
qy=0.

x=np.zeros((Nx,Ny),dtype=float)
y=np.zeros((Nx,Ny),dtype=float)

for i in range(Nx):
	for j in range(Ny):
		x[i][j]=xd[i]
		y[i][j]=yd[j]

u=np.zeros((Nx,Ny),dtype=float)
u=u+20

T=20
sigma = 0.06
dt = sigma*min(dx,dy)**2/nu 

Nt=int(T/dt)
t=np.linspace(0,T,Nt)

A=1+(2*nu*dt)/(dx**2)+(2*nu*dt)/(dy**2)
Ax=-(dt*nu)/(dx**2)
Ay=-(dt*nu)/(dy**2)

B=np.zeros(((Nx-2)*(Ny-2),(Nx-2)*(Ny-2)),dtype=float)

for i in range((Nx-2)*(Ny-2)):
    for j in range((Nx-2)*(Ny-2)):
        if i==j:
            B[i][j]=A
            if(i<(Nx-2)*(Ny-2)-1):
                B[i+1][j]=Ax
            if(i>0):
                B[i-1][j]=Ax
        