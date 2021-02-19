# Synthetic test 1 – Distinct SIs and strong nonlinear magnetic base level

Running the code `synthetic_test.py` will allow the reprodution of the results.
The figures generated may differ from the publication and 
can be adapted in the script `plot_functions.py`.

## Input:

- input - synthetic_data.dat    
    	  2d-array with "n" rows by 4 columns: x-coordinate, y-coordinate, z-coordinate, anomaly.    
    	  Where "n" rows correspond to the size of the data

## Parameters:

- Size of the moving data window:    
    winsize - an odd integer number. 
              Ex.: for a moving data window of 5 x 5 grid points -> winsize = 5
                                  
- Percentage of the solutions that will be keep:
    filt - a float number ranging from 0.0 to 1.0. 
           Ex.: to keep 10% of the solutions -> filt = 0.1

- Structural indices used:
    SI_vet - an array that can store any of the four SIs.
             Ex.: to test only the SI = 1 -> SI_vet = [1] and to test the four SIs -> SI_vet = [0.001, 1, 2, 3]

- The areas to compute the statistics about the mean of the northing, easting and depth estimates:
    area_cla  - array defining the four vertices of a polygon 
                [south,north,west,east]

## Outputs:

- figures - Figures 2d, 4 and 7 of the synthetic example in the manuscript will be saved
		in this folder. The figures generated may differ from the publication and
		can be adapted in the script `plot_functions.py`.
		
- results - the mean of the northing, easting and depth estimates over the selected areas.


## Extra:

- to save the estimates in a txt file add to the end of the synthetic_test:

#convert the list to array
output=np.asarray(est_classic)
#save the estimates in distinct files according to the SI
for i in range(len(SI_vet)):
    np.savetxt("file_SI_" + str(i) + ".txt",output[i],delimiter=",")
