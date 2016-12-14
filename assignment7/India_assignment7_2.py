#@author: Jasvinder
import probabilities as prob
import India_process_data as data
import numpy as np
import matplotlib.pyplot as plt
import os.path
# samples n characters from the distribution
#input:
#   probalities: Dictionary - required data to be sampled
#   n: Integer: - No of characters to be sampled
#output:
#   String - generated value after sampling
def sample_n_times(probabilities, n):
  chars = list(probabilities.keys())
  prob =  [probabilities[char] for char in chars]
  return "".join(np.random.choice(chars, n, p = prob))

# finds maximum pointwise distance of the Cdfs
# input:
#   Cdfs of the two generated texts
# output:
#    Integer - maximum pointwise distance
def find_norm(y1, y2):
  small_list_size = min(y1.shape[0], y2.shape[0])
  return np.max(np.abs(np.subtract
  (y1[:small_list_size], y2[:small_list_size])))

# finds the word rank frequency
# input:
#   word frequency in file
# output:
#   rank of the word frequency
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

    generated_string = sample_n_times(prob.uniform_probabilities, total_chars)

    if not os.path.isfile(generated_file_1):
      with open(generated_file_1, "w") as file:
        file.write(generated_string)
    generated_string = sample_n_times(prob.zipf_probabilities, total_chars)
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
  plt.show()

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
  plt.show()

  smirnov_uniform = find_norm(cdf_y_wiki, cdf_y_g1)
  smirnov_zipf = find_norm(cdf_y_wiki, cdf_y_g2)
  print("Kolmogorov Smirnov test for g1")
  print(smirnov_uniform)
  print("Kolmogorov Smirnov test for g2")
print( smirnov_zipf)