import socket
__author__ = "jasvinder"

# A function to decode the data from client into key value pair of lists.
# eg a data in format "Name:jass\nAge:18\nMatrikelnummer:2168756\n" is decoded into a list like this [["Name", "jass"], ["Age", "18"], ["Matrikelnummer", 2168756] ]
def decode_message(data):
  # remove last new line and then split across new line charachter
    message_line = data.strip().split("\n")
    key_value_pair = [ line.split(":") for line in message_line]
    return key_value_pair

# Prints the decoded list of key value pair in user understandable format as given in assignment.
def print_message(decoded_message):
    for key_value in decoded_message:
      print(key_value[0] + ":\t" + key_value[1]+";" )


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a localhost and port number 8080 as asked in question
serversocket.bind(("localhost", 8080))

# listen as  a server socket for incoming connection
serversocket.listen(1)
(clientconnection, address) = serversocket.accept()

#receive encoded data from client in bytes
client_message_in_bytes = clientconnection.recv(1024)

#convert the encoded data from bytes to string for decoding into key value pair.
client_message_in_string = client_message_in_bytes.decode("utf-8")

#calls decode function to decode message into list
decoded_message = decode_message(client_message_in_string)

# prints the list
print_message(decoded_message)

clientconnection.close()
