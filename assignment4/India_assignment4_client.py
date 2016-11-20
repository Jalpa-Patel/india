import socket
__author__ = "jasvinder"

# create an INET, STREAMING socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# now connect to the web server of west.uni-koblenz.de on port 80 - the normal http port
clientSocket.connect(("west.uni-koblenz.de", 80))
# get URL from user
url_name = input("Enter the URL\n")

#  User request for sending user input URL as HTTP request ending with two empty lines
get_request = ''.join(['GET',' ','url_name', 'HTTP/1.0', '\r','\n','\r','\n'])

#Sending data from client to server
clientSocket.send(str.encode(protocolMessage))
clientSocket.close()



