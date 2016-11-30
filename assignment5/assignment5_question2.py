import http_client
import csv
from collections import deque
import sys
import re
#import downloadEverything
import http_client

queue = deque()
traversed_set = set()
external_urls = {}
internals_urls = {}
domain =  "http://141.26.208.82/"

def find_all_links(file_name):
  with open(file_name, 'r') as f:
    html = f.read()
  href_pattern = 'href=[\'"]?([^\'" >]+)'
  return re.findall(href_pattern, html)

def if_relative_url(url):
  parse_url = http_client.parse_url(url)
  if(parse_url.netloc):
    return False
  else:
    return True

def make_absolute_url(relative_url):
  relative_url = http_client.parse_url(relative_url).path
  return "".join([domain,relative_url] )

def add_value_to_queue(value):
  if value not in traversed_set:
    queue.append(value)
    traversed_set.add(value)

def process_queue():
  return queue.popleft()

def crawl(start_url):
  add_value_to_queue(start_url)
  i = 0
  while(len(queue)):
    if(i%25 == 0 ):
       print('crawling\t' + str(i) + ' th page')
    i = i +1

    url_to_be_crawled = process_queue()
    print("\ncarwaling url\n" + url_to_be_crawled)
    output = http_client.call_http_server(url_to_be_crawled, False)
    if output[0] == True:
      urls = find_all_links(output[1])
      for url in urls:
        if(if_relative_url(url)):
          absolute_url = make_absolute_url(url)
          url_list = internals_urls.get(url_to_be_crawled, [])
          add_value_to_queue(absolute_url)
          url_list.append(absolute_url)
          internals_urls[url_to_be_crawled] = url_list
        else:
          url_list = external_urls.get(url_to_be_crawled, [])
          url_list.append(url)
          external_urls[url_to_be_crawled] = url_list
  write = csv.writer(open("internal_urls.csv", "w"))
  for key, val in internals_urls.items():
    write.writerow([key, val])
  write = csv.writer(open("external_urls.csv", "w"))
  for key, val in internals_urls.items():
    write.writerow([key, val])


if __name__ == '__main__':
  start_url = "http://141.26.208.82/articles/g/e/r/Germany.html"
  crawl(start_url)

