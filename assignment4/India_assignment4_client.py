import socket
from urllib.parse import urlparse
import sys
__author__ = "jasvinder"

# gets URL from use


# create an INET, STREAMING socket
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
#   output:
#     String - parsed Url into 6 components

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

# Receives the Http Response
def receive_http_body_as_text(tcp_connection):
  total_http_response_data = []
  http_response = tcp_connection.recv(512).decode('utf-8')
  total_http_response_data.append(http_response)
  while(http_response):
    http_response = tcp_connection.recv(512).decode('utf-8')
    total_http_response_data.append(http_response)
  return ''.join(total_http_response_data)

def read_http_header(tcp_connection):
  http_headers = []
  response = tcp_connection.recv(4).decode('utf-8')
  http_headers.append(response)
  while(True):
    if(response == '\r'):
      response = tcp_connection.recv(3).decode('utf-8')
      if(response == '\n\r\n'):
        break
      else:
        http_headers.append('\r')
        http_headers.append(response)
    response = tcp_connection.recv(1).decode('utf-8')
    http_headers.append(response)
  return ''.join(http_headers)
  
def read_http_body_as_binary(tcp_connection):
  http_headers = []
  response = tcp_connection.recv(512)
  while(response):
    http_headers.append(response)
    response = tcp_connection.recv(512)
    #http_headers.append(response)
  return http_headers

def decode_http_header(http_header):
  return http_header.split('\r\n')
  # { value.split(':')[0] : value.split(':')[1] for value in http_header.split('\r\n')}

def find_content_type(decoded_http_header):
  for value in decoded_http_header:
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
def http_server(url_name):
  parsed_url = parse_url(url_name)
  tcp_socket = tcp_connection(parsed_url.netloc, 80)
  http_request = encode_http_request(parsed_url.path, 'GET')
  send_http_request(tcp_socket, http_request)
  http_header = read_http_header(tcp_socket)
  http_data = read_http_body_as_binary(tcp_socket)
  decoded_message = decode_http_header(http_header)
  save_text_data(http_header, 'index.php.header')
  if(find_content_type(decoded_message) == 'text'):
    save_text_data(http_data, 'index.php')
  elif(find_content_type(decoded_message) == 'binary'):
    save_binary_data(http_data, 'index.jpg')
  tcp_socket.close()
http_server(sys.argv[1])
