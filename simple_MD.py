# Program to run Molecular dyanmics for Morse oscillator
from numpy import *
from matplotlib.pyplot import *
## defining useful functions
def compute_pot(x):
    pot=4*epsilon*((sigma/x)**12-(sigma/x)**6)
    force=4*epsilon*(12*(sigma**12/(x**13))-6*(sigma**6/(x**7)))
    acc=force/mass
    return acc, pot
def evolve_by_1step(x,v,acc):
    x=x+v*dt+1/2*acc*dt*dt
    v=v+1/2*acc*dt
    acc,pot=compute_pot(x)
    v=v+1/2*acc*dt
    return x,v,acc,pot
#step-1 defining the parameters (in atomic units)
epsilon=8.71*10**(-4)
sigma=6.69
mass=145123 
dt=50
total_time=10**6
#step-2 setting initial conditions (in atomic units)
x=7
v=0
current_time=0
acc,pot=compute_pot(x)
#step-3 Evolving
nsteps=int(total_time/dt) #number of steps 
File=open('LJcoordinates.out','w')
for i in range(nsteps):
    print(current_time,x,file=File)
    x,v,acc,pot=evolve_by_1step(x,v,acc)
    current_time=current_time+dt
File.close()

# Plotting the data
data=loadtxt('LJcoordinates.out')
plot(data[:,0],data[:,1])
xlabel("Time")
ylabel("Position")
show()
