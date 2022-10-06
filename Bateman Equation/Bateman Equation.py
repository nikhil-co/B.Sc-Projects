
## Importing Required Modules
import numpy as np
import math as mt
import xlrd as xl
import sympy as sy

## Initializing Constants and Dependent Parameters
e=mt.e #Euler's Number
pi=mt.pi
to=mt.pow(10,-5) # Tolerance of Newton's Method to limit our calculations


# The being Stored in a Excel Sheet at Location /Users/nikhil/Bateman/data.xls
# Using the "xlrd" module extract the data for the Population of Elements
data1=xl.open_workbook("data.xls")
dt=data1.sheet_by_index(1)

ind=range(1998) # Index
# To define the Population we the following notation - (ni)
# Where (n) is the number of nucleas and i represents the nucleas in the 
# i'th decay chain
t=dt.col_values(1,2,2002)   # Time (1500 seconds having 2000 divisions)
n0=dt.col_values(2,2,2002)  # Parent Nucleus Radon 219
n1=dt.col_values(3,2,2002)  # Polonium 215
n2=dt.col_values(4,2,2002)  # Lead 211
n3=dt.col_values(5,2,2002)  # Bismuth 211
n4=dt.col_values(6,2,2002)  # Polonium 211
n5=dt.col_values(7,2,2002)  # Lead 207

# Decay Constant for the Elements the notation is same as before 
# (integer represents the product in the nth decay chain)
l0=[]

## Finding Decay Constant Lambda0 for the Parent Nucleus (Radon-211) 
for i in ind:
    if i==0:
        l0.append(10000)
    else:
        if n0[i+1]!=0:
            l0.append((mt.log(n0[0]/n0[i+1]))/t[i])
        else:
            break
        
## Decay Constant for Parent Nucleus
D0=min(l0)            
## Finding Decay Constant Lambda1 for Polonium-211 = 1'st Product       
def L1(D1,i):
    f=(D0*n0[i]/(D1-D0))+((D0*n0[0]/(D1-D0))+n1[1])*mt.exp(-D1*t[i])-n1[i]
    d1=sy.var('d1')
    f1=(D0*n0[i]/(d1-D0))+((D0*n0[0]/(D1-D0))+n1[1])*e**(-d1*t[4])-n1[i]
    fp=sy.diff(f1,d1)
    fp=fp.subs(d1,D1)
    return(f/fp)    

## Newton's Method
x=np.zeros(1998)
x[0]=3 #Starting Point
for i1 in range(1997):
   x[i1+1]=x[i1]-L1(x[i1],i1)
   if x[i1+1]-x[i1]<=to:
       x=np.trim_zeros(x)
       break
## Decay Constant of 1'st Product   
D1=x[len(x)-1] 

## Finding Decay Constant Lambda2 for Lead-211 = 2'rd Product
def L2(D2,i):
    c=D0*D1/(D0-D1)
    f=-n2[i]+c*n0[i]/(D2-D1)+mt.exp(-D2*t[i])*(c*n0[0]/(D2-D1)+D2*n1[1]/(D2-D1))+mt.exp(-D2*t[i])*(n0[0]*(D0*D1/((D0-D2)*(D1-D2)))+n1[1]*D1/(D1-D2)+n2[1])
    d2=sy.var('d2')
    f1=-n2[i]+c*n0[i]/(d2-D1)+e**(-d2*t[i])*(c*n0[0]/(d2-D1)+d2*n1[1]/(d2-D1))+f+e**(-d2*t[i])*(n0[0]*(D0*D1/((D0-d2)*(D1-d2)))+n1[1]*D1/(D1-d2)+n2[1])
    fp=sy.diff(f1,d2)
    fp=fp.subs(d2,D2)
    return(f/fp)
y=np.zeros(1998) 
### Newton's Method
for i2 in range(1997):
   y[i2+1]=y[i2]-L2(y[i2],i2)

## Decay Constant of 2'nd Product
D2=y[len(y)-1] 

## Calculating Half life
ln=mt.log(2)
t1=ln/D0
t2=ln/D1
t3=ln/D2


print('Decay Constant for the Parent Nucleus (Radon-211) ',D0)
print('Therefore the Half Life of Radon211 ',t1)
print('Decay Constant for the 1st Daughter Nucleus (Polonium-215) ',D1)
print('Therefore the Half Life of Polonium215 ',t2)
print('Decay Constant for the Parent Nucleus (Lead-211) ',D2)
print('Therefore the Half Life of Lead211 ',t3)

















