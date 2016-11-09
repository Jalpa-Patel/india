import socket
__author__ = "jasvinder"

# create an INET, STREAMing socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# now connect to the web server on port 80 - the normal http port
clientSocket.connect(("localhost", 8080))
# get name from user
name = input("Enter your name\n")
# gets age from user
age = input("Enter your age\n")
#gets matrikelnummer from programmer
matrikelNummer = input("Enter your Matrikelnummer\n")
# Protocol for sending user input information in the key:value\n
#where key is for example the Name and value is its Value given by user.
protocolMessage = ''.join(['Name:', name, '\n', 'Age:', age, '\n', 'MatrikelNummer:', matrikelNummer, '\n'])
#Sending data from client to server
clientSocket.send(str.encode(protocolMessage))
clientSocket.close()



