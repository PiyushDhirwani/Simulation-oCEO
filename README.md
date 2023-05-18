## Library for simulation of molecules and atom types with python code
- lnpi_gen.py
  - Probability Distributions
  - Graph and Normalization
  - file_type = gnn.dat, gn_m.dat
  - Results displayed right after code run

--------
- moments_gen.py
  - First, second, third and fourth order moments
  - With average strategy and without average strategy
  - Center moments from complex numbers libraries
  - Results presented in avg_std_1 and avg_std_2 folders
--------
- prop_gen.py
  - Third and fourth order moments
  - Skewness and kurtosis parameters
  - Compressibility using moments
  - Results will be displayed in console output

-----

- clustering.py
  - Create clustes of same molecule and atom type
  - Iterate over number of processor
  - Read files from the folder with format type xyz_{Process_no.}_{file_no.}.dat

---- 
- radial_distribution_function.py
  - Iterate over number of processor
  - Read files from the folder with format type xyz_{Process_no.}_{file_no.}.dat
  - For molecule_type1, molecule_type1 and particle_type1, particle_type2


## Data Folders

- d0.1_T0.85_data_validate_python
  - R4, R5, R6, R7
  - Data files gnn.dat, gn_m.dat, central_moments.dat, moments.dat
---------
- SW_HS_db0.1_T0.85
  - R1, R2, R3, R4, R5, R6, R7
  - Data files xyz_{Process_no.}_{file_no.}.dat for cluster and RDF


## Testing

- sim_lib.py
  - Main library with all functions already imported
  - Directly call ```import sim_lib``` or ```from sim_lib import *```
--------
- test.py
  - Call ```from sim_lib import sim_lib```
  - Assign ```simulator=sim_lib()```
  - Call any function with ```simulator.{function_name}```


## Setup
- Clone the repo with ```git clone https://github.com/PiyushDhirwani/Simulation-oCEO.git```
- Or directly download the .zip file from the *Code* section
- In the new terminal or cmd run ```pip install -e .```