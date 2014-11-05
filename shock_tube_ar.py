import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


def u_initial(x):
    gamma=1.4
    n=len(x)
    
    U=np.zeros((3,n),dtype=float)

    
    ind=np.where(x<0)
    
    U[0,ind]=1
    U[0,ind[-1][-1]+1:]=0.125
    
    U[1,ind]=0.
    U[1,ind[-1][-1]+1:]=0.
    
    U[2,ind]=100000/(1.4-1)
    U[2,ind[-1][-1]+1:]=10000/(1.4-1)
    
    return U

def f(U):
    gamma=1.4
    n=len(U[0,:])
    
    F=np.zeros((3,n),dtype=float)
    
    F[0,:]=U[1,:]
    F[1,:]=(U[1,:]**2/U[0,:])+(gamma-1)*(U[2,:]-0.5*(U[1,:]**2/U[0,:]))	
    F[2,:]=(U[2,:]+(gamma-1)*(U[2,:]-0.5*(U[1,:]**2/U[0,:])))*(U[1,:]/U[0,:])
    
    return F


def maccormack(u, nt, dt, dx):
    ustar=u.copy()
    for i in range(1,2):
        un=u.copy()
        F=f(un)
        for j in range(nx-1):
            ustar[:,j+1]=0.5*(un[:,j+1]+un[:,j])-(dt/(2*dx))*(F[:,j+1]-F[:,j])
        ustar[:,0]=ustar[:,1]
        Fs=f(ustar)
        for j in range(1,nx-1):
            u[:,j]=un[:,j]-(dt/dx)*(Fs[:,j+1]-Fs[:,j-1])
        u[:,0]=u[:,1]
        u[:,-1]=u[:,-2]
    return u

    

nx= 41
dx= 20.0/(nx-1)
dt =0.001
nt=int(.1/dt)
x = np.linspace(-10.,10.,nx)

U = u_initial(x)


u=maccormack(U,nt,dt,dx)

plt.figure
plt.plot(x,u[1,:]/u[0,:],'-b.')
plt.show()

plt.figure
plt.plot(x,0.4*(u[2,:]-u[1,:]**2/u[0,:]),'-b.')
plt.show()

plt.figure
plt.plot(x,u[0,:],'-b.')
plt.show()
