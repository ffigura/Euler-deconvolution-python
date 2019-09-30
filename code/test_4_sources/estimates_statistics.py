"""
Estimates statistics

A Python program to compute the mean of the northing, easting and 
depth estimates. 

The outputs are placed at the folder 'results'.
The nomenclature is 'classic_pltX.txt', where
X stands for the area corresponding to the SI plotted.

This code is released from the paper: 
Reliable Euler deconvolution estimates throughout the
vertical derivatives of the total-field anomaly

The program is under the conditions terms in the file README.txt

authors: Felipe F. Melo and Valeria C.F. Barbosa, 2019
email: felipe146@hotmail.com, valcris@on.br
"""

import numpy as np

def classic(est_classic,area_plt,SI_vet,name):
    
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
        
        meanx=(np.mean(masked[:, 0]/1000.))
        meany=(np.mean(masked[:, 1]/1000.))
        meanz=(np.mean(masked[:, 2]/1000.))        
        results.append([SI_vet[i],meanx,meany,meanz])
        
    output=np.array([(results[i]) for i in range (0,len(SI_vet))])             
    np.savetxt('results/'+str(name)+'.txt',output,fmt='%.3f',\
               header="SI, mean x, mean y, mean z",comments='')              
    return