#it replaces all dots,commas etc in the file by spaces and takes o(n)
import India_stats as stat
import matplotlib.pyplot as plt
import sys
def word_frequency_in_article(file_name):
  article_list = []
  article_hash = {}
  with open(file_name,'r') as file:
    for line in file:
      ##article_list extracted by code for extracting article
      #articles_count
      article_hash = read_and_countwords(line)
      line = line.strip()
      if line:
        article_list.append(article_hash)
  return article_list
def article_lengths(file_name):
  length_of_article = []
  with open(file_name, 'r') as file:
    for line in file:
      line = line.strip()
      if line:
        length_of_article.append(len(line))
  return length_of_article

def read_and_countwords(text):
  words_count = {}
  text.strip()
  cleandot_data = text.replace('.',' ')
  cleancomma_data = cleandot_data.replace(',',' ')
  cleanbracket1_data = cleancomma_data.replace('(',' ')
  cleanbracket2_data = cleanbracket1_data.replace(')',' ')
  cleancolon_data = cleanbracket2_data.replace(':',' ')
  cleanspace_data = cleancolon_data.replace(' ',' ')
  cleanquotes_data = cleanspace_data.replace('"',' ')
  word_list = cleanquotes_data.split()
  words_count = count_length_of_words_in_list(word_list)
  return words_count


#it returns the count of the word from the given list
def count_length_of_words_in_list(word_list):
  frequency_of_word_size = {}
  for word in word_list:
    length_of_word = len(word)
    frequency_of_word_size[length_of_word] = frequency_of_word_size.get(length_of_word, 0) + 1
  return frequency_of_word_size
if __name__ == '__main__':
  if len(sys.argv) > 1:
    filename_to_be_read = sys.argv[1]
  else:
    filename_to_be_read = '/home/jass/Documents/jass/WebScience/india/assignment6/simple-20160801-1-article-per-line'
  article_hash_list = word_frequency_in_article(filename_to_be_read)
  medians = [stat.median_of_freq(article_hash)
  for article_hash in article_hash_list]
  length = article_lengths(filename_to_be_read)
  plt.title('Length vs median word length scatter plot')
  plt.xlabel('length')
  plt.ylabel('median')
  plt.xscale('log')
  plt.yscale('log')
  plt.plot(length, medians, 'ro')
  plt.show()
  maxs = [max(article_hash.keys())
  for article_hash in article_hash_list]
  plt.plot(length, maxs, 'bx')
  plt.title('Length vs max word length scatter plot')
  plt.xlabel('length')
  plt.ylabel('max')
  plt.xscale('log')
  plt.yscale('log')
  plt.show()