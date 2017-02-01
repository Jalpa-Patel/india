import numpy as np
import matplotlib.pyplot as plt
import csv
file_name = "onlyhash.data"
def read_data():
  user_tweets = {}
  system_tweets = {}
  with open(file_name, newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for tweet_info in reader:
      name = tweet_info[0]
      date = tweet_info[1]
      hash_tag = tweet_info[2]
      if date not in system_tweets:
        system_tweets[date] = {'total': 0}
      system_tweets[date][hash_tag] = system_tweets[date].get(hash_tag, 0) + 1
      system_tweets[date]['total'] += 1
      if date not in  user_tweets:
        user_tweets[date] = {}
      if name not in user_tweets[date]:
        user_tweets[date][name] = {"total": 0}
      user_tweets[date][name][hash_tag] = user_tweets[date][name].get(hash_tag, 0) + 1
      user_tweets[date][name]["total"] += 1
  return (user_tweets, system_tweets)

def calculate_average_user_entropy(user_tweets):
  entropy = {}
  daily_average_entropy = {}
  probability = 0
  no_of_user = 0
  for date, user_hash_tags in user_tweets.items():
    daily_average_entropy[date] = 0
    for user, hash_tags in user_hash_tags.items():
      entropy[user] = 0
      for hash_tag, tweet_count in hash_tags.items():
        probability = tweet_count/hash_tags['total']
        entropy[user] += probability * np.log(probability)
      entropy[user] *= -1
    for user, user_entropy in entropy.items():
      daily_average_entropy[date] += user_entropy
    no_of_user = len(entropy.keys())
    daily_average_entropy[date] /= no_of_user
  return  daily_average_entropy

def calculate_average_system_entropy(system_tweets):
  probability = 0
  daily_entropy = {}
  probability = 0

  for date, hash_tags in system_tweets.items():
    daily_entropy[date] = 0
    for hash_tag, tweet_count in hash_tags.items():
      probability = tweet_count/ hash_tags['total']
      daily_entropy[date] += probability * np.log(probability)
    daily_entropy[date] *= -1
  return daily_entropy
def plot_entropy():
  data = read_data()
  user_entropy = calculate_average_user_entropy(data[0])
  system_entropy = calculate_average_system_entropy(data[1])
  dates = sorted(user_entropy.keys())
  x = [user_entropy[d] for d in dates]
  y = [system_entropy[d] for d in dates]
  fig = plt.figure()
  plt.plot(x, y, 'o', c='blue', alpha=0.8, markeredgecolor='none')
  plt.legend()
  plt.title("Entropy scatter plot")
  plt.xlabel("User Entropy")
  plt.ylabel("System Entropy")
  fig.savefig("entropy.png", transparent=True, bbox_inches='tight', pad_inches=0)
  plt.show()

plot_entropy()


