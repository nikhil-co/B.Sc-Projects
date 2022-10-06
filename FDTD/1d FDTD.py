import numpy as np
import matplotlib.pyplot as py
import scipy as sp
py.ion()
SIZE = 300
p = np.linspace(0,SIZE,SIZE)


t = 500             # TOTAL TIME
T = range(0,t)      # TIME DOMAIN ARRAY
imp0 = 377.0        #
epsr = np.ones(SIZE)# REALTIVE PERMITIVITY
g = 0               # TIME STATE
h = np.zeros(SIZE)  # MAGNETIC FIELD IN THE SPATIAL DOMAIN
e = np.zeros(SIZE)  # ELETRIC FIELD  IN THE SPATIAL DOMIAN

e_t = np.zeros(t)   
e_t = list(e_t)     # ELECTRIC FIELD IN TIME DOMAIN
h_t = np.zeros(t)   
h_t = list(h_t)     # MAGNETIC FIELD IN TIME DOMAIN     

  
epsr[200:250] = 3

ft  = sp.zeros(t)
ft = list(ft)

reft  = sp.zeros(t)
reft = list(ft)

fy = np.fft.fftfreq(e.size,d=.1)

for g in T:
    #h[SIZE-1] = h[SIZE-2] # ABSORBING BOUNDARY CONDITION
    for i in range(0,SIZE-1):
        h[i] = h[i] + (e[i+1] - e[i])/imp0
    h[149] -= np.exp(-(g-30)*(g-30)/100)/imp0               # CORRECTION FOR TFSF
    
    e[0] = e[1]           # ABSORBING BOUNDARY CONDITION
    e[SIZE-1] = e[SIZE-2]
    for i in range(1,SIZE-1):    
        e[i] = e[i] + (h[i] - h[i-1])*imp0/epsr[i]
    e[150] += np.exp(-(g+.5-(-.5)-30)*(g+.5-(-.5)-30)/100)  # CORRECTION FOR TFSF   
    
    #h[SIZE-1] = h[SIZE-1] + (0-e[SIZE-1])/imp0    
    #e[0] = e[0] + (h[0]-0)*imp0 
    
    #e[150] = np.exp(-(g-30.0)*(g-30.0)/100) # GAUSSIAN SOURCE
    
    e_t[g] = e.copy()
    h_t[g] = h.copy()
    
    ft[g] = np.fft.fft(e)
    reft[g] = ft[g].real
    reft[g] = reft[g]/max(reft[g])
    
         
    if g%5 == 0:  # PLOTTING AT EVERY 5 TIME STEPS
        py.figure(0)
        py.clf()

        py.subplot(211)
        py.plot(p,e)
        py.axis((0,SIZE, -2, 2))
        py.title(g)


        py.subplot(212)
        py.plot(fy,reft[g])
        py.axis((-5,5, -1, 1))
        py.title('MAGNETIC FIELD')
    
        py.pause(0.01)
    
    g = g + 1
