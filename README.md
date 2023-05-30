# Intel_oneAPI_AI_code
The following code are sourced from the Intel(R) Extension for Scikit-learn github page, the aim of the repo is to enable developer to test the Intel oneAPI AI Libraries
and see the performance difference in the Machine learning training time and also the power consumption of the CPU. 

# Guide to replicate the results 

## Setup of Python Environment
if you dont have ananconda install in your local enviornment.        
- step-1: Download Anaconda with the following link      
https://docs.anaconda.com/free/anaconda/install/     
- Step-2: installing anaconda with the following link      
  - Windows users: https://docs.anaconda.com/free/anaconda/install/windows/      
  - Linux users: https://docs.anaconda.com/free/anaconda/install/linux/      
  - Mac Os users: https://docs.anaconda.com/free/anaconda/install/mac-os/      

Once you installed the anaconda in you local environment follows the following commands:      
*conda create -n env python=3.10 scikit-learn-intelex
The above command will create conda virtual enviroemnt and then install scikit-learn in a new enviroments will all the dependancies need to run the codes.
To track the power consumption we need to install CodeCarbon 
*conda install -c conda-forge codecarbon

## Additional Information
### CPU
On Windows or Mac    

Tracks Intel processors power consumption using the Inter Power Gadget. You need to install it yourself from this source .      

On Linux      

Tracks Intel Processor power consumption from Inter RAPL files at \sys\class\powercap\intel-rapl ( reference ). All CPUs listed in this directory will be tracked. Help us improve this and make it configurable.

Note: The Power Consumption will be tracked only if the RAPL files exist at the above mentioned path
