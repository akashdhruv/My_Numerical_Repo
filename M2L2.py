import numpy as np 
import matplotlib.pyplot as plt 

# linear convection function
def linearconv(nx):
	"""
	Solves linear convection eqn
	d_t u + c d_x = 0
	- the wave speed is set at 1
	- domain in x: [0,2]
	- 20 timesteps with dt = 0.025
	- IC: hat function

	plots results

	Parameter: nx - int - number of internal grid points
	Returns: none
	"""
	# IC
	dx = 2./(nx-1)
	nt = 20
	dt = 0.025
	c = 1

	# Hat fn
	u = np.ones(nx)
	u[.5/dx : 1/dx+1] = 2

	un = np.ones(nx)

	for n in range(nt):
		un = u.copy()
		u[1:] = un[1:] - c*dt/dx*(un[1:] - un[0:-1])
		u[0] = 1.0

	plt.figure
	plt.plot(np.linspace(0,2,nx), u)
	plt.ylim(0,2.5)
	plt.show()

# using linear convection fn
# linearconv(41)

# ---------- code rewritten with the CFL condition --------

def linearconv(nx):
	"""
	solve linear convection eqn

	same as fn above with CFL condition
	- dt computed using CFL of 0.5

	Parameters: nx - int - internal grid points
	Returns: none
	"""

	# IC
	dx = 2./(nx-1)
	nt = 800
	c = 1.
	sigma = 0.005 # CFL condition

	dt = sigma*dx

	# hat fn
	x=0;
	u = np.ones(nx)
	for i in range(len(u)):
		x=x+dx
		if(x<=0.9):
			u[i]=0.0
		elif(x>0.9 and x<=1.0):
			u[i]=10*(x-0.9)
		elif(x>1 and x<=1.1):
			u[i]=10*(1.1-x)
		elif(x>1.1):
			u[i]=0

	un = np.ones(nx)
	u_ini=u.copy()


	for n in range(nt):
		un = u.copy()
		for j in range(1,nx-1):
		
			u[j] = un[j] - c*dt/(2*dx)*(u[j+1]-u[j-1])

		u[0]=u[1]
		u[nx-1]=u[-1]
	print dt*nt	
	plt.figure()
	plt.plot(np.linspace(0,3,nx), u)
	plt.plot(np.linspace(0,3,nx),u_ini,'--r')
	plt.ylim(0,2.5)
	plt.show()

# testing modified linear convection fn
linearconv(75)


