# -*- coding: utf-8 -*-
import numpy as np
import csv
"""
Created on Tue Nov 29 19:17:08 2016

@author: Amani
"""
def dict_to_sorted_lists(freq):
  ys = []
  for x in xs:
    ys.append(freq[x])
  return [xs, ys]

def cumulate_freq(freq_array):
  ys = freq_array[1]
  for iter in range(len(ys) - 1):
    ys[iter + 1] = ys[iter] + ys[iter + 1]
  return [freq_array[0], ys]


def cdf(cumulated_freq_array):
  ys = cumulated_freq_array[1]
  length = len(ys)
  max_val = ys[length - 1]
  cumul_ys = [(val / max_val) for val in ys]
  return [cumulated_freq_array[0], cumul_ys]

def median_of_freq(freq):
  xs_ys = dict_to_sorted_lists(freq)
  cum_xs_ys = cumulate_freq(xs_ys)
  cdf_xs_ys = cdf(cum_xs_ys)

  cdf_ys = cdf_xs_ys[1]
  for iter in range(len(cdf_ys)):
    if cdf_ys[iter] >= 0.5:
      return cdf_xs_ys[0][iter]



if __name__ == '__main__':
  a = { 26:21, 4:10, 43:4 }
  b = dict_to_sorted_lists(a)
  c = cumulate_freq(b)
  cdfs = cdf(c)
  med = median_of_freq(a)
  print(med)
  print(cdfs)
