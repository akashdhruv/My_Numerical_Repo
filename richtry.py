import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


def u_initial(x):
	gamma=1.4	
	n=len(x)
    
    	u1=np.linspace(0.0,0.0,n)
	u2=np.linspace(0.0,0.0,n)
	u3=np.linspace(0.0,0.0,n)

    
    	ind=np.where(x<=0)


    	u1[ind]=1
    	u1[ind[-1][-1]+1:]=0.125

	u2[ind]=0.
	u2[ind[-1][-1]+1:]=0.

	u3[ind]=100000/(1.4-1)
	u3[ind[-1][-1]+1:]=10000/(1.4-1)

    	return u1,u2,u3
def Ff1(U1,U2,U3):
	F1=U2
	return F1

def Ff2(U1,U2,U3):
	gamma=1.4
	F2=(U2**2/U1)+(gamma-1)*(U3-0.5*(U2**2/U1))	
	return F2
	

def Ff3(U1,U2,U3):
	gamma=1.4	
	F3=(U3+(gamma-1)*(U3-0.5*(U2**2/U1)))*(U2/U1)
	return F3


"""
def maccormack(u, nt, dt, dx):  
	ustar=u.copy()
    	for i in range(1,nt):

	return u
"""		
    

nx= 81
dx= 20.0/(nx-1)
sigma = .1
dt =0.002
nt=int(.01/dt)
x = np.linspace(-10.,10.,nx)

u1,u2,u3 = u_initial(x)

print nt
"""
print x
print "\n\n"
print u1
print u2
print u3
"""
fn1=np.linspace(0.0,0.0,nx)
fn2=np.linspace(0.0,0.0,nx)
fn3=np.linspace(0.0,0.0,nx)

us1=np.linspace(0.0,0.0,nx)
us2=np.linspace(0.0,0.0,nx)
us3=np.linspace(0.0,0.0,nx)

fs1=np.linspace(0.0,0.0,nx)
fs2=np.linspace(0.0,0.0,nx)
fs3=np.linspace(0.0,0.0,nx)

"""
for j in range(nx):
	f1[j]=Ff1(u1[j],u2[j],u3[j])
	f2[j]=Ff2(u1[j],u2[j],u3[j])
	f3[j]=Ff3(u1[j],u2[j],u3[j])

print "\n\n"
print f1
print f2
print f3
"""
for i in range(nt):
	un1=u1.copy()
	un2=u2.copy()
	un3=u3.copy()

	for j in range(nx):
		fn1[j]=Ff1(un1[j],un2[j],un3[j])
		fn2[j]=Ff2(un1[j],un2[j],un3[j])
		fn3[j]=Ff3(un1[j],un2[j],un3[j])
	for j in range(1,nx-1):
		u1[j]=0.5*(un1[j+1]+un1[j-1])-(dt/(2*dx))*(fn1[j+1]-fn1[j-1])
		u2[j]=0.5*(un2[j+1]+un2[j-1])-(dt/(2*dx))*(fn2[j+1]-fn2[j-1])
		u3[j]=0.5*(un3[j+1]+un3[j-1])-(dt/(2*dx))*(fn3[j+1]-fn3[j-1])
	
	
	
#	for j in range(nx):
#		fs1[j]=Ff1(us1[j],us2[j],us3[j])
#		fs2[j]=Ff2(us1[j],us2[j],us3[j])
#		fs3[j]=Ff3(us1[j],us2[j],us3[j])
#	
#	for j in range(1,nx-1):
#		u1[j]=(un1[j])-(dt/(dx))*(fs1[j+1]-fs1[j-1])
#		u2[j]=(un2[j])-(dt/(dx))*(fs2[j+1]-fs2[j-1])
#		u3[j]=(un3[j])-(dt/(dx))*(fs3[j+1]-fs3[j-1])
	


plt.figure()
plt.plot(x,u2/u1)
plt.show()

plt.figure()
plt.plot(x,u1)
plt.show()

ind=np.where(x==2.5)

print u2[ind]/u1[ind]
print u1[ind]
