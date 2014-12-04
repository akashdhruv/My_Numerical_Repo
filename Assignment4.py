import numpy as np
import matplotlib.pyplot as plt

n = 192
Du, Dv, F, k = 0.00016, 0.00008, 0.035, 0.065 # Bacteria 1 
dh = 5./(n-1)
T = 8000
dt = .9 * dh**2 / (4*max(Du,Dv))
nt = int(T/dt)

uvinitial = np.load('C:/Users/Akash/Documents/GitHub/My_Numerical_Repo/uvinitial.npz')
U = uvinitial['U']
V = uvinitial['V']

X,Y=np.meshgrid(np.linspace(0.,5.,n),np.linspace(0.,5.,n))

plt.figure()
plt.contourf(X,Y,U.T)
plt.contour(X,Y,V.T)
plt.show()

for tstep in range(nt):
    un=U.copy()
    vn=V.copy()
    
    U[1:-1,1:-1]=un[1:-1,1:-1]+dt*(Du*(un[:-2,1:-1]+un[2:,1:-1]-2*un[1:-1,1:-1])/(dh*dh)+\
                 Du*(un[1:-1,:-2]+un[1:-1,2:]-2*un[1:-1,1:-1])/(dh*dh)+\
                 -(un[1:-1,1:-1]*vn[1:-1,1:-1]*vn[1:-1,1:-1])+F*(1-un[1:-1,1:-1]))

    V[1:-1,1:-1]=vn[1:-1,1:-1]+dt*(Dv*(vn[:-2,1:-1]+vn[2:,1:-1]-2*vn[1:-1,1:-1])/(dh*dh)+\
                 Dv*(vn[1:-1,:-2]+vn[1:-1,2:]-2*vn[1:-1,1:-1])/(dh*dh)+\
                 +un[1:-1,1:-1]*vn[1:-1,1:-1]*vn[1:-1,1:-1]-(F+k)*(vn[1:-1,1:-1]))
    
    
    U[0,:]=U[1,:]
    U[-1,:]=U[-2,:]
    U[:,0]=U[:,1]
    U[:,-1]=U[:,-2]
    
    V[0,:]=V[1,:]
    V[-1,:]=V[-2,:]
    V[:,0]=V[:,1]
    V[:,-1]=V[:,-2]
    



plt.figure()
plt.contourf(X,Y,U.T)
plt.contour(X,Y,V.T)
plt.show()
