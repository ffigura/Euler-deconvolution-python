"""
Euler deconvolution 

A Python program to perform Euler deconvolution on gridded data
and visualization of the estimates on classic and plateau plots.

The program is under the conditions terms in the file README.txt

authors: Felipe F. Melo and Valeria C.F. Barbosa, 2019
email: felipe146@hotmail.com, valcris@on.br
"""

import numpy as np
import matplotlib.pylab as plt
import matplotlib.patches as patches
import matplotlib as mpl
import euler_python as euler

class nf(float):
    #get contourlines for contour plot
    def __repr__(self):
        str = '%.1f' % (self.__float__(),)
        if str[-1] == '0':
            return '%.0f' % self.__float__()
        else:
            return '%.1f' % self.__float__()
        
def classic_plot_z(data,estx,esty,estz,yi,xi,shape,SI,name,filt):
    #plot of solutions on classic way - z estimates 
    rect1 = patches.Rectangle((5.85,5.85),0.4,0.4,linewidth=1,
                   edgecolor='crimson',facecolor='none',linestyle='-',zorder=2)
    rect2 =patches.Rectangle((13.85,15.85),0.3,0.3,linewidth=1,
                   edgecolor='crimson',facecolor='none',linestyle='-',zorder=2)

    minz = np.min(-0.3)
    maxz = np.max(1.6)
    levelsz = np.linspace(minz,maxz,15)

    fig=plt.figure(figsize=(5,5))
    ax=fig.add_subplot(111)
    ax.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                   data.reshape(shape), 30, cmap='gray')
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    scat=plt.scatter(estx/1000., esty/1000.,s=50,
                         c=(estz/1000.), cmap='terrain_r', edgecolor='black',
                     vmin=minz, vmax=maxz)    
    cbar=fig.colorbar(scat,ticks=levelsz,pad=0.01,shrink=1,format='%0.1f')
    cbar.set_label('$\^z_o $ (km)',labelpad=-18,y=-0.03,rotation=0,fontsize=13)
    cbar.ax.tick_params(labelsize=13)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    plt.text(16,20,'B',color='k',weight='bold', size='x-large')
    plt.text(9,9,'A',color='k',weight='bold', size='x-large') 
    ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
    ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
    ax.set_xticks([0,5,10,15])
    plt.savefig('results/figures/Fig.4_SI_'+ str(SI)+'_'+str(name)+'.png',
                dpi=300,bbox_inches='tight')
    plt.close(fig)
    
    return        
        
def classic_plot_b(data,estx,esty,estb,yi,xi,shape,SI,name,filt):
    #plot of solutions on classic way - b estimates    
    rect1 = patches.Rectangle((5.85,5.85),0.4,0.4,linewidth=1,
                   edgecolor='crimson',facecolor='none',linestyle='-',zorder=2)
    rect2 =patches.Rectangle((13.85,15.85),0.3,0.3,linewidth=1,
                   edgecolor='crimson',facecolor='none',linestyle='-',zorder=2)

    minb = np.min(-3)
    maxb = np.max(4)
    levelsb = np.linspace(minb,maxb,15)

    fig=plt.figure(figsize=(5,5))
    ax=fig.add_subplot(111)
    ax.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                   data.reshape(shape), 30, cmap='gray')
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    scat=plt.scatter(estx/1000., esty/1000.,s=50, edgecolor='black',
                         c=(estb), cmap=my_cmap,vmin=minb,vmax=maxb)
    cbar=fig.colorbar(scat,ticks=levelsb,pad=0.01,shrink=1,format='%.1f')
    cbar.set_label('$\^b $ (nT)',labelpad=-22,y=-0.03, rotation=0,fontsize=13)
    cbar.ax.tick_params(labelsize=13)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    plt.text(16,20,'B',color='k',weight='bold', size='x-large')
    plt.text(9,9,'A',color='k',weight='bold', size='x-large') 
    ax.set_xlim(np.min(yi/1000.),np.max(yi/1000.))
    ax.set_ylim(np.min(xi/1000.),np.max(xi/1000.))
    ax.set_xticks([0,5,10,15])
    plt.savefig('results/figures/Fig.4_SI_'+ str(SI)+'_'+str(name)+'.png',
                dpi=300,bbox_inches='tight')
    plt.close(fig)
    
    return   

def plateu_plot_x(estimate,yi,xi,shape,SI,area_plt1,area_plt2,name):
    #plot of solutions on plateau way - x and y estimates    
    rect1 = patches.Rectangle((5.85,5.85),0.4,0.4,linewidth=1,
                   edgecolor='crimson',facecolor='none',linestyle='-',zorder=2)
    rect2 =patches.Rectangle((13.85,15.85),0.3,0.3,linewidth=1,
                   edgecolor='crimson',facecolor='none',linestyle='-',zorder=2)
    rectplt1 = patches.Rectangle((area_plt1[2]/1000.,area_plt1[0]/1000.),
           (area_plt1[3]-area_plt1[2])/1000.,(area_plt1[1]-area_plt1[0])/1000.,
           linewidth=1,edgecolor='white',facecolor='none',linestyle='-',
           zorder=3)    
    rectplt2 = patches.Rectangle((area_plt2[2]/1000.,area_plt2[0]/1000.),
           (area_plt2[3]-area_plt2[2])/1000.,(area_plt2[1]-area_plt2[0])/1000.,
           linewidth=1,edgecolor='white',facecolor='none',linestyle='-',
           zorder=3)
    fig=plt.figure(figsize=(5,5))
    ax=fig.add_subplot(111)
    im=ax.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                   estimate.reshape(shape)/1000., 30, cmap='terrain_r')
    CS=ax.contour(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
               estimate.reshape(shape)/1000.,15, colors='k',linestyles='solid')
    CS.levels=[nf(val) for val in CS.levels]
    ax.clabel(CS, CS.levels, inline=True, fmt = '%d', fontsize=12)
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    cbar=fig.colorbar(im,pad=0.01,shrink=1,format='%d') 
    cbar.set_label('$\^x_o $ (km)',labelpad=-9,y=-0.03,rotation=0,fontsize=13)
    cbar.ax.tick_params(labelsize=13)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    ax.add_patch(rectplt1)    
    ax.add_patch(rectplt2)   
    ax.set_xticks([0,5,10,15])
    plt.text(16,20,'B',color='w',weight='bold', size='x-large')
    plt.text(9,9,'A',color='w',weight='bold', size='x-large') 
    plt.savefig('results/figures/Fig.5_SI_'+ str(SI)+'_'+str(name)+'.png',
                dpi=300,bbox_inches='tight')
    plt.close(fig)
    
    return

def plateu_plot_y(estimate,yi,xi,shape,SI,area_plt1,area_plt2,name):
    #plot of solutions on plateau way - x and y estimates    
    rect1 = patches.Rectangle((5.85,5.85),0.4,0.4,linewidth=1,
                   edgecolor='crimson',facecolor='none',linestyle='-',zorder=2)
    rect2 =patches.Rectangle((13.85,15.85),0.3,0.3,linewidth=1,
                   edgecolor='crimson',facecolor='none',linestyle='-',zorder=2)
    rectplt1 = patches.Rectangle((area_plt1[2]/1000.,area_plt1[0]/1000.),
           (area_plt1[3]-area_plt1[2])/1000.,(area_plt1[1]-area_plt1[0])/1000.,
           linewidth=1,edgecolor='white',facecolor='none',linestyle='-',
           zorder=3)    
    rectplt2 = patches.Rectangle((area_plt2[2]/1000.,area_plt2[0]/1000.),
           (area_plt2[3]-area_plt2[2])/1000.,(area_plt2[1]-area_plt2[0])/1000.,
           linewidth=1,edgecolor='white',facecolor='none',linestyle='-',
           zorder=3)
    fig=plt.figure(figsize=(5,5))
    ax=fig.add_subplot(111)
    im=ax.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                   estimate.reshape(shape)/1000., 30, cmap='terrain_r')
    CS=ax.contour(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
               estimate.reshape(shape)/1000.,15, colors='k',linestyles='solid')
    CS.levels=[nf(val) for val in CS.levels]
    ax.clabel(CS, CS.levels, inline=True, fmt = '%d', fontsize=12)
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    cbar=fig.colorbar(im,pad=0.01,shrink=1,format='%d') 
    cbar.set_label('$\^x_o $ (km)',labelpad=-9,y=-0.03,rotation=0,fontsize=13)
    cbar.ax.tick_params(labelsize=13)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    ax.add_patch(rectplt1)    
    ax.add_patch(rectplt2)   
    ax.set_xticks([0,5,10,15])
    plt.text(16,20,'B',color='w',weight='bold', size='x-large')
    plt.text(9,9,'A',color='w',weight='bold', size='x-large') 
    plt.savefig('results/figures/Fig.5_SI_'+ str(SI)+'_'+str(name)+'.png',
                dpi=300,bbox_inches='tight')
    plt.close(fig)
    
    return

def plateu_plot_z(estimate,yi,xi,shape,SI,area_plt1,area_plt2,name):
    #plot of solutions on plateau way - z estimates        
    rect1 = patches.Rectangle((5.85,5.85),0.4,0.4,linewidth=1,
                   edgecolor='crimson',facecolor='none',linestyle='-',zorder=2)
    rect2 =patches.Rectangle((13.85,15.85),0.3,0.3,linewidth=1,
                   edgecolor='crimson',facecolor='none',linestyle='-',zorder=2)
    rectplt1 = patches.Rectangle((area_plt1[2]/1000.,area_plt1[0]/1000.),
           (area_plt1[3]-area_plt1[2])/1000.,(area_plt1[1]-area_plt1[0])/1000.,
           linewidth=1,edgecolor='white',facecolor='none',linestyle='-',
           zorder=3)    
    rectplt2 = patches.Rectangle((area_plt2[2]/1000.,area_plt2[0]/1000.),
           (area_plt2[3]-area_plt2[2])/1000.,(area_plt2[1]-area_plt2[0])/1000.,
           linewidth=1,edgecolor='white',facecolor='none',linestyle='-',
           zorder=3)
    
    minz = np.min(-0.3)
    maxz = np.max(1.6)
    levelsz = np.linspace(minz,maxz,15)
    levelsz2 = np.linspace(minz,maxz,30)
    
    fig=plt.figure(figsize=(5,5))
    ax=fig.add_subplot(111)
    im=ax.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                   estimate.reshape(shape)/1000., levelsz2, cmap='terrain_r',
                   vmin=minz,vmax=maxz)
    CS=ax.contour(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
               estimate.reshape(shape)/1000.,levelsz, colors='k',
               linestyles='solid')
    CS.levels=[nf(val) for val in CS.levels]
    ax.clabel(CS, CS.levels, inline=True, fmt = '%d', fontsize=12)
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    cbar=fig.colorbar(im,boundaries=levelsz,ticks=levelsz,pad=0.01,shrink=1,
                      format='%.1f') 
    cbar.set_label('$\^z_o $ (km)',labelpad=-17,y=-0.03,rotation=0,fontsize=13)
    cbar.ax.tick_params(labelsize=13)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    ax.add_patch(rectplt1)    
    ax.add_patch(rectplt2) 
    plt.text(16,20,'B',color='w',weight='bold', size='x-large')
    plt.text(9,9,'A',color='w',weight='bold', size='x-large') 
    ax.set_xticks([0,5,10,15])
    plt.savefig('results/figures/Fig.5_SI_'+ str(SI)+'_'+str(name)+'.png',
                dpi=300,bbox_inches='tight')
    plt.close(fig)
    
    return

def plateu_plot_b(estimate,yi,xi,shape,SI,area_plt1,area_plt2,name):
    #plot of solutions on plateau way - b estimates        
    rect1 = patches.Rectangle((5.85,5.85),0.4,0.4,linewidth=1,
                   edgecolor='crimson',facecolor='none',linestyle='-',zorder=2)
    rect2 =patches.Rectangle((13.85,15.85),0.3,0.3,linewidth=1,
                   edgecolor='crimson',facecolor='none',linestyle='-',zorder=2)
    rectplt1 = patches.Rectangle((area_plt1[2]/1000.,area_plt1[0]/1000.),
           (area_plt1[3]-area_plt1[2])/1000.,(area_plt1[1]-area_plt1[0])/1000.,
           linewidth=1,edgecolor='white',facecolor='none',linestyle='-',
           zorder=3)    
    rectplt2 = patches.Rectangle((area_plt2[2]/1000.,area_plt2[0]/1000.),
           (area_plt2[3]-area_plt2[2])/1000.,(area_plt2[1]-area_plt2[0])/1000.,
           linewidth=1,edgecolor='white',facecolor='none',linestyle='-',
           zorder=3)
    
    minb = np.min(-3)
    maxb = np.max(4)
    levelsb = np.linspace(minb,maxb,15)
    levelsb2 = np.linspace(minb,maxb,30)
    
    fig=plt.figure(figsize=(5,5))
    ax=fig.add_subplot(111)
    im=ax.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                   estimate.reshape(shape), levelsb2, cmap=my_cmap)
    CS=ax.contour(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
                estimate.reshape(shape),levelsb, colors='k',linestyles='solid')
    CS.levels=[nf(val) for val in CS.levels]
    ax.clabel(CS, CS.levels, inline=True, fmt = '%0.1f', fontsize=12)
    ax.set_ylabel('Northing (km)', fontsize = 14)
    ax.set_xlabel('Easting (km)', fontsize = 14)
    ax.tick_params(labelsize=13)
    cbar=fig.colorbar(im,ticks=levelsb,boundaries=levelsb,pad=0.01,shrink=1,
                      format='%0.1f')
    cbar.set_label('$\^b $ (nT)',labelpad=-17,y=-0.03, rotation=0,fontsize=13)
    cbar.ax.tick_params(labelsize=13)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    ax.add_patch(rectplt1)    
    ax.add_patch(rectplt2)
    ax.set_xticks([0,5,10,15])
    plt.text(16,20,'B',color='w',weight='bold', size='x-large')
    plt.text(9,9,'A',color='w',weight='bold', size='x-large') 
    plt.savefig('results/figures/Fig.5_SI_'+ str(SI)+'_'+str(name)+'.png',
                dpi=300,bbox_inches='tight')
    plt.close(fig)
    
    return

#for a nice plot of magnetic anomaly and b-estimates following Niccoli (2014)      
LinL = np.loadtxt('Linear_L_0-1.txt')

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
# print rgb
# creating dictionary
k=['red', 'green', 'blue']
LinearL=dict(zip(k,rgb)) # makes a dictionary from 2 lists
#this is the new colormap
my_cmap = mpl.colors.LinearSegmentedColormap('my_colormap',LinearL)  
"""
The test starts here
"""        
# from the model
shape = (120, 100)
area = [0, 24000, 0, 20000]

data_input=np.loadtxt('synthetic_data.dat')
xi=data_input[:,0]
yi=data_input[:,1]
zi=data_input[:,2]
data=data_input[:,3]


rect1 = patches.Rectangle((5.85,5.85),0.4,0.4,linewidth=1,edgecolor='crimson',
                          facecolor='none',linestyle='-',zorder=2)
rect2 =patches.Rectangle((13.85,15.85),0.3,0.3,linewidth=1,edgecolor='crimson',
                         facecolor='none',linestyle='-',zorder=2)

fig=plt.figure(figsize=(5,5))
ax=fig.add_subplot(111)
im=ax.contourf(yi.reshape(shape)/1000.,xi.reshape(shape)/1000.,
               data.reshape(shape), 30, cmap=my_cmap)
ax.set_ylabel('Northing (km)', fontsize = 14)
ax.set_xlabel('Easting (km)', fontsize = 14)
ax.tick_params(labelsize=13)
cbar=fig.colorbar(im,pad=0.01,shrink=1)
cbar.set_label('nT',labelpad=-21,y=-0.01, rotation=0,fontsize=13)
ax.add_patch(rect1)
ax.add_patch(rect2)
cbar.ax.tick_params(labelsize=13)
plt.text(16,20,'B',color='k',weight='bold', size='x-large')
plt.text(9,9,'A',color='k',weight='bold', size='x-large') 
plt.savefig('results/figures/Fig.3b_input.png',dpi=300,bbox_inches='tight')
plt.close(fig)

#moving data window size
winsize=9
#percentage of the solutions that will be keep
filt=0.05
#structural index - in this case let's run for two SIs
SI = [2,3]

#output statistics for classic plot
stat_cla1=[]
stat_cla2=[]
#output statistics for plateau plot
stat_plt1=[]
stat_plt2=[]
#area for computation of the solutions' statistics
#rectangle with vertices on [south,north,west,east]
area_plt1=np.array([5000,7000,5000,7000])
area_plt2=np.array([15000,17000,13000,15000])

for i, SI in enumerate(SI):
    #all estimates, for plateau plot, and selected estimates for classic plot
    est_plt,est_cl=euler.euler_deconv(data,xi,yi,zi,shape,area,SI,winsize,filt)
    
    #statistics on traditional plot
    #southernmost source - A in manuscript
    filt_cla1=euler.statistics_solutions(est_cl,area_plt1)
    stat_cla1.append((SI,filt_cla1[0],filt_cla1[1],filt_cla1[2],filt_cla1[3],
                      filt_cla1[4],filt_cla1[5],filt_cla1[6],filt_cla1[7]))
    #northernmost source - B in manuscript    
    filt_cla2=euler.statistics_solutions(est_cl,area_plt2)
    stat_cla2.append((SI,filt_cla2[0],filt_cla2[1],filt_cla2[2],filt_cla2[3],
                      filt_cla2[4],filt_cla2[5],filt_cla2[6],filt_cla2[7],))    

    #statistics on plateau plot - the analysis is over plan coordinates
    est_plt_stat=np.stack((xi,yi,est_plt[:,2],est_plt[:,3]),axis=-1) 
    #southernmost source - A in manuscript
    filt_plt1=euler.statistics_solutions(est_plt_stat,area_plt1)
    stat_plt1.append((SI,filt_plt1[0],filt_plt1[1],filt_plt1[2],filt_plt1[3],
                      filt_plt1[4],filt_plt1[5],filt_plt1[6],filt_plt1[7]))   
    #northernmost source - B in manuscript        
    filt_plt2=euler.statistics_solutions(est_plt_stat,area_plt2)    
    stat_plt2.append((SI,filt_plt2[0],filt_plt2[1],filt_plt2[2],filt_plt2[3],
                      filt_plt2[4],filt_plt2[5],filt_plt2[6],filt_plt2[7]))   
    
    #Classic plots of Fig. 4
    #all solutions - plot "plateau estimates" as scatter plot or 
    #"classic estimates" with filt=1 generates the same result
    #the only visual difference is the order where the estimates are plotted
    classic_plot_z(data,est_plt[:,1],est_plt[:,0],est_plt[:,2],
                   yi,xi,shape,SI,'z_est',1)
    classic_plot_b(data,est_plt[:,1],est_plt[:,0],est_plt[:,3],
                   yi,xi,shape,SI,'b_est',1)
    #best solutions
    classic_plot_z(data,est_cl[:,1],est_cl[:,0],est_cl[:,2],
                   yi,xi,shape,SI,'z_est',filt)    
    classic_plot_b(data,est_cl[:,1],est_cl[:,0],est_cl[:,3],
                   yi,xi,shape,SI,'b_level',filt)    
    
    # Plateau plots of Fig. 5
    plateu_plot_x(est_plt[:,0],yi,xi,shape,SI,area_plt1,area_plt2,'outx')
    plateu_plot_y(est_plt[:,1],yi,xi,shape,SI,area_plt1,area_plt2,'outy')
    plateu_plot_z(est_plt[:,2],yi,xi,shape,SI,area_plt1,area_plt2,'outz')
    plateu_plot_b(est_plt[:,3],yi,xi,shape,SI,area_plt1,area_plt2,'outb')
    
    xy_estimates=np.stack((xi,yi,est_plt[:,0],est_plt[:,1],est_plt[:,2],
                       est_plt[:,3]),axis=-1)    

    #save estimates for plateau plot with coordinates 
    np.savetxt('results/estimates/all_estimates_SI_'+ str(SI)+'.dat',
               xy_estimates,delimiter=' ',fmt='%1.3f',header="coorx, coordy,"\
           "outx,outy, outz,outb",comments='')
    xy_estimates=[]
    #save estimates for traditional plot
    np.savetxt('results/estimates/selected_estimates_SI_'+ str(SI)+'.dat',
               est_cl,delimiter=' ',fmt='%1.3f',header="coorx, coordy,"\
           "outx,outy, outz,outb",comments='')
    


#statistics of the estimate on traditional plot
np.savetxt('results/estimates/statistics_classic_sourceA.txt',stat_cla1,
           fmt='%0.3f',header="SI, mean x,std x,mean y, std y,mean z, std z,"\
           "mean b,std b",comments='')     
np.savetxt('results/estimates/statistics_classic_sourceB.txt',stat_cla2,
           fmt='%0.3f',header="SI, mean x,std x,mean y, std y,mean z, std z,"\
           "mean b,std b",comments='')     
#statistics of the estimate on plateau plot
np.savetxt('results/estimates/statistics_plateau_sourceA.txt',stat_plt1,
           fmt='%0.3f',header="SI, mean x,std x,mean y, std y,mean z, std z,"\
           "mean b,std b",comments='')     
np.savetxt('results/estimates/statistics_plateau_sourceB.txt',stat_plt2,
           fmt='%0.3f',header="SI, mean x,std x,mean y, std y,mean z, std z,"\
           "mean b,std b",comments='')     
		   
print ('Congratulations, go to /results/figures and /results/estimates.')