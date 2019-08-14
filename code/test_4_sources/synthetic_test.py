"""
Synthetic test 1

A Python program to compute the Synthetic test 1 
Distinct SIs and strong nonlinear magnetic base level 

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
shape = (120, 140)
area = [0, 24000, 0, 28000]
xi=data_input[:,0]
yi=data_input[:,1]
zi=data_input[:,2]
data=data_input[:,3]

#Plot input data - Figure 3
plt_fc.plot_input_data(data,xi,yi,zi,shape)
'''
These are the two parameters of our methodology for Euler deconvolution:
window size and the percentage of solutions to keep
'''
#moving data window size
winsize=9
#percentage of the solutions that will be keep
filt=0.08
#empty arrays for multiple SIs
est_classic=[]
est_plateau=[]
'''
Euler deconvolution for multiple SIs
'''
for SI in (0.001,1,2,3):
    classic,plateau=euler.euler_deconv(data,xi,yi,zi,shape,area,SI,winsize,
                                       filt)
    est_classic.append(classic)            
    est_plateau.append(plateau)       
#Here finishes Euler deconvolution     
'''
Here starts the plots of figures 4, 5 and 6.
'''
#plot Figure 4 - All depth and base level estimates for all SIs
plt_fc.plot_classic(data,est_classic,xi,yi,zi,shape)
#plot Figure 5 - Horizontal estimates
plt_fc.plot_plateau_xy(data,est_plateau,xi,yi,zi,shape)
#plot Figure 6 - All depth and base level estimates for all SIs
plt_fc.plot_plateau(data,est_plateau,xi,yi,zi,shape)


''' 
Areas used to get the statistics - Defined after the classic plot
south,north,west,east
''' 
area_cla0=[0.,25000,24000,28000]
area_cla1=[9200,25000,15000,20000]
area_cla2=[14000,18000,5000,10000]
area_cla3=[5000,8000,5000,8000]

est_stats.classic(est_classic,area_cla0,'classic_plt0')
est_stats.classic(est_classic,area_cla1,'classic_plt1')
est_stats.classic(est_classic,area_cla2,'classic_plt2')
est_stats.classic(est_classic,area_cla3,'classic_plt3')


''' 
Plateaus used to get the statistics - Defined after the plateau plot
south,north,west,east
''' 
area_plt0=[0.,25000,26020,26920]
area_plt1=[9200,25000,16200,17300]
area_plt2=[15000,16800,5800,8000]
area_plt3=[5900,6900,6000,7600]

est_stats.plateau(est_plateau,xi,yi,area_plt0,'plateau_plt0')
est_stats.plateau(est_plateau,xi,yi,area_plt1,'plateau_plt1')
est_stats.plateau(est_plateau,xi,yi,area_plt2,'plateau_plt2')
est_stats.plateau(est_plateau,xi,yi,area_plt3,'plateau_plt3')