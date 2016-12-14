def get_freq(word_list):
  frequency_of_word_size = {}
  for word in word_list:
    frequency_of_word_size[word] = frequency_of_word_size.get(word, 0) + 1
  return frequency_of_word_size

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
  words_count = get_freq(word_list)
  return words_count

def word_frequency_in_file(file_name):
  with open(file_name,encoding="utf-8") as file:
    return read_and_countwords(file.read())


def count_chars_and_spaces(file_name):
  count_chars_and_spaces = 0
  with open(file_name, encoding="utf-8") as file:
    data = file.read()
  for char in data:
    if char.isalpha() or char.isspace():
      count_chars_and_spaces += 1
  return count_chars_and_spaces


if __name__ == "__main__":
a =count_chars_and_spaces("simple-20160801-1-article-per-line")