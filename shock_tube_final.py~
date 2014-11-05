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

def get_f(U):
    gamma=1.4
    n=len(U[0,:])
    
    F=np.zeros((3,n),dtype=float)
    
    F[0,:]=U[1,:]
    F[1,:]=(U[1,:]**2/U[0,:])+(gamma-1)*(U[2,:]-0.5*(U[1,:]**2/U[0,:]))	
    F[2,:]=(U[2,:]+(gamma-1)*(U[2,:]-0.5*(U[1,:]**2/U[0,:])))*(U[1,:]/U[0,:])
    
    return F


def solver(u, nt, dt, dx):
    ustar=u.copy()
    epsilon=0.1
    for i in range(nt):
        un=u.copy()
        F=get_f(un)
        ustar[:,:-1]=0.5*(un[:,1:]+un[:,:-1])-(dt/(2*dx))*(F[:,1:]-F[:,:-1])
	ustar[:,0]=ustar[:,1]
        Fs=get_f(ustar)
        u[:,1:-1]=epsilon*(un[:,2:]-2*un[:,1:-1]+un[:,:-2])+un[:,1:-1]-(dt/dx)*(Fs[:,1:-1]-Fs[:,:-2])
	#u[:,1:-1]=un[:,1:-1]-(dt/dx)*(Fs[:,1:-1]-Fs[:,:-2])
	u[:,0]=u[:,1]
	u[:,-1]=u[:,-2]
	#plt.figure
	#plt.plot(x,u[1,:]/u[0,:])
    return u

    

nx= 81
dx= 20.0/(nx-1)

dt=0.0002
nt=int(.01/dt)

x = np.linspace(-10.,10.,nx)

U = u_initial(x)
u=solver(U,nt,dt,dx)

plt.figure
plt.plot(x,u[1,:]/u[0,:],'-b.')
plt.show()

plt.figure
plt.plot(x,0.4*(u[2,:]-u[1,:]**2/u[0,:]),'-b.')
plt.show()

plt.figure
plt.plot(x,u[0,:],'-b.')
plt.show()

ind=np.where(x==2.5)
print u[1,ind]/u[0,ind]

print 0.4*(u[2,ind]-0.5*u[1,ind]**2/u[0,ind])

print u[0,ind]
