# A function I dont know yet : #$$$$$$$$$$$$# ;

from email import message
import socket
import threading

host = '127.0.0.1' # localhost
port = 55555

nickname = input("Chose a nickname:  ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port)) # now we are connecting it to the server, when this line runs, it will triger the accept method on the server, and the client will be connected to the server.

# we are going to defind 2 methods, and run 2 threads simultaneously,
# 1: we are going to recieve all the time data from the server -> we gonna have a recieve function, running constantly, 
# at the same time,
# 2: we need a thread running for all the messages we are going to send.

def receive():
    while True:
        try: # trying to receive messages from the server
            message = client.recv(1024).decode('ascii')# we are still recieving from the derver, not the client -> for the server to send messages, it uses its clients, so it could be considered a cliuent.
            # we need to check if the message, that we have just recieved, is NICK or regular message.
            if message == 'NICK':
                client.send(nickname.encode('ascii'))# the server is listening all the time, the client is chosing a nickname, connecting to the server, at the mooment -> trigers the accept method (in recieve func in server.py), its prints connected with the addres, and the first thing the server then does: sends the keyword: NICK, so in client we goona get the keyword(the previos line), and we goona send the nickname(this lline of code), noe in the server its being recived, appended, and then we are having a connection. now as the server send somthing to as, we are going to recieve it and print it onto our screen(client).
            else:
                print(message)
        except:# if it doesn't work -> close the connection.
            print("An error occurred!")
            client.close()
            break
        

       
def write():
    while True:
        try:
            message = f'{nickname}: {input("")}' # we are constantly running new input functions, as soon as the user clicks enter - and sends one input -> we ask for the next one.
            # the options for the user: 1. close the client 2. write messages.
            client.send(message.encode('ascii'))
        except:
            pass
        

# now we need to run the 2 threads. for the receive, and write:

receive_thread = threading.Thread(target=receive)  
receive_thread.start() 


write_thread = threading.Thread(target=write)  
write_thread.start()    






