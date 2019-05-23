import numpy as np
import matplotlib.pyplot as plt
import random

################## DON'T TOUCH: Utilities for later use ##################
# An array to keep Hamming weight values of all numbers from 0 to 255
# Hamming Weight(x) = Number of ones in a given x
# Example:
#	hw[146] = hw[1001_0010] = 3
#	hw[211] = hw[1101_0011] = 5
hw = [bin(n).count("1") for n in range (0,256)]

## AES Sbox lookup table
sbox=(
0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,
0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,
0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,
0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,
0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,
0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,
0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,
0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,
0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,
0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,
0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,
0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,
0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,
0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,
0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,
0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16)

# A function to compute the value of the intermediate value
def intermediate(pt, keyguess):
    return sbox[pt ^ keyguess]
###########################################################################

################## DON'T TOUCH: Import Data ###############################
##  Traces, plaintexts, knownkey
trace_array = np.load(r'./traces/2018.11.24-21.52.36_traces.npy')
plaintexts = np.load(r'./traces/2018.11.24-21.52.36_textin.npy')
# We will use the knownkey for sanity checking. In an actual attack, we do not know its value.
knownkey = np.load(r'./traces/2018.11.24-21.52.36_knownkey.npy')
###########################################################################

################## DON'T TOUCH: Input Parameters #########################
# Number of Traces and plaintexts
numTraces=1000
#Number of samples/points in each trace
numSamples=3000
## Choose a key byte to guess (We will use byte 0)
bnum = 0;
plaintext_array = np.zeros(numTraces, dtype=np.ubyte)
plaintext_array = plaintexts[0:numTraces,bnum]
###########################################################################


# Step 3: Compute the hypothetical intermediate values
#         for each key guess

# Step 3a: Create the hypothetical intermediate value matrix
intermediate_val_array = np.zeros((256, numTraces),dtype=np.ubyte)
# Step 3b: Fill the array for each [key-guess] and [plaintext] 

# YOUR CODE
# YOUR CODE
# YOUR CODE



############# DISTINGUISHER (DON'T TOUCH BELOW THIS LINE) ###################
# Step 4: Compute the hypothetical power consumption values
# for each key-guess and plaintext byte
# Use hw[] array (given above) to compute Hamming Weight

# Step 4a: Create the hypothetical intermediate value matrix
hyp_pwr_array = np.zeros((256, numTraces),dtype=np.ubyte)
# Step 4b: Fill the array for each [key-guess] and [plaintext]
for kguess in range(0, 256):
	for tnum in range (0, numTraces):
		hyp_pwr_array[kguess][tnum] = hw[intermediate_val_array[kguess][tnum]] # YOUR CODE
###########################################################################

################# Your code starts here ###################
# Step 4: Compute the correlation coefficients
# between the actual power traces and the hypothetical power values
# step 4a: create a 2D array to keep the correlation trace for each key guess
corrcoeff_array = np.zeros((256,numSamples))

#Step 4b: Compute the correlation trace
for kguess in range(0, 256):
	for snum in range (0, numSamples):
			
		corrcoeff_array[kguess, snum] = np.corrcoef(hyp_pwr_array[kguess][0:numTraces], trace_array[0:numTraces, snum])[0][1] # YOUR CODE
	# Absolute value
	corrcoeff_array[kguess,:] = np.abs(corrcoeff_array[kguess,:])
	### DONT'T TOUCH: test code ##########################################
	if(kguess == knownkey[0]):
		plt.plot(np.abs(corrcoeff_array[kguess,:]), 'r', label=('correct_key (kguess = 0x%x)'%knownkey[0]))
	elif(kguess == 0):
		plt.plot(np.abs(corrcoeff_array[kguess,:]), 'k--', label='wrong_keys (all of the remaining key guesses)')
	else:
		plt.plot(np.abs(corrcoeff_array[kguess,:]), 'k--')
	print "key-byte %d, key-guess %d, score = %f \n" % (0,kguess, max(corrcoeff_array[kguess,:]))


# abs of coefficients
corrcoeff_array = np.abs(corrcoeff_array)

#Ranking the key guesses for each key byte
max_corrcoeff_array = np.zeros((256))
for kguess in range(0, 256):
	max_corrcoeff_array[kguess] = max(corrcoeff_array[kguess,:])
	
sorted_kguess_array = np.zeros((256))
sorted_kguess_array = np.argsort(max_corrcoeff_array)[::-1]

best_guess = sorted_kguess_array [0]


# Rank of the known key 
rank_known_key = list(sorted_kguess_array).index(knownkey[bnum])
	
# Print guesses vs. known key bytes
print "\n Results: \n"
#print "guessed key-byte value : 0x%x      actual key-byte value: 0x%x    \n" % (best_guess, knownkey[0])
print "guessed key-byte value : %d      actual key-byte value: %d    \n" % (best_guess, knownkey[0])

	

