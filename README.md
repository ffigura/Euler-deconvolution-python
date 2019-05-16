# Euler deconvolution estimates on classic and plateau plots - A Python implementation

by
Felipe F. Melo and Valéria C.F. Barbosa

## About

This paper has been submitted for publication in *Computers & Geosciences*.

This repository contains the source code `euler_python.py`, the synthetic data `synthetic_data.dat` presented in the paper and script `synthetic_euler_python.py` to generate the results of the synthetic test.

The *euler_python* program is compatible with both Python 2.7 and Python 3.7 programming language.

In this work, we compare the classic and the plateau plots of Euler deconvolution estimates for gridded data to interpret magnetic anomaly. This work is a further step to clarify how these plots work in defining the source-position estimates in Euler deconvolution. We also show an application to the real magnetic data Anitápolis, southern Brazil, and infer the that a plug is the causative source.
 
## Abstract

Euler deconvolution is a popular method for interpretation of potential-field data. 
The method estimates the position of a geologic source and the data background (base level)
based on the magnetic or gravimetric data, for a given nature (i.e., structural index – SI).
These estimates are computed using a moving data-window scheme spanning the whole dataset. 
The selection of the best estimates uses the plot of these estimates. Traditionally, for each 
SI, the horizontal coordinates estimates obtained for each position of a moving data window 
are plotted in the plan view of the study area and the depth estimates are represented by different
color. This plot requires a statistical criterion to select the best estimates for each SI. In this
case, mostly, the base-level estimates are computed but they are neither used nor shown. Henceforth,
this traditional representation of Euler solution will be referred to as “classic plot” of Euler 
solutions. We compare the classic plot with an alternative plot of Euler estimates (henceforth referred
to “plateau plot” of Euler solutions). In the plateau plot, for each SI, every Euler estimate is 
displayed against the central position of the moving data window. At plateau plot, when the correct
SI is used the horizontal, depth and base-level estimates form a plateau of constant values over the
source. We compare the visualization of Euler deconvolution estimates using classic and plateau plots
through synthetic data generated by two sources with distinct SI, obtaining similar results. In addition,
we plot the base-level estimates in the classic and traditional way to perform the comparison. We also
compare these visualizations of solutions by applying Euler deconvolution to the real magnetic anomaly
of Anitápolis in southern Brazil. Either classic or plateau plots of Euler estimates yields similar 
results and we may infer that a plug generates the Anitápolis anomaly.

## Content

- euler_python.py:
	General Python module containing the functions to compute de derivatives and 
	Euler deconvolution.
	
- synthetic_euler_python.py:
	Python script to generate the synthetic results. The script loads the total-field
	anomaly of a synthetic model from the file "synthetic_data.dat" and computes the
	Euler deconvolution using the functions in "euler_python.py". 
	
Test data:

- synthetic_data.dat:
		Synthetic magnetic data generated using the Python packaged "Fatiando a Terra":
		http://fatiando.org/. This data is an example used in the current publication.

## Getting the code

You can download a copy of all the files in this repository by cloning the
[git](https://git-scm.com/) repository:

    git clone https://github.com/ffigura/Euler-deconvolution-python.git

or [download a zip archive](https://github.com/ffigura/Euler-deconvolution-python/archive/master.zip).

A copy of the repository is also archived at *insert DOI here*


## Dependencies

The Python program Euler deconvolution - "euler_python.py" requires the Python library "numpy" 
and the script "synthetic_euler_python.py" requires the Python packages "numpy" and "matplotlib". 
The easier way to get Python and all libraries installed is through the Anaconda Python 
distribution (https://www.anaconda.com/distribution/). After installed Anaconda, install the libraries 
by running the following command in your terminal:

	conda install numpy matplotlib

The program for Euler deconvolution "euler_python.py" and "synthetic_euler_python.py"
 are compatible with both Python 2.7 and 3.7.

## Reproducing the results

The results and figures for the synthetic test are reproducible from the folder `code/`.
Ruuning the code `synthetic_euler_python.py` will allow the reprodution of the results. For more information
read the file `README.MD` or `README.txt` in the folder `code/`.


## License

All source code is made available under a BSD 3-clause license. You can freely
use and modify the code, without warranty, so long as you provide attribution
to the authors. See `LICENSE.md` for the full license text.

The manuscript text is not open source. The authors reserve the rights to the
article content, which is currently submitted for publication in the
*Computers & Geosciences*.
