import socket
from urllib.parse import urlparse
import sys
__author__ = "jasvinder"


# creates an INET, STREAMING socket
# input:
#   url:String - takes the valid url to make tcp connection
#   port: Integer - take the port number to connect
# output:
#   TCPSocket - returns a tcp socket object for further communication.
def tcp_connection(url, port):
  clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  clientSocket.connect((url, port))
  return clientSocket

# Parses the URL into six components.i.e scheme, network location, path, parameters, query and fragment
# input:
#   url_name:String - takes the valid url passed
# output:
#   String - parsed Url into 6 components
def parse_url(url_name):
  return urlparse(url_name)

# User request for sending user input URL as HTTP request ending with two empty lines
# input:
#   url_name:String - takes the valid url passed
#   method_type:String - takes Http method type,i.e generally, POST or GET
# output:
#   get_request:String - returns the valid Http Request according to method type
def encode_http_request(path, method_type):
  protocol_type = 'HTTP/1.0'
  get_request = ''.join([method_type,' ', path,' ',protocol_type, '\r','\n','\r','\n'])
  return get_request

# Sends the Http Request
# input:
#   tcp_connection:TCP Socket object - takes the object of the TCP connection established
#   http_request:String - takes the valid Http Request according to method type i.e GET or POST method
# output:
#   Bytes: returns the Http request made in bytes to send it further for communication
def send_http_request(tcp_connection, http_request):
  return tcp_connection.send(str.encode(http_request))

# Reads the Http header of the response
# input:
#   tcp_connection:TCP Socket object - takes the object of the TCP connection established
#output:
#   http_headers: String - gives the HTTP header of the response
def read_http_header(tcp_connection):
  http_headers = []
  while(True):
    response = tcp_connection.recv(1).decode('utf-8')
    if(response == '\r'):
      http_headers.append(response)
      response = tcp_connection.recv(3).decode('utf-8')
      if(response == '\n\r\n'):
        http_headers.append(response)
        break
      else:
        http_headers.append(response)

    else:
      http_headers.append(response)
  return ''.join(http_headers)

# Reads the body of the Http response
# input:
#   tcp_connection:TCP Socket object - takes the object of the TCP connection established
#output:
#    total_http_response_data: array - gives the http body of the response, as text

def receive_http_body_as_text(tcp_connection):
  total_http_response_data = []
  http_response = tcp_connection.recv(512).decode('utf-8')
  total_http_response_data.append(http_response)
  while(http_response):
    http_response = tcp_connection.recv(512).decode('utf-8')
    total_http_response_data.append(http_response)
  return ''.join(total_http_response_data)

# Reads the body of the Http response
# input:
#   tcp_connection:TCP Socket object - takes the object of the TCP connection established
#output:
#   http_body: array - gives the body of the Http response, as binary data
def read_http_body_as_binary(tcp_connection):
  http_body = []
  response = tcp_connection.recv(1024)
  while(response):
    http_body.append(response)
    response = tcp_connection.recv(1024)
    #http_body.append(response)
  return http_body

def decode_http_header(http_header):
  return http_header.strip().split('\r\n')

def find_content_type(decoded_http_header):
  #print(decoded_http_header)
  for value in decoded_http_header:
    if(value.startswith('Content-Type:')):
      if(value.startswith('Content-Type: text/html')):
        return 'text'
      else:
        return 'binary'


def save_text_data(string_data_to_be_written, file_name):
  with open(file_name, 'w+') as file:
    file.write(string_data_to_be_written)

def save_binary_data(binary_data_array_to_be_written, file_name):
    #binary_data_to_be_written = str.encode(string_data_to_be_written)
    with open(file_name, 'bw') as file:
      for value in binary_data_array_to_be_written:
        file.write(value)



#Sending data from client to server
def http_server(url_name, saveheader = True):
  parsed_url = parse_url(url_name)
  tcp_socket = tcp_connection(parsed_url.netloc, 80)
  http_request = encode_http_request(parsed_url.path, 'GET')
  send_http_request(tcp_socket, http_request)
  http_header = read_http_header(tcp_socket)
  http_data = read_http_body_as_binary(tcp_socket)
  decoded_message = decode_http_header(http_header)
  file_name = parsed_url.path.split('/')[-1]
  if saveheader:
    header_file_name = file_name +  '.header'
    save_text_data(http_header, header_file_name)
  if(find_content_type(decoded_message) == 'text'):
    text_file_name = file_name + '.html'
    save_binary_data(http_data, text_file_name)
  elif(find_content_type(decoded_message) == 'binary'):
    save_binary_data(http_data, file_name)
  tcp_socket.close()
if __name__ == "__main__":
  http_server(sys.argv[1])
