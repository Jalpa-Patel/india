import numpy as np
import matplotlib.pyplot as plt
# rolls 2 dices simultaneously
# input:
#   no_of_times: Integer - no of times to roll the dice
# output:
#   Integer - sum of both dices' outputs
def roll_2_die(no_of_times):
  die_1 = np.random.random_integers(1, 6, no_of_times)
  die_2 = np.random.random_integers(1, 6, no_of_times)
  return die_1 + die_2

# finds maximum pointwise distance
def find_norm(y1, y2):
  small_list_size = min(y1.shape[0], y2.shape[0])
  return np.max(np.abs(np.subtract
  (y1[:small_list_size], y2[:small_list_size])))

# finds the median sum of two dice sides
def get_median(x, y):
  return x[np.min(np.where(y >= 0.5))]

# finds the probability of dice sum to be <= to the required number
#given by prob passed here
def get_prob(x,y, prob):
  x_index = np.max(np.where(x <= prob))
  return y[x_index]#[x[np.max(np.where(x < 0.5))],np.max(y[np.where(x <=0.5)])
if __name__ == "__main__":
  dice_sum_output = roll_2_die(100)
  plt.title(
  "cumulated plots of Rank frequency plot of throwing two dice")
  plt.xlabel('dice output')
  plt.ylabel('Frequency')
  y = plt.hist(dice_sum_output, bins=11,normed= True, cumulative= True,
  histtype= "step", label="n=100" )
  a = get_median(y[1], y[0])
  print("median for n =100")
  print(a)
  x_9 = get_prob(y[1],y[0], 9)
  print("value of p <= 9 for n = 100")
  print(x_9)
  y1 = y[0]
  plt.plot([a , a],[0, .5],"m--",label = "median n=100")
  plt.plot([9 , 9],[0,x_9],"k--",label = "p < 9 n=100")
  dice_sum_output = roll_2_die(1000)
  y = plt.hist(dice_sum_output, bins=11,normed= True, cumulative= True,
  histtype= "step", label="n=1000" )
  print("median for n =1000")
  a = get_median(y[1], y[0])
  print(a)
  x_9 = get_prob(y[1],y[0], 9)
  print("value of p <= 9 for n = 1000")
  print(x_9)
  y2 = y[0]
  plt.plot([a , a],[0, .5],"y-",label = "median n=1000")
  plt.plot([9 , 9],[0,x_9],"r-",label = "p < 9 n=1000")
  plt.legend(fontsize = 8, framealpha = 0.85 )
  print("maximum pointwise distance")
  smirnov = find_norm(y1,y2)
  print(smirnov)
plt.show()