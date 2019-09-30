"""
Synthetic test 1

A Python program to compute the Synthetic test 1 
Distinct SIs and strong nonlinear magnetic base level 

This code is released from the paper: 
Reliable Euler deconvolution estimates throughout the
vertical derivatives of the total-field anomaly

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
#empty array for multiple SIs
est_classic=[]
#Define below the SIs to be tested
SI_vet=[0.001,1,2,3]
'''
Euler deconvolution for multiple SIs
'''
for SI in (SI_vet):
    classic=euler.euler_deconv(data,xi,yi,zi,shape,area,SI,winsize,
                                       filt)
    est_classic.append(classic)            
#Here finishes Euler deconvolution     
'''
Plot Figures 3 and 4 - All depth and base level estimates for all SIs
'''
plt_fc.plot_classic(data,est_classic,xi,yi,zi,shape)
''' 
Areas used to get the statistics - Defined after the classic plot
south,north,west,east
''' 
area_cla0=[0.,25000,24000,28000]
area_cla1=[9200,25000,15000,20000]
area_cla2=[14000,18000,5000,10000]
area_cla3=[5000,8000,5000,8000]

est_stats.classic(est_classic,area_cla0,SI_vet,'classic_plt0')
est_stats.classic(est_classic,area_cla1,SI_vet,'classic_plt1')
est_stats.classic(est_classic,area_cla2,SI_vet,'classic_plt2')
est_stats.classic(est_classic,area_cla3,SI_vet,'classic_plt3')