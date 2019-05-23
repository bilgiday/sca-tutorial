import numpy as np
import matplotlib.pyplot as plt

################## DON'T TOUCH: Utilities for later use ##################
# An array to keep Hamming weight values of all numbers from 0 to 255
# Hamming Weight(x) = Number of ones in a given x
# Example:
#	hw[146] = hw[1001_0010] = 3
#	hw[211] = hw[1101_0011] = 5
hw = [bin(n).count("1") for n in range (0,256)]
###########################################################################



################## DON'T TOUCH: Import Data ###############################
##  Traces, plaintexts, knownkey
trace_array = np.load(r'./traces/2018.11.24-21.52.36_traces.npy')
plaintext_array = np.load(r'./traces/2018.11.24-21.52.36_textin.npy')
###########################################################################

################## DON'T TOUCH: Input Parameters #########################
# Number of Traces and plaintexts
numTraces=1000
#Number of samples/points in each trace
numSamples=3000
###########################################################################

################# Your code starts here ###################

## Choose a byte of plaintext to compute correlation
bnum = 10;

## 1. Copy byte bnum of all plaintext into an array plaintext_bytes
## plaintext_array -> numTraces x 16
## plaintext_bytes  -> numTraces x 1
## a. Create and initialize plaintext_bytes
plaintext_bytes = np.zeros(numTraces)

## b. Copy byte bnum of all plaintexts into an array plaintext_bytes
plaintext_bytes = plaintext_array[??,??]  # YOUR CODE


## 2. Compute the Hamming Weight of plaintext_bytes
## Use the already created hw[] array in the Utilities Section above
## a. Array to keep hamming weights
plaintext_bytes_hw = np.zeros(numTraces)
## b. A loop to fill the array plaintext_bytes_hw
for tnum in range(0,numTraces):
	plaintext_bytes_hw[tnum] = hw[??] # YOUR CODE


## 3. Create the correlation trace by
##	  computing the Correlation Coefficient between
##		- each sample of trace_array[] and
##		- plaintext_bytes_hw.
##
## a. An array to keep correlation trace r (numSamples x 1)
r = np.zeros(numSamples)
## b. A loop to fill the correlation trace
##		- Use numPy corrcoef() function to compute 
##		  Pearson Correlation coefficient 
for snum in range(0,numSamples):
	r[snum] = np.corrcoef(trace_array[??,??],plaintext_bytes_hw)[0,1] # YOUR CODE

## 4. Plot the Correlation trace
plt.plot(r)
plt.title('Input Correlation Trace for byte %d'%bnum)
plt.xlabel('Samples')
plt.ylabel('Correlation Coeff (r)')
plt.show()
 
	

