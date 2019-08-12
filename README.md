# Reliable Euler deconvolution estimates throughout the vertical derivatives in the sensitivity matrix 

by
Felipe F. Melo and Valéria C.F. Barbosa

## About

This paper has been submitted for publication in *Computers & Geosciences*.

This repository contains the source code to perform the two synthetic tests presented.
The codes `euler_python.py`, the synthetic data `synthetic_data.dat` presented in the
paper and the codes `synthetic_test.py`, `estimates_statistics.py` and `plot_functions`
to generate the results of the synthetic test.

The *euler_python* program is compatible with both Python 2.7 and Python 3.7 programming language.
 
## Abstract

We propose a novel methodology to select reliable Euler deconvolution estimates throughout the 
vertical derivatives in the sensitivity matrix. For each moving data window, we compute the 
covariance matrix and then the standard deviation of the vertical derivatives. The moving data
windows with the largest standard deviation of the vertical derivatives define the location of
the sources. Assuming tentative SIs, the estimates with tight clustering define the correct 
structural index (SI). Traditionally, for each SI, the horizontal coordinates estimates obtained
for each position of a moving data window are plotted in the plan view of the study area and the
depth estimates are represented by different colors. We also show the base-level estimates plotted
in the same way and how they can be used to define the correct SI. We compare the estimates on
this plot where reliable solutions need to be selected (classic plot) with an alternative plot of
Euler estimates where all solutions are show (plateau plot). In the plateau plot, for each SI,
every Euler estimate is displayed against the central position of the moving data window. When 
the correct SI is assumed, the horizontal, depth and base-level estimates form plateaus of 
constant values over the source. The minimum standard deviation of depth or base-level estimates
defines the correct SI. We compare these methodologies to define the correct SI and visualize the
Euler deconvolution estimates through synthetic data in two distinct scenarios. First, four 
sources with distinct SI generate the total-field anomaly that is corrupted by an additive and 
strongly interfering nonlinear background. Second, two nearby sources generating a strongly 
interfering anomaly. In both cases, the results are satisfactory. We apply these methodologies
to the real magnetic anomaly of Anitápolis, Brazil, and they yields similar results. Therefore,
we may infer that a plug generates the Anitápolis anomaly.

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
