import numpy as np
import xlrd as xl
import math as m
import matplotlib.pyplot as py

# Constants
pi = m.pi
w = 180/86400 # Earth's Angular Velocity

# Time 
t = np.arange(0,410,10)


# Data

## 1st Reading
d_1 = 3.5 #diameter of the image
t_1 = 400
i_1 = np.array([18,30,75,141,227,317,417,535,682,784,903,1014,1113,1223,1321,1378,1403,1415,1420,1421,1422,1416,1419,1411,1411,1386,1350,1300,1227,1160,1080,1002,908,812,716,619,521,421,300,250,170])
i0_1 = i_1.max()
i_1_rel = i_1/i0_1

## 2nd Reading
i_2 = np.array([11,24,45,70,100,131,169,202,244,280,316,348,377,399,412,413,413,413,413,413,412,411,410,406,406,406,399,374,344,315,282,240,194,151,122,89,60,35,17,9,5])
i0_2 = i_2.max()
i_2_rel = i_2/i0_2

## 3rd Reading {Main}
wk = xl.open_workbook_xls("data.xls")
sh = wk.sheet_by_index(0)
t_2 = []
i_3 = []
for i in range(47):
    t_2.append(sh.cell_value(i+1,0))
    i_3.append(sh.cell_value(i+1,1))
i_3 =  np.array(i_3)
i0_3 = i_3.max()
i_3_rel = i_3/i0_3

## W. Van Hamme formula
th = np.arange(0,90,4.5)
the = np.cos(th*pi/180)
i_4_rel = 1-(0.648)*(1-the)-(0.207)*the*np.log10(the)

## Eddington approximation

i_5_rel = 2/5+(3/5)*the

# Plotting
py.figure(1)

py.subplot(311)
py.scatter(t,i_1_rel) # 1st data
py.title('Time vs I/I(0) ')

py.subplot(312)
py.scatter(t,i_2_rel) # 2nd data


py.subplot(313)
py.scatter(t_2,i_3_rel) # 3rd data

#py.subplot(514)
py.figure(2)
py.scatter(th,i_4_rel,marker = "_") #  W. Van Hamme formula
py.scatter(-th,i_4_rel, marker = "_")
py.scatter(th,i_5_rel, marker = "|") #  Eddington approximation
py.scatter(-th,i_5_rel,marker = "|")
py.title('Theta vs I/I(0) W. Van Hamme formula and Eddington approximation')



