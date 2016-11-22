import re
import sys
import http_client
def read_data(file_name):
  with open(file_name, 'r') as f:
     data = f.read()
  return data


def match_img_src(html):
  img_pattern = '<img.*?src="([^"]*)"'
  return re.findall(img_pattern, html)


def make_absolute_url(url_list, url):
  downloaded_domain = http_client.parse_url(url).netloc
  complete_url = []
  for url in url_list:
    parsed_url = http_client.parse_url(url)
#    parsed_url.append(http_client.parse_url(url_list))
    if(parsed_url.netloc):
      complete_url.append(url)
    else:
      complete_url.append('http://' + downloaded_domain + url )
  return complete_url



def print_all_url_links(file_name):
  html_data = read_data(file_name)
  url_list = match_img_src(html_data)
  return url_list


def download_urls(file_name,url):
  url_list = print_all_url_links(file_name)
  full_url_list = make_absolute_url(url_list, url)
  print(full_url_list)
  for url in full_url_list:
    http_client.http_server(url, False)




if __name__ == "__main__":
  download_urls(sys.argv[1], sys.argv[2])