# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as hist
import csv
"""
Created on Tue Nov 29 19:17:08 2016

@author: Amani
"""

internal_urls = {}
external_urls = {}
def read_csv_as_dictionary(file_name):
    read_dictionary = {}
    for key, val in csv.reader(open(file_name)):
        read_dictionary[key] = val
    return read_dictionary
                 
def counting_dictionary(url_dictionary):
    count_urls = dict()
    for key, value in url_dictionary.items():
        count_urls[key] = len(value)
    return count_urls
# sum of values and number of keys
def sum_link(count_dict):
    sum_of_values = 0
    number_of_keys = 0
    for key, value in count_dict.items():
        number_of_keys += 1
        sum_of_values += value
    return (number_of_keys, sum_of_values)


# page_link gives the urls with number of links
def mean(page_links):
   values = sum_link(page_links)
   mean_links = values[1] / values[0]
   return mean_links
     
   
#function for caluculating median
def median(page_link):
      sort_list= sorted(page_link.values())
      length = len(sort_list)
      median_pos = length // 2
     
      if length % 2 == 0:
          median = (sort_list[median_pos - 1] + 
                    sort_list[ ( median_pos) ]) / 2
          return median
      else:
         median = sort_list[median_pos]
         return median
#Number of internal links
def add_data(data_dict1, data_dict2):
    added_dict  = {}
    for key, values in data_dict1.items():
        added_dict[key] = data_dict1[key] + data_dict2[key]
    return added_dict
def scaterring_graph(array_x,array_y):
    plt.plot(array_x,array_y, 'bo')
    plt.title('Scatter graph to number of internal links and external links values')
    plt.xlabel('internal links')
    plt.ylabel('external links')
    return plt
    
if __name__ == '__main__':
    
#Reading the data from csv files assigned to string variables
      internal_link_file = 'internal_urls.csv'
      external_link_file = 'external_urls.csv'
#Assign the variables to read csv fiels
      internal_urls = read_csv_as_dictionary(internal_link_file)
      external_urls = read_csv_as_dictionary(external_link_file)
      external_urls_count = counting_dictionary(external_urls)
      internal_links_count = counting_dictionary(internal_urls)
      sum_of_urls = add_data(internal_links_count, external_urls_count)
#Printing the number of internal links
      print('total number of url encountered')
      total_urls_encountered = len(sum_of_urls.keys())
      print(sum_link(sum_of_urls)[0])
# Printing the number of externl links

#Printing total number of urls
     

      
      
      
      print('toal number of links encountered')
      print(sum_link(sum_of_urls)[1])

#Printing the number mean and median of the links per webpage
      internal_link_x = [value for (key, value) in sorted(internal_links_count.items())]
      external_link_y = [value for (key, value) in sorted(external_urls_count.items())]
      plt1 = scaterring_graph(internal_link_x, external_link_y)
      plt1.show()
      print('average number of url')
      print(mean(sum_of_urls))
      print('median number of url')
      print(median(sum_of_urls))
#Ploting the scatterring graph

    
#printing the histogram
      data = list(sum_of_urls.values())
      d = plt.hist(data, bins = 30)
      plt.show()
