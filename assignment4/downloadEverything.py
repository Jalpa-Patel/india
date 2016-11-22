import re
from http_client import parse_url
def read_data(file_name):
  with open(file_name, 'r') as f:
     data = f.read()
  return data


def match_img_src(html):
  img_pattern = '<img.*?src="([^"]*)"'
  return re.findall(img_pattern, html)


def make_absolute_url(url_list, url):
  parse_url(url)
  parsed_url = []
  for url in url_list:
    parsed_url.append( parse_url(url_list))
  return parsed_url



def print_all_url_links(file_name):
  html_data = read_data(file_name)
  url_list = match_img_src(html_data)
  print(url_list)
  return url_list

file_name = '/home/jass/WebScience/india/assignment4/introduction-to-web-science.html'
url = "http://west.uni-koblenz.de/en/studying/courses/ws1617/introduction-to-web-science"

url_list = print_all_url_links(file_name)

parsed_url = make_absolute_url(url_list, url)
print(parsed_url)
