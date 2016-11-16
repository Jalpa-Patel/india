import socket
__author__ = "jasvinder"

# A function to decode the URL from client into various fields i.e protocol, sub-domain,
#domain, port number, path, parameters and fragment.
def decode(data):
  decoded_message = {}
  # it removes the \r and \n from the URL given
  url_given = data.strip()
  
  protocol_and_urllist = url_given.split("://")
  # Dictionary built for saving the protocol
  decoded_message["protocol"] = protocol_and_urllist[0]
  protocol_and_urlfragmentlist = protocol_and_urllist[1].split("#")
  # Dictionary built for saving the fragment
  if len(protocol_and_urlfragmentlist) > 1: 
    decoded_message["fragment"] = protocol_and_urlfragmentlist[1] 
  url_parameterslist = protocol_and_urlfragmentlist[0].split("?")

  #Dictionary built for saving the url parameters

  if len(url_parameterslist) > 1: 

    decoded_message["parameters"] = {}
    parameters_list =  url_parameterslist[1].split("&")
    for value in parameters_list:
      key_valueList = value.split("=")
      decoded_message["parameters"][key_valueList[0]] = key_valueList[1]  
  url_portandpathlist = url_parameterslist[0].split(":")

  #Dictionary built for port no and path
  if len(url_portandpathlist) > 1:
    decoded_message["URL"] = url_portandpathlist[0]
    portandpathlist = url_portandpathlist[1].split("/")
    decoded_message["port no"] = portandpathlist[0]
    if len(portandpathlist) > 1:
      decoded_message["path"] = ""
      for value in portandpathlist[1:]:
        decoded_message["path"] = decoded_message["path"] + "/" + value


  
  else:
    url_pathlist = url_portandpathlist[0].split("/")
    decoded_message["URL"] = url_pathlist[0]
    if len(url_pathlist) >1:
      decoded_message["path"] = ""
      for value in url_pathlist[1:]:
        decoded_message["path"] = decoded_message["path"] + "/" + value

  #Dictionary built for domain
  domainlist = decoded_message["URL"].split(".")
  decoded_message["domain"] = domainlist[len(domainlist) - 1]

  #Dictionary built for sub domain
  decoded_message["sub-domain"] = ""
  for value in domainlist[:-1]:
    decoded_message["sub-domain"] = decoded_message["sub-domain"] + value + "."

  decoded_message["sub-domain"] = decoded_message["sub-domain"][:-1]
  return decoded_message

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
decoded_message = decode(client_message_in_string)
print(decoded_message)

#closing the connection
clientconnection.close()


