"""
Plot functions 

A Python program to plot the total-field anomaly and the estimates
on classic plot. 

This code plot the figures 3 and 4 in the folder 'figures'.

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

def plot_input_data(data,xi,yi,zi,shape):

    '''
    Plot the input data - Figure 2
    '''
    
    data_input=np.loadtxt('input/synthetic_base_level.dat')
    input_b=data_input[:,3]
    
    data_input=np.loadtxt('input/noise_synthetic_data.dat')
    noise_free_data=data_input[:,3]

    im1 = plt.imread('input/prisms_ppt.tif')
    
    
    fig=plt.figure(figsize=(13, 10))
    
    ax = plt.subplot(221)
    plt.title("(a)", fontsize = 14, loc='center',y=-0.26)
    ax.imshow(im1)
    ax.axis('off') 
    
    ax = plt.subplot(222)
    rect0 = patches.Rectangle((26,0),2,24,linewidth=1,edgecolor='crimson',
                              facecolor='none',linestyle='-',zorder=2)
    rect1 = patches.Rectangle((16.850,10),0.3,24,linewidth=1,
                              edgecolor='crimson',facecolor='none',
                              linestyle='-',zorder=2)
    rect2 = patches.Rectangle((6.850,15.850),0.3,0.3,linewidth=1,
                              edgecolor='crimson',facecolor='none',
                              linestyle='-',zorder=2)
    rect3 = patches.Rectangle((6.850,6.850),0.4,0.4,linewidth=1,
                              edgecolor='crimson',facecolor='none',
                              linestyle='-',zorder=2)
    plt.title("(b)", fontsize = 14, loc='center',y=-0.27)
    im=plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                   noise_free_data.reshape(shape), 30, cmap=my_cmap)
    ax = plt.gca()
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    cbar=fig.colorbar(im,pad=0.01,shrink=1)
    cbar.set_label('nT',labelpad=-21,y=-0.01, rotation=0,fontsize=13)
    ax.add_patch(rect0)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    ax.add_patch(rect3)
    cbar.ax.tick_params(labelsize=13)
    ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
    ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
    plt.text(22.5,5,'P0',color='w',weight='bold', size='x-large')
    plt.text(19.5,18,'P1',color='w',weight='bold', size='x-large')
    plt.text(7,19,'P2',color='w',weight='bold', size='x-large')
    plt.text(3,4,'P3',color='w',weight='bold', size='x-large')
    
    
    ax = plt.subplot(223)
    rect0 = patches.Rectangle((26,0),2,24,linewidth=1,edgecolor='crimson',
                              facecolor='none',linestyle='-',zorder=2)
    rect1 = patches.Rectangle((16.850,10),0.3,24,linewidth=1,
                              edgecolor='crimson',facecolor='none',
                              linestyle='-',zorder=2)
    rect2 = patches.Rectangle((6.850,15.850),0.3,0.3,linewidth=1,
                              edgecolor='crimson',facecolor='none',
                              linestyle='-',zorder=2)
    rect3 = patches.Rectangle((6.850,6.850),0.4,0.4,linewidth=1,
                              edgecolor='crimson',facecolor='none',
                              linestyle='-',zorder=2)
    plt.title("(c)", fontsize = 14, loc='center',y=-0.27)
    im=plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                   input_b.reshape(shape), 30, cmap=my_cmap)
    ax = plt.gca()
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    cbar=fig.colorbar(im,pad=0.01,shrink=1)
    cbar.set_label('nT',labelpad=-21,y=-0.03, rotation=0,fontsize=13)
    ax.add_patch(rect0)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    ax.add_patch(rect3)
    cbar.ax.tick_params(labelsize=13)
    ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
    ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
    plt.text(22.5,5,'P0',color='w',weight='bold', size='x-large')
    plt.text(19.5,18,'P1',color='w',weight='bold', size='x-large')
    plt.text(7,19,'P2',color='w',weight='bold', size='x-large')
    plt.text(3,4,'P3',color='w',weight='bold', size='x-large')
    
    ax = plt.subplot(224)
    rect0 = patches.Rectangle((26,0),2,24,linewidth=1,edgecolor='crimson',
                              facecolor='none',linestyle='-',zorder=2)
    rect1 = patches.Rectangle((16.850,10),0.3,24,linewidth=1,
                              edgecolor='crimson',facecolor='none',
                              linestyle='-',zorder=2)
    rect2 = patches.Rectangle((6.850,15.850),0.3,0.3,linewidth=1,
                              edgecolor='crimson',facecolor='none',
                              linestyle='-',zorder=2)
    rect3 = patches.Rectangle((6.850,6.850),0.4,0.4,linewidth=1,
                              edgecolor='crimson',facecolor='none',
                              linestyle='-',zorder=2)
    plt.title("(d)", fontsize = 14, loc='center',y=-0.27)
    im=plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                   data.reshape(shape), 30, cmap=my_cmap)
    ax = plt.gca()
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    cbar=fig.colorbar(im,pad=0.01,shrink=1)
    cbar.set_label('nT',labelpad=-21,y=-0.01, rotation=0,fontsize=13)
    ax.add_patch(rect0)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    ax.add_patch(rect3)
    cbar.ax.tick_params(labelsize=13)
    ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
    ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
    plt.text(22.5,5,'P0',color='w',weight='bold', size='x-large')
    plt.text(19.5,18,'P1',color='w',weight='bold', size='x-large')
    plt.text(7,19,'P2',color='w',weight='bold', size='x-large')
    plt.text(3,4,'P3',color='w',weight='bold', size='x-large')
        
    plt.subplots_adjust(wspace=0.15,hspace=0.3)
    
    plt.savefig('figures/FIG2.png', bbox_inches='tight', dpi = 600)
    plt.close('all')
    
    return

def plot_classic(data,est_classic,xi,yi,zi,shape):
    '''
    Classic plot of the depth and base level estimates for all SIs
    '''
    
    '''
    Figure 3 source-position (depth) estimates
    '''
    vet_title=["(a)","(b)","(c)","(d)"]
    
    
    minz = np.min(0.)
    maxz = np.max(1.5)
    levelsz = np.linspace(minz,maxz,7)   
    
    #depth plots
    plt.figure(figsize=(13, 10))
    for i in range (4):
     
        plt.subplot(2,2,i+1)  
        plt.title(vet_title[i], fontsize = 14, loc='center',y=-0.27)
        plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                       data.reshape(shape), 30, cmap='gray')
        ax = plt.gca()
        ax.set_ylabel('Northing (km)', fontsize = 14)
        ax.set_xlabel('Easting (km)', fontsize = 14)
        ax.tick_params(labelsize=13)
        scat=plt.scatter(est_classic[i][:,1]/1000., 
                         est_classic[i][:,0]/1000.,s=40,
                         c=(est_classic[i][:,2]/1000.),
                         cmap='terrain_r',vmin=minz,vmax=maxz,
                         edgecolors='k')             
        cbar=plt.colorbar(scat,ticks=levelsz,pad=0.01,shrink=1,
                          format='%0.1f')
        cbar.set_label('$\^z_o$ (km)',labelpad=-18,y=-0.03, rotation=0,
                       fontsize=13)
        cbar.ax.tick_params(labelsize=13)
        ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
        ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
        ax.set_xticks([0,5,10,15,20,25])
        plt.text(21,5,'P0',color='w', size='large')
        plt.text(19.5,18,'P1',color='w', size='large')
        plt.text(7,19,'P2',color='w', size='large')
        plt.text(3,2.3,'P3',color='w', size='large')   
        
    plt.subplots_adjust(wspace=0.15,hspace=0.32)
        
    plt.savefig('figures/FIG3.png',bbox_inches='tight', dpi = 600)
    plt.close('all')
    gc.collect()
        
        
    '''
    Figure 4 base level-position (base-level) estimates
    '''
    plt.figure(figsize=(13, 10))
    for i in range (4):
     
        if i == 0:
            #base level estimates for SI = 0 have higher amplitude
            minb = np.min(-70)
            maxb = np.max(20)
            levelsb = np.linspace(minb,maxb,7)
            
            plt.subplot(2,2,i+1) 
            plt.title(vet_title[i], fontsize = 14, loc='center',
                      y=-0.27)
            plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                           data.reshape(shape), 30, cmap='gray')
            ax=plt.gca()
            ax.set_ylabel('Northing (km)', fontsize = 14)
            ax.set_xlabel('Easting (km)', fontsize = 14)
            ax.tick_params(labelsize=13)
            scat=plt.scatter(est_classic[i][:,1]/1000.,
                             est_classic[i][:,0]/1000.,s=40,
                             c=(est_classic[i][:,3]/1000.), 
                             cmap=my_cmap,vmin=minb,
                             vmax=maxb,edgecolors='k')             
            cbar=plt.colorbar(scat,ticks=levelsb,pad=0.01,shrink=1,
                              format='%d')
            cbar.set_label('$\^b$ (nT)',labelpad=-18,y=-0.03, rotation=0,
                           fontsize=13)
            cbar.ax.tick_params(labelsize=13)
            ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
            ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
            ax.set_xticks([0,5,10,15,20,25])
            plt.text(21,5,'P0',color='w', size='large')
            plt.text(19.5,18,'P1',color='w', size='large')
            plt.text(7,19,'P2',color='w', size='large')
            plt.text(3,2.3,'P3',color='w',size='large') 
            plt.text(25,25,'x10$^{3}$',color='k',size='medium')
            
        else:
            minb = np.min(-30)
            maxb = np.max(210)
            levelsb = np.linspace(minb,maxb,7)
      
            plt.subplot(2,2,i+1) 
            plt.title(vet_title[i], fontsize = 14, loc='center',
                      y=-0.27)
            plt.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                           data.reshape(shape), 30, cmap='gray')
            ax=plt.gca()
            ax.set_ylabel('Northing (km)', fontsize = 14)
            ax.set_xlabel('Easting (km)', fontsize = 14)
            ax.tick_params(labelsize=13)
            scat=plt.scatter(est_classic[i][:,1]/1000., 
                             est_classic[i][:,0]/1000.,s=40,
                             c=(est_classic[i][:,3]),cmap=my_cmap,
                             vmin=minb, vmax=maxb,edgecolors='k')        
            cbar=plt.colorbar(scat,ticks=levelsb,pad=0.01,shrink=1,
                              format='%d')
            cbar.set_label('$\^b$ (nT)',labelpad=-18,y=-0.03, rotation=0,
                           fontsize=13)
            cbar.ax.tick_params(labelsize=13)
            ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
            ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
            ax.set_xticks([0,5,10,15,20,25])
            plt.text(21,5,'P0',color='w', size='large')
            plt.text(19.5,18,'P1',color='w', size='large')
            plt.text(7,19,'P2',color='w', size='large')
            plt.text(3,2.3,'P3',color='w',size='large')    
            
    plt.subplots_adjust(wspace=0.15,hspace=0.32)
        
    plt.savefig('figures/FIG4.png',bbox_inches='tight', dpi = 600)
    plt.close('all')
    gc.collect()
    
    return