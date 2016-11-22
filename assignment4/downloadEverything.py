import re
import sys
import http_client

# Reads the file saved at the file name and returns the data.
# input:
#   file_name:String - name of the fiel to be read.
#output:
#    String: Data from the file.
def read_data(file_name):
  with open(file_name, 'r') as f:
     data = f.read()
  return data


# finds the src from the img tag in full html string..
# input:
#   html:String - HTML data as strings
#output:
#    List: list of urls from image tags src.
def match_img_src(html):
  img_pattern = '<img.*?src="([^"]*)"'
  return re.findall(img_pattern, html)


# Converts the relative urls from url list to complete http urls.
# input:
#   url_list:List - URL list as list of string.
#   url: String- Url of main page from where html was downloaded.
#output:
#    List - List of complete http url.
def make_absolute_url(url_list, url):
  downloaded_domain = http_client.parse_url(url).netloc
  complete_url = []
  for url in url_list:
    parsed_url = http_client.parse_url(url)
    if(parsed_url.netloc):
      complete_url.append(url)
    else:
      complete_url.append('http://' + downloaded_domain + url )
  return complete_url

# Reads the html files extracts all html links to image and download it and saves it to the disc and prints all the URLs at the console.
# input:
#   file_name - Name of the file in which html page is saved-
#   url:String - Url of the resource from where main file was  downloaded.
#output:
#    None
def download_urls(file_name, url):
  html_data = read_data(file_name)
  url_list = match_img_src(html_data)
  full_url_list = make_absolute_url(url_list, url)
  print('List of URLs extracted from downloaded html')
  print(full_url_list)
  for url in full_url_list:
    print('\ndownloading url')
    http_client.call_http_server(url, False)

if __name__ == "__main__":
  download_urls(sys.argv[1], sys.argv[2])
