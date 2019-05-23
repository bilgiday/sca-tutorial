import numpy as np
import matplotlib.pyplot as plt

################## DON'T TOUCH: Import Data ###############################
### Import the input data
##  Traces, plaintexts, knownkey
trace_array = np.load(r'./traces/2018.11.24-21.52.36_traces.npy')
plaintext_array = np.load(r'./traces/2018.11.24-21.52.36_textin.npy')
###########################################################################

################# DON'T TOUCH: Examining the input data ###################
# Plot a trace and examine it 
# Hint: matplotlib.pyplot
plt.plot(trace_array[0])
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.title ("Power Trace for Plaintext 0")
plt.show()

# Dimensions of the trace array and plaintext array
print("\nDimensions of Trace Array\n")
print (np.shape(trace_array))
# How many traces do we have?
numTraces= 0 #<YOUR ANSWER>
# How many samples does each trace contain?
numSamples= 0 #<YOUR ANSWER>


print("\n\nDimensions of Plaintext Array\n")
print(np.shape(plaintext_array))
# How many plaintexts do we have?
numPTs = 0 #<YOUR ANSWER>
# How many bytes does each plaintexts contain?
numPTBytes = 0 #<YOUR ANSWER>

###########################################################################

	

