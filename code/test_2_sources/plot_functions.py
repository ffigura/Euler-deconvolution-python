"""
Plot functions 

A Python program to plot the total-field anomaly and the estimates
on classic plot. 

This code plot the figure 5 in the folder 'figures'.

This code is released from the paper: 
Reliable Euler deconvolution estimates throughout the
vertical derivatives in the sensitivity matrix

The program is under the conditions terms in the file README.txt

authors: Felipe F. Melo and Valeria C.F. Barbosa, 2019
email: felipe146@hotmail.com, valcris@on.br
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt
import gc
import matplotlib.patches as patches

'''
For a nice plot of magnetic anomaly and b-estimates
 following Niccoli (2014)
'''
LinL = np.loadtxt('input/Linear_L_0-1.txt')

b3=LinL[:,2] # value of blue at sample n
b2=LinL[:,2] # value of blue at sample n
b1=np.linspace(0,1,len(b2)) # position of sample n - ranges from 0 to 1

# setting up columns for list
g3=LinL[:,1]
g2=LinL[:,1]
g1=np.linspace(0,1,len(g2))
r3=LinL[:,0]
r2=LinL[:,0]
r1=np.linspace(0,1,len(r2))
# creating list
R=zip(r1,r2,r3)
G=zip(g1,g2,g3)
B=zip(b1,b2,b3)
# transposing list
RGB=zip(R,G,B)
rgb=zip(*RGB)
# creating dictionary
k=['red', 'green', 'blue']
LinearL=dict(zip(k,rgb)) # makes a dictionary from 2 lists
my_cmap = mpl.colors.LinearSegmentedColormap('my_colormap',LinearL) 
#######################################################################


def plot_classic(data,est_classic,xi,yi,zi,shape):
    '''
    Plot the input data and the depth solutions of the proposed methodology 
	for SI = 2 and 3 in the Classic plot
    '''
    vet_title=["(b)","(c)","(d)","(e)"]
    
    fig=plt.figure(figsize=(11, 6))
    
    plt.subplot(2,3,1)  
    
    plt.title('(a)', fontsize = 14, loc='center',y=-0.39)
    
    rect2 = patches.Rectangle((4.050,5.850),0.4,0.4,linewidth=1,
                              edgecolor='crimson',facecolor='none',
                              linestyle='-',zorder=2)
    rect3 = patches.Rectangle((5.850,6.850),0.3,0.3,linewidth=1,
                              edgecolor='crimson',facecolor='none',
                              linestyle='-',zorder=2)
    im=plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                   data.reshape(shape), 30, cmap=my_cmap)
    ax = plt.gca()
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    cbar=fig.colorbar(im,pad=0.01,shrink=1)
    cbar.set_label('nT',labelpad=-21,y=-0.01, rotation=0,fontsize=13)
    ax.add_patch(rect2)
    ax.add_patch(rect3)
    cbar.ax.tick_params(labelsize=13)
    ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
    ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
    plt.text(8,8,'P2',color='w', size='large')
    plt.text(2,4,'P3',color='w', size='large')
    
    minz = np.min(0.)
    maxz = np.max(1.2)
    levelsz = np.linspace(minz,maxz,7)   
    
    minb = np.min(-.02)
    maxb = np.max(.02)
    levelsb = np.linspace(minb,maxb,5)   
    
       
    plt.subplot(2,3,2)  
    plt.title(vet_title[0], fontsize = 14, loc='center',y=-0.39)
    plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                   data.reshape(shape), 30, cmap='gray')
    ax = plt.gca()
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    scat=plt.scatter(est_classic[0][:,1]/1000., est_classic[0][:,0]/1000.,
                     s=50,c=(est_classic[0][:,2]/1000.), cmap='terrain_r',
                     vmin=minz, vmax=maxz,edgecolors='k')            
    cbar=plt.colorbar(scat,ticks=levelsz,pad=0.01,shrink=1,format='%0.1f')
    cbar.set_label('$\^z_o$ (km)',labelpad=-18,y=-0.05, rotation=0,
                   fontsize=13)
    cbar.ax.tick_params(labelsize=13)
    ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
    ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
    ax.set_xticks([0,2,4,6,8])
    plt.text(8,8,'P2',color='w', size='large')
    plt.text(2,4,'P3',color='w', size='large')   
    
    
    plt.subplot(2,3,3)  
    plt.title(vet_title[1], fontsize = 14, loc='center',y=-0.39)
    plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                   data.reshape(shape), 30, cmap='gray')
    ax = plt.gca()
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    scat=plt.scatter(est_classic[0][:,1]/1000., est_classic[0][:,0]/1000.,
                     s=50,c=(est_classic[0][:,3]/1000.), cmap=my_cmap,
                     vmin=minb, vmax=maxb,edgecolors='k')            
    cbar=plt.colorbar(scat,ticks=levelsb,pad=0.01,shrink=1,format='%0.2f')
    cbar.set_label('$\^b$ (nT)',labelpad=-18,y=-0.05, rotation=0,
                   fontsize=13)
    cbar.ax.tick_params(labelsize=13)
    ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
    ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
    plt.text(8,8,'P2',color='w', size='large')
    plt.text(2,4,'P3',color='w', size='large')  
    
    
    
    plt.subplot(2,3,5)  
    plt.title(vet_title[2], fontsize = 14, loc='center',y=-0.39)
    plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                   data.reshape(shape), 30, cmap='gray')
    ax = plt.gca()
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    scat=plt.scatter(est_classic[1][:,1]/1000., est_classic[1][:,0]/1000.,
                     s=50,c=(est_classic[1][:,2]/1000.), cmap='terrain_r',
                     vmin=minz, vmax=maxz,edgecolors='k')            
    cbar=plt.colorbar(scat,ticks=levelsz,pad=0.01,shrink=1,format='%0.1f')
    cbar.set_label('$\^z_o$ (km)',labelpad=-18,y=-0.05, rotation=0,
                   fontsize=13)
    cbar.ax.tick_params(labelsize=13)
    ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
    ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
    ax.set_xticks([0,2,4,6,8])
    plt.text(8,8,'P2',color='w', size='large')
    plt.text(2,4,'P3',color='w', size='large')   
    
    
    plt.subplot(2,3,6)  
    plt.title(vet_title[3], fontsize = 14, loc='center',y=-0.39)
    plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                   data.reshape(shape), 30, cmap='gray')
    ax = plt.gca()
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    scat=plt.scatter(est_classic[1][:,1]/1000., est_classic[1][:,0]/1000.,
                     s=50,c=(est_classic[1][:,3]/1000.), cmap=my_cmap,
                     vmin=minb, vmax=maxb,edgecolors='k')            
    cbar=plt.colorbar(scat,ticks=levelsb,pad=0.01,shrink=1,format='%0.2f')
    cbar.set_label('$\^b$ (nT)',labelpad=-18,y=-0.05, rotation=0,
                   fontsize=13)
    cbar.ax.tick_params(labelsize=13)
    ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
    ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
    plt.text(8,8,'P2',color='w', size='large')
    plt.text(2,4,'P3',color='w', size='large')  
        
    plt.subplots_adjust(wspace=0.4,hspace=0.42)
    plt.savefig('figures/FIG5.png', bbox_inches='tight', dpi = 600)
    plt.close('all')
    gc.collect()
    
    return