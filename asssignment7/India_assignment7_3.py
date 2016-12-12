import numpy as np
import matplotlib.pyplot as plt
def roll_2_die(no_of_times):
  die_1 = np.random.random_integers(1, 6, no_of_times)
  die_2 = np.random.random_integers(1, 6, no_of_times)
  return die_1 + die_2

def get_median(x, y):
  return x[np.max(np.where(y <= 0.5))]
def get_prob(x,y, prob):
  x_index = np.max(np.where(x <= prob))
  return y[x_index]#[x[np.max(np.where(x < 0.5))],np.max(y[np.where(x <=0.5)])
if __name__ == "__main__":
  dice_sum_output = roll_2_die(100)
  plt.title(
  "cumulated plots of Rank frequency plot of throwing two dice")
  plt.xlabel('dice output')
  plt.ylabel('p(Frequency >= n)')
  y = plt.hist(dice_sum_output, bins=11,normed= True, cumulative= True,
  histtype= "step", label="first try" )
  dice_sum_output = roll_2_die(1000)
  y = plt.hist(dice_sum_output, bins=11,normed= True, cumulative= True,
  histtype= "step", label="second try" )
  a = get_median(y[1], y[0])
  print(a)
  x_9 = get_prob(y[1],y[0], 9)
  print(x_9)
  #plt.legend(fontsize = 8, framealpha = 0.85 )
  #plt.show()
