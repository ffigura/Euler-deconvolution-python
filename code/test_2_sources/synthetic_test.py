"""
Synthetic test 2

A Python program to compute the Synthetic test 2 
Nearby sources with remanence

This code is released from the paper: 
Reliable Euler deconvolution estimates throughout the
vertical derivatives in the sensitivity matrix

The program is under the conditions terms in the file README.txt

authors: Felipe F. Melo and Valeria C.F. Barbosa, 2019
email: felipe146@hotmail.com, valcris@on.br
"""

import numpy as np
import plot_functions as plt_fc
import euler_python as euler
import estimates_statistics as est_stats

# Input data
data_input=np.loadtxt('input/synthetic_data.dat')
shape = (60, 50)
area = [0, 12000, 0, 10000]
xi=data_input[:,0]
yi=data_input[:,1]
zi=data_input[:,2]
data=data_input[:,3]
'''
These are the two parameters of our methodology for Euler deconvolution:
window size and the percentage of solutions to keep
'''
#moving data window size
winsize=5
#percentage of the solutions that will be keep
filt=0.02
#empty arrays for multiple SIs
est_classic=[]
est_plateau=[]
'''
Euler deconvolution for multiple SIs
'''
for SI in (2,3):
    classic,plateau=euler.euler_deconv(data,xi,yi,zi,shape,area,SI,winsize,
                                       filt)
    est_classic.append(classic)            
    est_plateau.append(plateau)       
#Here finishes Euler deconvolution     
'''
Here starts the plots of figures 6 and 7.
'''
#plot Figure 6 - total field anomaly and depth estimates for SIs 2 and 3
plt_fc.plot_classic(data,est_classic,xi,yi,zi,shape)

#plot Figure 7 - depth and base level estimates for SIs 2 and 3
plt_fc.plot_plateau(data,est_plateau,xi,yi,zi,shape)


''' 
Areas used to get the statistics - Defined after the classic plot
south,northing,west,east - meters the same unit as input
'''
area_cla2=[6000,8000,5800,7000]
area_cla3=[5000,7000,3500,5000]

est_stats.classic(est_classic,area_cla2,'classic_plt2')
est_stats.classic(est_classic,area_cla3,'classic_plt3')

''' 
Plateaus used to get the statistics - Defined after the plateau plot
south,northing,west,east - meters the same unit as input
''' 
area_plt2=[6500,7800,6200,6900]
area_plt3=[5000,6400,3300,4200]

est_stats.plateau(est_plateau,xi,yi,area_plt2,'plateau_plt2')
est_stats.plateau(est_plateau,xi,yi,area_plt3,'plateau_plt3')
