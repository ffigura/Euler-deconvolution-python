# Reliable Euler deconvolution estimates throughout the vertical derivatives of the total-field anomaly

by Felipe F. Melo (Observatório Nacional) and Valéria C. F. Barbosa (Observatório
Nacional) (2019)

Email: felipe146@hotmail.com (F.F. Melo); valcris@on.br (V.C.F. Barbosa) 

This repository contains a collection of Python codes and synthetic data 
example for a paper about the open-source package Euler deconvolution.The 
example data reproduce the synthetc results and figures shown in the publication.
The Euler deconvolution package `euler_python.py` is compatible with Python 2.7
and 3.7 programming language. To run the program,the numpy library is required. 
In addition, numpy is to run the complementary codes for the tests `estimates_statistics.py`
and the matplotlib is required to run the scripts `plot_functions.py` and `synthetic_test.py`.

1 - Abstract

2 - Content

3 - Prerequisites

4 - Parameterization

5 - Running the files

6 - License

===============================================================================


1 - Abstract
----------------------
We propose a novel methodology to select reliable Euler deconvolution estimates throughout the vertical derivatives of the total-field anomaly. In applying Euler deconvolution to a small moving-data window, we compute the standard deviation of the vertical derivatives of the total-field anomaly for each data window. Then, we define the reliable source-location estimates as those estimates that are obtained by using the data windows with the largest standard deviations of the vertical derivatives of the total-field anomaly. For all tentative values of the structural index (SI), the reliable estimates with tight clustering define the correct SI and the mean of these estimates define the source-position. Our methodology successfully works in two complex scenarios. In the first one, multiple sources with distinct SI generate a total-field anomaly which in turn is corrupted by an additive nonlinear background that simulates a regional field. This regional field strongly interfere the anomalies produced by the sources, changing their amplitudes and shapes. In the second scenario, nearby sources give rise to strongly interfering anomalies. In both scenarios, our methodology correctly defines the SIs, the horizontal positions and the depths of the causative sources. Application to real magnetic anomaly from southern Brazil allows inferring the presence of a plug intrusion.

2 - Content
----------------------

Both synthetic tests can be reproduced with this codes. The test 1 can be reproduced from the folder
`test_4_sources` and the test 2 can be reproduced from the folder `test_2_sources`.

Python codes:

	- euler_python.py
		General Python module containing the functions to compute de derivatives and Euler deconvolution.
	
	- synthetic_test.py
		Python script to generate the synthetic results. The script loads the total-field
		anomaly of a synthetic model from the file "synthetic_data.dat" and computes the
		Euler deconvolution using the functions in "euler_python.py". The results are 
		generated using the functions "plot_functions.py" for the plots and 
		"estimates_statistics.py" to compute the statistics of the data. 
		
	- plot_functions.py:
		Python script to generate the figures in the synthetic tests results. 
	
	- estimates_statistics.py:
		Python script to compute the mean of the depth estimates. 
	
Outputs: 
 
	- figures - all figures that generated the synthetic example in the manuscript will be saved
			in this folder. The figures generated may differ from the publication and
			can be adapted in the script `plot_functions.py`.
						 
	- results - the mean of the depth estimates over the selected areas.

Test data:

	- input/synthetic_data.dat
		Synthetic magnetic data generated using the Python packaged "Fatiando a Terra":	
		http://fatiando.org/. This data is an example used in the current publication.
	
3 - Prerequisites
----------------------
The Python program Euler deconvolution - `euler_python.py` and the scripts `estimates_statistics.py` requires 
the Python library "numpy" and the scripts `synthetic_test.py` and `plot_functions.py` requires the Python
packages "numpy" and "matplotlib". 
The easier way to get Python and all libraries installed is through the Anaconda Python 
distribution (https://www.anaconda.com/distribution/). After installed Anaconda, install the libraries 
by running the following command in your terminal:

	conda install numpy matplotlib

The program for Euler deconvolution `euler_python.py` and the algorithm `synthetic_test.py`
 are compatible with both Python 2.7 and 3.7.
 
4 - Parameterization
----------------------
There are the two parameters of our methodology for Euler deconvolution: window size and the percentage of solutions to keep. 
The moving data window size is defined in the parameter `winsize` and the percentage of the solutions that will be keep is defined in the parameter `filt`.

Additionally, the structural indexes are defined in the vector `SI_vet` and the areas used to get the statistics about the mean depth are defined in the vector  `area_cla=[S,N,W,E]`, where the vertices of a polygon are defined as south,northing,west,east - meters the same unit as input.

5 - Running the files
----------------------
After Anaconda and the libraries are installed, you need to run 
the code `synthetic_test.py` to generate the results.
There are two easy ways to run the synthetic test `synthetic_test.py`

1. Via command line: 

	1.1 On linux based systems open the command prompt windows (terminal), and run the command:
	
	On Python 2.7: python synthetic_test.py 
	On Python 3.7: python3 synthetic_test.py 

	1.2 On windows based systems open the Iphyton console (Python 2.7) or 
	Anaconda Navigator and then Jupyter QtConsole (Python 3.7), and run the command:

	run synthetic_test.py

2. Open the Spyder program that comes with the Ananconda installation. In the Spyder, open
the example script "synthetic_test.py" and click in "play" inside the Spyder to execute it.

If everything runs ok, the figures and results shown in the publication will be saved, respectively,
on the folders: `/figures` and `/results`.

The  module `euler_python.py` can be imported to an interactive Python session or called from
an external Python module. The functionalities are documented using standard Python
docstrings.

The file `synthetic_test.py` is a Python-based command line script. By using this 
script, the figures and results of the synthetic test presented in the publication can be reproduced.
The figures generated may differ from the publication and can be adapted in the script `plot_functions.py`.


6 - License
----------------------
The following legal note is restricted solely to the content of the named files. It cannot
overrule licenses from the Python standard distribution modules, which are imported and
used therein.

The `euler_python.py`, `synthetic_test.py`, `plot_functions.py` and `estimates_statistics.py`
files are distributed under the following license agreement:

BSD 3-clause license

Copyright (c) 2019 Felipe F. Melo and Valéria C.F. Barbosa.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the names of the copyright holders nor the names of any contributors
  may be used to endorse or promote products derived from this software
  without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
