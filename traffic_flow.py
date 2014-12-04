import numpy as np 
import matplotlib.pyplot as plt 

# linear convection function

def F(rho,switch):
    if switch==1:
        Vmax=80.
        rhomax=250.
        f=Vmax*rho*(1-(rho/rhomax))
    elif switch==2:
        Vmax=136.
        rhomax=250.
        f=Vmax*rho*(1-(rho/rhomax))
    return f

def traffic_flow(nx,nt,switch):
    
	# IC
	L=11.
        dt=0.001
	x = np.linspace(0,L,nx)
	dx=x[1]-x[0]
        v=np.ones(nx)*0.0
        vn=np.ones(nx)*0.0
        r = np.ones(nx)*10
        r[10:20] = 50
        if(switch==1):
            ro=10.0
        elif(switch==2):
            ro=20.0
        
        r[0] = ro

	for i in range(nt):
	    rn = r.copy()
	    for j in range(1,nx):
		  r[j] = rn[j] - dt/dx*(F(rn[j],switch) - F(rn[j-1],switch))
            r[0]=ro
        for j in range(nx):
            v[j]=F(r[j],switch)/r[j]
        for j in range(nx):
            vn[j]=F(rn[j],switch)/rn[j]
        
	plt.figure
	plt.plot(x,v)
	plt.show()
	
	return r,v,rn,vn

# Part A
# Minimum velcoity at t=0
r,v,rn,vn=traffic_flow(51,1,1)

print "Part A, Q1:",min(vn)*5/18

# Average velocity at t=3 mins
r,v,rn,vn=traffic_flow(51,50,1)

print "Part A, Q2:",(sum(v)/51)*5/18

# Minimum velocity at t=6 mins
r,v,rn,vn=traffic_flow(51,100,1)

print "Part A, Q3:",min(v)*5/18

# Part B
# Minimum velcoity at t=0
r,v,rn,vn=traffic_flow(51,1,2)

print "Part B, Q1:",min(vn)*5/18

# Average velocity at t=3 mins
r,v,rn,vn=traffic_flow(51,50,2)

print "Part B, Q2:",(sum(v)/51)*5/18

# Minimum velocity at t=6 mins
r,v,rn,vn=traffic_flow(51,50,2)

print "Part B, Q3:",min(v)*5/18
