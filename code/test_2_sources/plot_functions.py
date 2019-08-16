"""
Plot functions 

A Python program to plot the total-field anomaly and the estimates
on classic and plateau plots. 

This code plot the figures 7 and 8 in the folder 'figures'.

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
    vet_title=["(b)","(c)"]
    
    fig=plt.figure(figsize=(20, 5))
    
    plt.subplot(1,3,1)  
    
    plt.title('(a)', fontsize = 14, loc='center',y=-0.23)
    
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
    
    
    for i in range (2):
    
        plt.subplot(1,3,i+2)  
        plt.title(vet_title[i], fontsize = 14, loc='center',y=-0.23)
        plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                       data.reshape(shape), 30, cmap='gray')
        ax = plt.gca()
        ax.set_ylabel('Northing (km)', fontsize = 14)
        ax.set_xlabel('Easting (km)', fontsize = 14)
        ax.tick_params(labelsize=13)
        scat=plt.scatter(est_classic[i][:,1]/1000., est_classic[i][:,0]/1000.,
                         s=50,c=(est_classic[i][:,2]/1000.), cmap='terrain_r',
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
           
        
    plt.subplots_adjust(wspace=0.3)
        
    plt.savefig('figures/FIG7.png', bbox_inches='tight', dpi = 600)
    plt.close('all')
    gc.collect()
    
    return



def plot_plateau(data,est_plateau,xi,yi,zi,shape):
    '''
    Plateau plot of the depth and base level estimates for SI = 2 and 3
    '''
    vet_title=["(a)","(b)","(c)","(d)"]
    
    
    fig=plt.figure(figsize=(10, 10))
    for i in range (2):
        
        minz = np.min(-0.5)
        maxz = np.max(2)
        levelsz = np.linspace(minz,maxz,7)   
        
        #the range of the estimates is broad, so we need to limit the max and 
        # min in the plots in order to compare the plots
        data_plot=np.copy(est_plateau[i][:,2].reshape(shape))
        data_plot[(est_plateau[i][:,2].reshape(shape))<minz] = minz
        data_plot[(est_plateau[i][:,2].reshape(shape))>maxz] = maxz
        
        fig=plt.figure()
        ax=fig.add_subplot(111)
        im_ref=ax.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                           data_plot, 26,cmap='terrain_r',vmin=minz,vmax=maxz)
        plt.close(fig)
        gc.collect()
        # until here was to limit the colorbar
        plt.subplot(2,2,i*2+1)  
        rect_plt2=patches.Rectangle((6.2,6.5),0.7,1.3,linewidth=1,
                                    edgecolor='crimson',facecolor='none',
                                    linestyle='-',zorder=2)
        rect_plt3=patches.Rectangle((3.3,5),0.9,1.4,linewidth=1,
                                    edgecolor='crimson',facecolor='none',
                                    linestyle='-',zorder=2)
        plt.title(vet_title[i*2], fontsize = 14, loc='center',y=-0.25)
        im=plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                        est_plateau[i][:,2].reshape(shape)/1000., 30,
                        cmap='terrain_r',vmin=minz,vmax=maxz)
        ax = plt.gca()
        ax.contour(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                      est_plateau[i][:,2].reshape(shape)/1000.,15,
                      colors='k',linestyles='solid')
        ax.set_ylabel('Northing (km)', fontsize = 14)
        ax.set_xlabel('Easting (km)', fontsize = 14)
        ax.tick_params(labelsize=13)
        cbar=plt.colorbar(im_ref,boundaries=levelsz,ticks=levelsz,pad=0.01,
                          shrink=1,format='%.1f') 
        cbar.set_label('$\^z_o $ (km)',labelpad=-9,y=-0.03,rotation=0,
                       fontsize=13)
        cbar.ax.tick_params(labelsize=13)
        ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
        ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
        ax.set_xticks([0,2,4,6,8])
        ax.add_patch(rect_plt2)
        ax.add_patch(rect_plt3)
        plt.text(8,8,'P2',color='w', size='large')
        plt.text(2,4,'P3',color='w', size='large')

        #base  level plot       
        
        rect_plt2=patches.Rectangle((6.2,6.5),0.7,1.3,linewidth=1,
                                    edgecolor='white',facecolor='none',
                                    linestyle='-',zorder=2)
        rect_plt3=patches.Rectangle((3.3,5),0.9,1.4,linewidth=1,
                                    edgecolor='white',facecolor='none',
                                    linestyle='-',zorder=2)
    
        minb = np.min(-50)
        maxb = np.max(20)
        levelsb = np.linspace(minb,maxb,7)
        levelsb2 = np.linspace(minb,maxb,30)
  
        plt.subplot(2,2,i*2+2) 
        plt.title(vet_title[i*2+1], fontsize = 14, loc='center',y=-0.25)
        im=plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                     est_plateau[i][:,3].reshape(shape), levelsb2, 
                     cmap=my_cmap,vmin=minb,vmax=maxb)
        ax=plt.gca()
        ax.contour(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                  est_plateau[i][:,3].reshape(shape),levelsb,
                  colors='k',linestyles='solid')
        ax.set_ylabel('Northing (km)', fontsize = 14)
        ax.set_xlabel('Easting (km)', fontsize = 14)
        ax.tick_params(labelsize=13)
        cbar=plt.colorbar(im,ticks=levelsb,pad=0.01,shrink=1,format='%d')
        cbar.set_label('$\^b$ (nT)',labelpad=-18,y=-0.03, rotation=0,
                       fontsize=13)
        cbar.ax.tick_params(labelsize=13)
        ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
        ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
        ax.add_patch(rect_plt2)
        ax.add_patch(rect_plt3)            
        plt.text(8,8,'P2',color='w', size='large')
        plt.text(2,4,'P3',color='w', size='large')
        ax.set_xticks([0,2,4,6,8])
                    
    plt.subplots_adjust(wspace=0.3,hspace=0.3)
    plt.savefig('figures/FIG8.png', bbox_inches='tight', dpi = 600)    
    plt.close('all')
    gc.collect()
        
    return
