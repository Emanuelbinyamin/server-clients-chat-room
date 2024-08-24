# A function I dont know yet : #$$$$$$$$$$$$# ;

import socket
import threading

host = '127.0.0.1' # localhost
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port)) # server is bond to lcalhost on port 55555
server.listen() # lisening for incoming connections

clients = []
nicknames =[] # nicknames of the clients

def broadcast(message):
    for client in clients: 
        client.send(message) #$$$$$$$$$$$$#
      
# this function will late on run in a thread, for each client we will have a singale thread runining and executing the handle function,client disconnect - error - break the loop -> terminate the function -> end th thread.  
def handle(client): # run this on every individual client who connects, we are constantly trying to get messages from the client, wont give error if he doesnt send message, will give error if: this client isn't there anymore 
    while(True): # endlessloop. unless eroor
        
        try: # try to recive a message from client, succed - brodcast the message to all other client, includ that client. 
            massage = client.recv(1024)  
            broadcast(massage) 
        except: # cut the connection to this particular client, remove him from the list - clients, kill this function.
            index = clients.index(client) # finding the index of this client, to later delete.
            clients.remove(client) # removing the client from the list of clients
            client.close() # close the connection to the client.
            nickname = nicknames[index] # whenever we adding the client, we are adding the nickname --> having the same index --> removing now the nickname by the index found.
            broadcast(f"{nickname} left the chat!".encode('ascii'))
            nicknames.remove(nickname)
            break
        
def recieve():
    while True:
        # the server basicly accepting all the connections .
        client, address =server.accept() # runing the accept method all the time , if this method get a connection, returns a client and the address of the client.
        # in this case, we always goona have the same address, we are on one computer.. , if it was running on a  server, we will see the IP address of the client connecting to the server.
        # we are allowing the client to connect, if this happens, we gonna see on the server's console:
        print(f"Connected with {str(address)}")
        
        # enabling the client to give his nickname:
        client.send('NICK'.encode('ascii')) # gonna send a message to this client, this message will be a code word, which isn't visibale to the user of the client, just visibale to the client itself, later on the code.
        # if the client recieve the keyword : NICK, it should be informed, and should send the nickname to the server, so the server knows who are you. 
        nickname = client.recv(1024).decode('ascii')# 
        nicknames.append(nickname)
        clients.append(client)
        
        # we gonna see on the server's console:
        print(f'nickname of the client is : {nickname} !')
        
        broadcast(f'{nickname} joind the chat'.encode('ascii'))# every client now know there is a new client in the chat, and get a message..
        # send the client who just connected :
        client.send('Connected to the server successfully!'.encode('ascii'))
        
        # we are gonne run one thread for each client connected, because we need to handle the at the same time: like one client send, and other, and we have to prosses it in the same time
        thread = threading.Thread(target =handle, args = (client,))# the target is the handle function.
        thread.start() # start the thread handling the connection to this particular client.

print("server is listening...")
recieve() # the recieve method needs to be called, its the main method, the ony function that we call... 