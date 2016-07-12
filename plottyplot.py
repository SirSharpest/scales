# Imports 
import matplotlib.pyplot as plt
import numpy as np

# Read a csv file and return the elements as an array 
def readCSV(fname, sep=","):
	values = []
	fh = open(fname)
	for line_no, line in enumerate(fh):
		if line[0] == "#" or len(line.strip()) == 0:
			continue
		fields = line.strip().split(sep)
		try:
			values.append(float(fields[0]))
		except IndexError:
			print("Failed to append value from line %d of %s" % (line_no, fname))	
	return values

# Create numpy array of the two csv files 
temp_vals = np.array(readCSV("temp.csv"))
weight_values = np.array(readCSV("weight.csv"))

# The length that each array should aim to be (to make happy plotting)
target_length = max(len(temp_vals), len(weight_values))


weight_positions = np.linspace(0, target_length, len(weight_values))
weight_vals = np.interp(range(target_length), weight_positions, weight_values)

# Normalise temp values 
temp_vals -= min(temp_vals)
temp_vals /= max(temp_vals)

# Normalise weight values 
weight_vals -= min(weight_vals)
weight_vals /= max(weight_vals)

# Plot everything! 
plt.plot(range(target_length), temp_vals)
plt.plot(range(target_length), weight_vals)
plt.show()
