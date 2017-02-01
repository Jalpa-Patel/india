import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt

def cum_sum(given_array):
  array_after_cumsum = []
  array_after_cumsum = np.cumsum(given_array)
  return array_after_cumsum

# x = given array
# y = cumsum array of array x
def gini_coefficient(x, y):
  diff = 0
  for i in x:
    for j in x:
      diff+= np.abs(np.subtract(i,j))
  denominator = 2*len(y)*y[-1]
  gini_value = diff/denominator
  return gini_value

if __name__ == "__main__":
  with open('network_1000.json') as json_data:
    sample_array = json.load(json_data)
  gini_array = []
  gini_arrays = []
  fig = plt.figure()
  for array_in_array in sample_array:
    for current_array in array_in_array:
      cumsum_dataset = cum_sum(current_array)
      gini_output = gini_coefficient(current_array, cumsum_dataset)
      gini_array.append(gini_output)
    gini_arrays.append(gini_array)

    gini_array = []
  print(gini_arrays[0])
  plt.plot([200,400,600,800,1000], gini_arrays[0], 'b-')
  plt.plot([200,400,600,800,1000], gini_arrays[1], 'b--')
  plt.plot([200,400,600,800,1000], gini_arrays[2], 'r-')
  plt.plot([200,400,600,800,1000], gini_arrays[3], 'r--')
  plt.plot([200,400,600,800,1000], gini_arrays[4], 'g-')
  plt.legend()
  plt.title("Gini coefficient plot")
  plt.xlabel("Customers")
  plt.ylabel("Gini coefficient G")
  fig.savefig("gini.png", transparent=True, bbox_inches='tight', pad_inches=0)
  plt.show()

  print('Gini coefficient for 200,400,600,800,1000 customers respectively are',gini_array)