import numpy as np
import matplotlib.pyplot as plt
from math import *

nu=0.01
Nx=50
xd=np.linspace(0.0,1.0,Nx)
dx=xd[1]-xd[0]


x=np.zeros((Nx+2,1),dtype=float)
for i in range(Nx):
	x[i+1]=xd[i]
x[0]=x[1]-dx
x[-1]=x[-2]+dx


u=np.zeros((Nx+2,1),dtype=float)

T=20
sigma = 1.0 
dt = sigma*dx**2/nu 

Nt=int(T/dt)
t=np.linspace(0,T,Nt)

nk=0

plt.figure()
for i in range(Nt):
	
	
	un=u.copy()
	
	for j in range(1,Nx+1):
		u[j]=un[j]+((nu*dt)/(dx*dx))*(un[j+1]+un[j-1]-2*un[j])
	
	u[0]=2*20-u[1]
	u[-1]=2*10-u[-2]

#	if(Nt%30==0):
#		nk=nk+1
#		p=plt.plot(x,u,label='t=%f'%t[i])
#		#plt.xlabel('X')
		#plt.ylabel('Temeprature')

plt.plot(x,u,'.k-')
plt.xlabel('X')
plt.ylabel('Temperature')
plt.title('Temperature gradient on 1-D Grid, Boundary Conditions: 20 \
and 10 deg and time t= 30')		
plt.show()
