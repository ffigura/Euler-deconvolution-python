"""
Estimates statistics

A Python program to compute statistics of the estimates 
on classic and plateau plots. 

The outputs are placed at the folder 'results'.
The nomenclature is 'classic' ou 'plateau' _plot X .txt, where
X stands for the area corresponding to the SI plotted.

This code is released from the paper: 
Reliable Euler deconvolution estimates throughout the
vertical derivatives in the sensitivity matrix

The program is under the conditions terms in the file README.txt

authors: Felipe F. Melo and Valeria C.F. Barbosa, 2019
email: felipe146@hotmail.com, valcris@on.br
"""

import numpy as np

def classic(est_classic,area_plt,name):
    
    results = []
    
    for i in range(len(est_classic)):
        
        estimates=np.stack((est_classic[i][:,0],est_classic[i][:,1],
                            est_classic[i][:,2],est_classic[i][:,3]),axis=-1)
        
        masked =np.ma.array(estimates,mask=np.repeat(estimates[:,0]<=
                                            area_plt[0],estimates.shape[1]))
        masked = np.ma.array(masked, mask=np.repeat(masked[:,0]>=area_plt[1],
                                                        estimates.shape[1]))
        masked = np.ma.array(masked, mask=np.repeat(masked[:,1]<=area_plt[2],
                                                        estimates.shape[1]))
        masked = np.ma.array(masked, mask=np.repeat(masked[:,1]>=area_plt[3],
                                                        estimates.shape[1]))
        
        statistics=(np.mean(masked[:, 2]/1000.),np.std(masked[:,2]/1000.), \
            np.mean(masked[:,3]),np.std(masked[:,3]))
        
        results.append(statistics)
        
    np.savetxt('results/'+str(name)+'.txt',results,fmt='%.3f',header="mean z,"\
               "std z,mean b, std b",comments='')          
    
    return

def plateau(est_plateau,xi,yi,area_plt,name):
    
    results=[]
    
    for i in range (len(est_plateau)):
        estimates=np.stack((xi,yi,est_plateau[i][:,2],est_plateau[i][:,3]),
                           axis=-1)
        
        masked =np.ma.array(estimates,mask=np.repeat(estimates[:,0]<=
                                            area_plt[0],estimates.shape[1]))
        masked = np.ma.array(masked, mask=np.repeat(masked[:,0]>=area_plt[1],
                                                        estimates.shape[1]))
        masked = np.ma.array(masked, mask=np.repeat(masked[:,1]<=area_plt[2],
                                                        estimates.shape[1]))
        masked = np.ma.array(masked, mask=np.repeat(masked[:,1]>=area_plt[3],
                                                        estimates.shape[1]))
        
        statistics=(np.mean(masked[:, 2]/1000.),np.std(masked[:,2]/1000.), \
            np.mean(masked[:,3]),np.std(masked[:,3]))
        
        results.append(statistics)
        
    np.savetxt('results/'+str(name)+'.txt',results,fmt='%.3f',header="mean z,"\
               "std z,mean b, std b",comments='')            
    
    return