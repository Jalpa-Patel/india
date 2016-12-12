#@author: Jasvinder

zipf_probabilities = {' ': 0.17840450037213465, '1': 0.004478392057619917, '0': 0.003671824660673643, '3': 0.0011831834225755678, '2': 0.0026051307175779174, '5': 0.0011916662329062454, '4': 0.0011108979455528355, '7': 0.001079651630435706, '6': 0.0010859164582487295, '9': 0.0026071152282516083, '8': 0.0012921888323905763, '_': 2.3580656240324293e-05, 'a': 0.07264712490903191, 'c': 0.02563767289222365, 'b': 0.013368688579962115, 'e': 0.09688273452496411, 'd': 0.029857183586861923, 'g': 0.015076820473031856, 'f': 0.017232219565845877, 'i': 0.06007894642873102, 'h': 0.03934894249122837, 'k': 0.006067466280926215, 'j': 0.0018537015877810488, 'm': 0.022165129421030945, 'l': 0.03389465109649857, 'o': 0.05792847618595622, 'n': 0.058519445305660105, 'q': 0.0006185966212395744, 'p': 0.016245321110753712, 's': 0.055506530071283755, 'r': 0.05221605572640867, 'u': 0.020582942617121572, 't': 0.06805204881206219, 'w': 0.013964469813783246, 'v': 0.007927199224676324, 'y': 0.013084644140464391, 'x': 0.0014600810295164054, 'z': 0.001048859288348506}

uniform_probabilities = {' ': 0.1875, 'a': 0.03125, 'c': 0.03125, 'b': 0.03125, 'e': 0.03125, 'd': 0.03125, 'g': 0.03125, 'f': 0.03125, 'i': 0.03125, 'h': 0.03125, 'k': 0.03125, 'j': 0.03125, 'm': 0.03125, 'l': 0.03125, 'o': 0.03125, 'n': 0.03125, 'q': 0.03125, 'p': 0.03125, 's': 0.03125, 'r': 0.03125, 'u': 0.03125, 't': 0.03125, 'w': 0.03125, 'v': 0.03125, 'y': 0.03125, 'x': 0.03125, 'z': 0.03125}


import India_process_data as data
import numpy as np
import matplotlib.pyplot as plt
import os.path

#input: probalities
#output:
#def sample_character(probabilities):
#  x_y_list = stats.dict_to_sorted_lists(probabilities)
#  probability_space = stats.cumulate_freq(x_y_list)
#  random_number = random.random()
#  for iter in range(len(probability_space[1])):
#    if random_number <= probability_space[1][iter]:
#      return probability_space[0][iter]

def sample_n_times(probabilities, n):
  chars = list(probabilities.keys())
  prob =  [probabilities[char] for char in chars]
  return "".join(np.random.choice(chars, n, p = prob))

def find_norm(y1, y2):
  small_list_size = min(y1.shape[0], y2.shape[0])
  return np.max(np.abs(np.subtract
  (y1[:small_list_size], y2[:small_list_size])))

def rank_freq(freq):
    points = [(k,v) for k, v in freq.items()]
    dtype = [('x', 'unicode'), ('y', int)]
    np_points = np.array(points, dtype = dtype)
    np_points['y'] *= -1
    sorted_freq = np.sort(np_points, order='y')
    sorted_freq['y'] *= -1
    return sorted_freq
if __name__ == '__main__':
  generated_file_1 = "generated_1.txt"
  generated_file_2 = "generated_2.txt"
  wikipedia_file = "simple-20160801-1-article-per-line"
  if not os.path.isfile(generated_file_1) or not os.path.isfile(generated_file_2):
    total_chars = data.count_chars_and_spaces(wikipedia_file)

    generated_string = sample_n_times(uniform_probabilities, total_chars)

    if not os.path.isfile(generated_file_1):
      with open(generated_file_1, "w") as file:
        file.write(generated_string)
    generated_string = sample_n_times(zipf_probabilities, total_chars)
    if not os.path.isfile(generated_file_2):
      with open(generated_file_2, "w") as file:
        file.write(generated_string)
  plt.title(
  "plot of Rank vs frequency  of wiki and two generated texts.")
  plt.xlabel('Rank')
  plt.ylabel('freq')

  fre = data.word_frequency_in_file(wikipedia_file)
  y_wiki = rank_freq(fre)['y']
  x_wiki = np.arange(1, len(y_wiki) + 1, 1)
  red_line, = plt.loglog(x_wiki, y_wiki,"r-", label="simple english wikipedia")

  fre = data.word_frequency_in_file(generated_file_1)
  y_g1 = rank_freq(fre)['y']
  x_g1 = np.arange(1, len(y_g1) + 1, 1)
  blue_line, = plt.loglog(x_g1, y_g1,"b-", label="uniform probability generated")

  fre = data.word_frequency_in_file(generated_file_2)
  y_g2 = rank_freq(fre)['y']
  x_g2 = np.arange(1, len(y_g2) + 1, 1)
  green_line, = plt.loglog(x_g2, y_g2, "g-", label="zipf probability generated")
  plt.legend(handles=[red_line, blue_line, green_line],
  fontsize = 8, framealpha = 0.85, frameon = True )
  #plt.show()

  plt.title(
  "cumulated plots of Rank frequency plot of wiki and two generated texts.")
  plt.xlabel('Rank')
  plt.ylabel('p(Frequency >= n)')

  csum_y_wiki = np.cumsum(y_wiki)
  cdf_y_wiki = csum_y_wiki/np.max(csum_y_wiki)

  red_line, = plt.plot(x_wiki, cdf_y_wiki, "r-",
  label="simple english wikipedia")

  csum_y_g1 = np.cumsum(y_g1)
  cdf_y_g1 = csum_y_g1 / np.max(csum_y_g1)

  blue_line, = plt.plot(x_g1, cdf_y_g1, "b-", label="uniform probab")
  plt.xscale('log')

  csum_y_g2 = np.cumsum(y_g2)
  cdf_y_g2 = csum_y_g2 / np.max(csum_y_g2)

  green_line, = plt.plot(x_g2, cdf_y_g2, "g-", label="zipf probab")
  plt.xscale('log')

  plt.legend( handles = [red_line, blue_line, green_line],
  fontsize = 8, framealpha = 0.85, frameon = True )
  #plt.show()

  smirnov_uniform = find_norm(cdf_y_wiki, cdf_y_g1)
  smirnov_zipf = find_norm(cdf_y_wiki, cdf_y_g2)
  print("Kolmogorov Smirnov test for g1")
  print(smirnov_uniform)
  print("Kolmogorov Smirnov test for g2")
  print( smirnov_zipf)
