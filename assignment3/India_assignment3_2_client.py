import socket
__author__ = "jasvinder"

# create an INET, STREAMing socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# now connect to the web server on port 80 - the normal http port
clientSocket.connect(("localhost", 8080))
# get URL from user
url_name = input("Enter the URL\n")

# Protocol for sending user input URL ending with \r and \n
protocolMessage = ''.join([url_name,'\r','\n'])

#Sending data from client to server
clientSocket.send(str.encode(protocolMessage))
clientSocket.close()



